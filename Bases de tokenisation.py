"""
import nltk
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("genesis")
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.stem import WordNetLemmatizer
"""
#pas sûr de l'utilité de nltk

"""
install spacy --> pip install spacy
modèle de langage fr --> spacy download fr_core_news_sm 
pour les lemmes --> pip install spacy-lefff
"""
import spacy 
from spacy_lefff import LefffLemmatizer


sample_txt="Le malheureux Dantès désespère dans sa captivité jusqu'à songer au suicide. Il a la chance de faire la connaissance de l'abbé Faria, un autre prisonnier qui, voulant s'évader, a creusé un tunnel qui débouche non sur la mer mais dans la cellule de Dantès, et sauve Dantès qui se laissait mourir de faim. Edmond Dantès découvre alors en l'abbé Faria une personne exceptionnelle, érudit dans tous les domaines scientifiques et philosophiques. L'abbé Faria fait la lumière sur le complot machiné contre Edmond en lui montrant son écriture de la main gauche qui ressemble étrangement à celle de la lettre et en lui expliquant que M. Noirtier est en réalité le père de Villefort. Ces révélations instillent la vengeance dans le cœur d'Edmond. L'abbé Faria, très érudit, se lie d'amitié avec Dantès et lui donne une éducation exceptionnelle tant en économie qu'en sciences, en politique, en philosophie mais aussi en langues. Faria fait une première crise de catalepsie qui le laisse paralysé d'un bras et d'une jambe rendant ainsi l'évasion qu'ils préparaient impossible. Il lui fait alors part d'un secret qui le fait lui-même passer pour fou aux yeux de ses geôliers et, pendant un court moment, de Dantès : il est le dépositaire d'un immense trésor, celui des Spada, enfoui depuis des siècles dans l'île de Monte Cristo. Le vieux prêtre meurt d'un troisième accès et Edmond, pensant pouvoir s'échapper, prend la place du cadavre dans le linceul, en se munissant d'un couteau au cas où il serait découvert. Il comprend au dernier moment que tous les prisonniers morts en captivité sont jetés à la mer avec aux pieds un boulet de trente-six1 au château d'If et se libère grâce à son couteau. Sa captivité aura duré quinze ans. Edmond nage jusqu'à l'île de Tiboulen et est récupéré par un bateau de contrebandiers avec lesquels il noue des liens. C'est grâce à ce bateau, sur lequel il travaille temporairement comme marin, qu'il parvient à atteindre l'île de Monte-Cristo. Devenu très riche grâce au trésor des Spada dont il prend possession, Dantès retourne à Marseille où il apprend la mort de son père et constate la disparition de ses quatre « amis » : Danglars, Fernand, Caderousse et Villefort."

nlp = spacy.load("fr_core_news_sm")
doc = nlp(sample_txt)
text_tokenized = []
for token in doc :
    text_tokenized += [token.text]#text tokénisé

stop_words_french = nlp.Defaults.stop_words #liste de stopwords fr
text_tokenized = [x for x in text_tokenized if x not in stop_words_french] #virer les "stopwords à partir d'une liste"


french_lemmatizer = LefffLemmatizer(after_melt=True)

for d in doc:
    print(d.text, d.tag_, d.lemma_)#tag=type de mot et lemma_ = version lemmatisée
text_lemmatized=[d.lemma_ for d in doc]
text_lemmatized

from collections import Counter
import numpy as np

tk_count=Counter(text_tokenized)
tk_count_all = list(tk_count.items())



