import requests
import bs4
import re
import pandas as pd

#Requirements : pip install bs4 lxml
#On veut récupérer l'index qui lie chaque livre à un nombre 

url_liste_textes = "https://www.gutenberg.org/dirs/GUTINDEX.ALL.iso-8859-1.txt"

request_liste_textes = requests.get(url_liste_textes).content

page = bs4.BeautifulSoup(request_liste_textes, "lxml")

body = page.find("body")

index_texte = body.get_text()

# Chercher les indices des marqueurs "<===LISTINGS=== >" et "<==End of GUTINDEX.ALL==>"
start_marker = "<===LISTINGS===>"
end_marker = "<==End of GUTINDEX.ALL==>"

# Trouver les positions de début et de fin
start_index = index_texte.find(start_marker)
end_index = index_texte.find(end_marker)

# Extraire le texte entre les deux marqueurs
texte_extrait = index_texte[start_index + len(start_marker):end_index].strip()    


texte_extrait_lignes = texte_extrait.splitlines()

#La ligne 1a sera la première de la table de correspondance 
print(texte_extrait_lignes[10])
#La dernière est bien
print(texte_extrait_lignes[len(texte_extrait_lignes)-1])


# On garde uniquement les lignes qui constituent la table de correspondance
texte_extrait_lignes_trié = texte_extrait_lignes[10:len(texte_extrait_lignes)-1]

# Fusionner les lignes triées pour obtenir une chaîne complète
texte_complet = '\n'.join(texte_extrait_lignes_trié)

# Utiliser le premier regex pour diviser le texte en œuvres (chaque œuvre est séparée par un ou plusieurs sauts de ligne)
oeuvres = re.split(r'(?=\n{2,})', texte_complet.strip())

# Préparer une liste pour les données finales
data = []

# Étape 2 : Traiter chaque œuvre séparément
for oeuvre in oeuvres:
    # Utiliser le deuxième regex pour extraire l'index (numéro associé à l'œuvre)
    match_index = re.search(r'(?<=\s\s)([\d]+?[A-Z]?)(?=\n)', oeuvre)
    
    if match_index:
        index = match_index.group(1)  # Extraire l'index
    else:
        index = None  # Si aucun index n'est trouvé
    
    # Nettoyer le texte de l'œuvre en supprimant l'index et les espaces inutiles
    description = re.sub(r'(?<=\s\s)([\d]+?[A-Z]?)(?=\n)', '', oeuvre).strip()
    
    # Ajouter l'entrée à la liste des données
    data.append({"Description": description, "Index": index})

# Étape 3 : Convertir en DataFrame pour structuration
df = pd.DataFrame(data)

'''
# Étape 4 : Nettoyer les valeurs de la colonne 'Index' et les convertir en entier
df['Index'] = df['Index'].str.replace(r'[^\d]', '', regex=True)  # Supprimer tout caractère non numérique
df['Index'] = pd.to_numeric(df['Index'], errors='coerce')  # Convertir en entier, NaN si invalide
'''

