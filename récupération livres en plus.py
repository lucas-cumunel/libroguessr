import requests
import bs4
import pandas as pd



#Requirements : pip install bs4 lxml rapidfuzz

#On récupère une liste d'oeuvres qu'on sait présentes sur le site pour ensuite demander leur thème 
# à l'API de chatgpt 
url_liste_oeuvres = "https://www.gutenberg.org/browse/scores/top-fr.php#books-last1"
request_liste_oeuvres = requests.get(url_liste_oeuvres).content

page_oeuvres = bs4.BeautifulSoup(request_liste_oeuvres, "lxml")

body_oeuvres = page_oeuvres.find("ol")

#On veut uniquement garder le texte sans les balises et le chiffre à la fin (nombre de téléchargements hier)
liste_li = body_oeuvres.find_all("li")

# Extraire les titres et auteurs
oeuvres_auteurs_pour_API = []
for li in liste_li:
    # Récupérer le texte brut (sans balises HTML)
    texte = li.get_text()
    # Supprimer les numéros entre parenthèses et tout ce qui suit
    texte = texte.split(" (")[0]
    oeuvres_auteurs_pour_API.append(texte)

#On supprime manuellement une oeuvre qui est en anglais
oeuvres_auteurs_pour_API = [ligne for ligne in oeuvres_auteurs_pour_API if ligne != "French Conversation and Composition by Harry Vincent Wann"]

df_oeuvres_pour_API = pd.DataFrame(oeuvres_auteurs_pour_API, columns=["Titre et Auteur"])
df_oeuvres_pour_API.to_csv("oeuvres_auteurs_pour_API.csv", index=False, encoding="utf-8")
