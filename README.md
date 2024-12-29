# Libroguessr
# **Projet Python 2A**

**Arnaud BARRAT** • **Lucas CUMUNEL** • **Aloys GALLO**

# Contexte

Libroguessr est un projet s'inscrivant dans le cadre du cours _Python pour la data science_ dispensé par Lino Galiana l'année scolaire 2024-2025. 


# Problématique

**Comment classifier les textes littéraires ? Qui peut établir une classification des textes littéraires ?** Le développement du traitement automatique du langage permet de réintroduire et de réinterpréter ces débats pluriséculaires. Le **Natural Language Processing (NLP)** permet en effet, de **quantifier et d'analyser des corpus littéraires**, en utilisant des modèles et des techniques qui analysent les structures et les thématiques sous-jacentes des textes.

Grâce à des outils tels que l'**'analyse de sentiment**, la **modélisation des sujets** (LDA), ou encore l'**embedding des mots** (comme Word2Vec ou BERT), on peut extraire des informations sur le contenu, les relations entre les mots et les concepts présents dans les textes. Ces techniques permettent de **classer** les textes non seulement par genre, mais aussi par **thèmes récurrents**, **motifs littéraires** ou **structures narratives**, ouvrant ainsi la voie à une nouvelle forme de classification basée sur des critères textuels.

En ce sens, le NLP permet d'**automatiser** une tâche qui a traditionnellement été subjective, en remplaçant ou en complétant le jugement humain par des modèles statistiques. 

Ainsi, ce projet a pour vocation de s'inscrire dans ces débats autour de la question suivante : **malgré leur diversité de style et de contenu, les textes littéraires peuvent-ils être regroupés efficacement uniquement à partir de leurs textes pour déterminer des regroupements thématiques précis et pertinents à l’aide de modèles de machine learning ?** 

Ce projet pourrait avoir _in fine_ des applications plus concrètes. Avec une base de données plus large, on pourrait établir des clusters plus précis permettant d'émettre des recommandation pertinente de livres aux lecteurs, en fonction des livres qu'ils ont aimés.

# Présentation des données

La première étape de notre travail a été de **récupérer les données** dont nous avions besoin. Pour ce faire, nous nous sommes rapidement tournés vers le site du projet [**Gutenberg**](https://www.gutenberg.org/), qui met gratuitement à disposition des ebooks. Nous avons sélectionné uniquement des **textes en français** d'auteurs **classiques du XVIIᵉ, du XVIIIᵉ et du XIXᵉ siècles**. Comme ce site ne fournissait pas les thèmes des ouvrages, pour les définir, nous avons utilisé l'API [**Open Library**](https://openlibrary.org/), puis l'API [**Lingva Translate**](https://lingva.ml/) pour traduire ces thèmes, puisqu'ils stockés en anglais ou dans d'autres langues. Notons que ce sont les deux seuls API gratuites que nous avons trouvé pour réaliser ces étapes. Or, celle-ci ne connaît les thèmes que des ouvrages les plus connus, ce qui explique notre choix. En effet, lorsque nous proposions des ouvrages moins célèbres, l'API ne donnait souvent aucun thème. Le temps très élevé qui aurait été nécessaire pour faire une requête concernant les plus de **3800 ouvrages** que nous avions pu récupérer nous a dissuadé de le faire. En parallèle, même si nous l'avions fait, la taille des données aurait été telle que notre puissance computantionnelle aurait été largement insuffisante pour traiter de une base de données avec autant de contenu textuel. Par exemple, supposons que pour tous les livres, on ait au moins 40 000 mots, nous aurions dû traiter plus de 152 millions de mots. Cela a contraint notre base de données à se limiter à **88 textes**. Toutefois, la **longueur de ces textes** semble à nos yeux compenser ce faible nombre.

A partir de cette base de données de 88 livres, nous avons **scrappé** la page [**gutindex.all**](https://www.gutenberg.org/dirs/GUTINDEX.ALL.iso-8859-1.txt) du site destiné à cet effet. Cette page recense l'ensemble des oeuvres disponibles et leur numéro d'index. Nous avons donc réalisé une **table** avec les informations sur l'ouvrage dans une colonne et le numéro d'index dans l'autre, nous avons trié ces ouvrages en fonction des caractéristiques recherchées et nous nous sommes servis de l'index pour récupérer le texte de chaque livre.


# Structure du git 

Le notebook [Notebook.ipynb](Notebook.ipynb) fournit les instructions détaillées pour utiliser le programme.


# Tokenisation des données


# Stat desc ???


# Clustering des livres : Application de la méthode VBGMM



III. Présentation des conclusions 

IV. Pistes d'améliorations




Structure : 
1 - Récupération de données 
2 - Transformation des données
3 - Statistiques descriptives
4 - Les modèles + 5 - Résultats 
(6 - Autocritique ?))

1 - Récupération des données


2- Transformation des données (coucou Lucas)
Après avoir confectionné une base de données exploitable, nous avons du transformer les textes de manière à pouvoir leur appliquer différents modèles.


3 - Statistiques descriptives
Avant d'appliquer les modèles, nous nous sommes interrogés sur le contenu des textes. LEs graphiques montrent des occurences de mots.................

4 - 
