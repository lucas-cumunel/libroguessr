# libroguessr
I. Contexte


I. Introduction : pitch & problématique


II. Lien vers notebook


III. Présentation des conclusions 

IV. Pistes d'améliorations



Peut-on prévoir le thème d'un livre à partir de son texte ?

L'objectif de notre projet est d'essayer de prédire le ou les thèmes d'un livre à partir de son texte. Il s'agit en effet d'utiliser des méthodes de NLP 

faut ajouter une ou deux lignes de blabla

Structure : 
1 - Récupération de données 
2 - Transformation des données
3 - Statistiques descriptives
4 - Les modèles + 5 - Résultats 
(6 - Autocritique ?))

1 - Récupération des données
La première étape de notre travail a été de récupérer les données dont nous avions besoin. Pour ce faire, nous nous sommes rapidement tournés vers le site du projet Gutenberg (https://www.gutenberg.org/), qui met gratuitement à disposition des ebooks. Nous avons sélectionné uniquement des textes en français d'auteurs classiques des XVIIᵉ, XVIIIᵉ et XIXᵉ siècles. En effet, pour définir les thèmes de chaque ouvrage, nous avons utilisé l'API open library (demander à Arnaud). Or, celle-ci ne connait les thèmes que des ouvrages les plus connus, ce qui explique notre choix. En effet, lorsque nous proposions des ouvrages moins célèbres, l'API ne donnait souvent aucun thème. Le temps très élevé qui aurait été nécessaire pour faire une requête concernant les plus de 3800 ouvrages que nos avions pu récupérer nous a dissuadé de le faire. Cela a contraint notre base de données à se limiter à 88 textes, quand bien même nous souhaitions en avoir plus de 100 à l'origine. Toutefois, la longueur de ces textes semble à no yeux compenser ce faible nombre. 
Concrètement, nous avons scrappé la page gutindex.all du site destiné à cette effet. Cette page recense l'ensemble des oeuvres disponibles et leur numéro d'index. Nous avons donc réalisé une table avec les inforations sur l'ouvrage dans une colonne et le numéro d'index dans l'autre, nous avons trié ces ouvrages en fonctions des caractéristiques recherchées et nous nous sommes servis de l'index pour récupérer le texte de chaque livre. 
Il nous a enfin fallu nettoyer le code afin d'éviter les erreurs.

2- Transformation des données (coucou Lucas)
Après avoir confectionné une base de données exploitable, nous avons du transformer les textes de manière à pouvoir leur appliquer différents modèles.


3 - Statistiques descriptives
Avant d'appliquer les modèles, nous nous sommes interrogés sur le contenu des textes. LEs graphiques montrent des occurences de mots.................

4 - 
