import requests
import bs4
import re
import pandas as pd
from rapidfuzz import fuzz

# Requirements : pip install bs4 lxml rapidfuzz

# URL du fichier d'index des textes
url_liste_textes = "https://www.gutenberg.org/dirs/GUTINDEX.ALL.iso-8859-1.txt"

# Téléchargement du fichier d'index
request_liste_textes = requests.get(url_liste_textes).content
page = bs4.BeautifulSoup(request_liste_textes, "lxml")
body = page.find("body")
index_texte = body.get_text()

# Chercher les indices des marqueurs "<===LISTINGS===>" et "<==End of GUTINDEX.ALL==>"
start_marker = "<===LISTINGS===>"
end_marker = "<==End of GUTINDEX.ALL==>"
start_index = index_texte.find(start_marker)
end_index = index_texte.find(end_marker)

# Extraire le texte entre les marqueurs
texte_extrait = index_texte[start_index + len(start_marker):end_index].strip()
texte_extrait_lignes = texte_extrait.splitlines()

# Filtrer les lignes pertinentes
texte_extrait_lignes_trie = texte_extrait_lignes[10:len(texte_extrait_lignes)-1]
texte_complet = '\n'.join(texte_extrait_lignes_trie)

# Diviser le texte en oeuvres
oeuvres = re.split(r'(?=\n{2,})', texte_complet.strip())

# Extraire les descriptions et indices
# Liste pour stocker les données extraites
data = []
for oeuvre in oeuvres:
    # Trouver l'index dans l'oeuvre
    match_index = re.search(r'(?<=\s\s)([\d]+?[A-Z]?)(?=\n)', oeuvre)
    index = match_index.group(1) if match_index else None

    # Nettoyer le texte de l'oeuvre
    description = re.sub(r'(?<=\s\s)([\d]+?[A-Z]?)(?=\n)', '', oeuvre).strip()

    # Ajouter les données
    data.append({"Description": description, "Index": index})

# Convertir les données en DataFrame
df = pd.DataFrame(data)

# Charger la base CSV avec les livres pour ajouter l'index
books2 = "final_list"  # Nom du fichier d'entrée
base_csv = pd.read_csv(books2)

# Conserver la colonne 'Description' dans la base initiale
base_csv['Description'] = ""
indices = []

# Parcourir les titres et auteurs en parallèle
for title, author in zip(base_csv['Title'], base_csv['Author']):
    # Nettoyage des données : normalisation
    df['Description_clean'] = df['Description'].str.strip().str.lower()
    title_clean = title.strip().lower()
    author_clean = author.strip().lower()

    # Correspondances exactes et approximatives
    df['Exact_Match'] = df['Description_clean'].str.match(rf"^{re.escape(title_clean)}(\s|[.,;!?]|$)", na=False)
    title_words = title_clean.split()
    df['Description_start'] = df['Description_clean'].str.split().str[:len(title_words)].str.join(' ')
    df['Starts_With_Title'] = df['Description_start'] == title_clean
    df['Similarity'] = df['Description_clean'].apply(lambda x: fuzz.ratio(title_clean, x[:len(title_clean)]))
    similarity_threshold = 90
    df['Approx_Match'] = df['Similarity'] > similarity_threshold
    df['Author_Present'] = df['Description_clean'].str.contains(author_clean, na=False)

    # Fusionner les critères
    df['Final_Match'] = (df['Exact_Match'] | df['Starts_With_Title'] | df['Approx_Match']) & df['Author_Present']
    match = df[df['Final_Match']]

    if not match.empty:
        # Ajouter l'index et la description correspondants
        indices.append(match.iloc[0]['Index'])
        base_csv.loc[base_csv['Title'] == title, 'Description'] = match.iloc[0]['Description']
    else:
        indices.append(None)

# Ajouter les indices trouvés à la base
base_csv['Index'] = indices

# Supprimer les lignes sans index trouvé
base_csv_clean = base_csv.dropna(subset=['Index'])

# Sauvegarder la base mise à jour
base_csv_clean.to_csv("base_csv_avec_index.csv", index=False)

# Charger la base nettoyée pour ajouter les textes
base_csv_index = pd.read_csv("base_csv_avec_index.csv")
base_csv_index['Texte'] = ""

# Télécharger les textes des livres
for livre, index in base_csv_index[['Title', 'Index']].itertuples(index=False):
    url = f"https://www.gutenberg.org/cache/epub/{index}/pg{index}-images.html"
    response = requests.get(url)

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()

        start_marker = f"*** START OF THE PROJECT GUTENBERG EBOOK "
        end_marker = f"*** END OF THE PROJECT GUTENBERG EBOOK"
        start_index = page_text.find(start_marker)
        end_index = page_text.find(end_marker)

        if start_index != -1 and end_index != -1:
            texte_extrait = page_text[start_index + len(start_marker):end_index].strip()
            base_csv_index.loc[base_csv_index['Title'] == livre, 'Texte'] = texte_extrait
        else:
            print(f"Marqueurs non trouvés pour {livre} (Index {index}).")
    else:
        print(f"Erreur lors du téléchargement de la page pour {livre} (Index {index}).")

base_csv_index = base_csv_index[base_csv_index["Description"].str.contains(r"\[Language: French\]", na=False)]

# Sauvegarder la base finale
base_csv_index.to_csv("Data/base_csv_final.csv", index=False)
print(base_csv_index.head())
print(base_csv_index.shape[0])