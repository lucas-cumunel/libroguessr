

"""
install spacy --> pip install spacy
modèle de langage fr --> spacy download fr_core_news_sm 
pour les lemmes --> pip install spacy-lefff
"""
import spacy 
from spacy_lefff import LefffLemmatizer
import pandas as pd
from collections import Counter

sample_txt="Le malheureux Dantès désespère dans sa captivité jusqu'à songer au suicide. Il a la chance de faire la connaissance de l'abbé Faria, un autre prisonnier qui, voulant s'évader, a creusé un tunnel qui débouche non sur la mer mais dans la cellule de Dantès, et sauve Dantès qui se laissait mourir de faim. Edmond Dantès découvre alors en l'abbé Faria une personne exceptionnelle, érudit dans tous les domaines scientifiques et philosophiques. L'abbé Faria fait la lumière sur le complot machiné contre Edmond en lui montrant son écriture de la main gauche qui ressemble étrangement à celle de la lettre et en lui expliquant que M. Noirtier est en réalité le père de Villefort. Ces révélations instillent la vengeance dans le cœur d'Edmond. L'abbé Faria, très érudit, se lie d'amitié avec Dantès et lui donne une éducation exceptionnelle tant en économie qu'en sciences, en politique, en philosophie mais aussi en langues. Faria fait une première crise de catalepsie qui le laisse paralysé d'un bras et d'une jambe rendant ainsi l'évasion qu'ils préparaient impossible. Il lui fait alors part d'un secret qui le fait lui-même passer pour fou aux yeux de ses geôliers et, pendant un court moment, de Dantès : il est le dépositaire d'un immense trésor, celui des Spada, enfoui depuis des siècles dans l'île de Monte Cristo. Le vieux prêtre meurt d'un troisième accès et Edmond, pensant pouvoir s'échapper, prend la place du cadavre dans le linceul, en se munissant d'un couteau au cas où il serait découvert. Il comprend au dernier moment que tous les prisonniers morts en captivité sont jetés à la mer avec aux pieds un boulet de trente-six1 au château d'If et se libère grâce à son couteau. Sa captivité aura duré quinze ans. Edmond nage jusqu'à l'île de Tiboulen et est récupéré par un bateau de contrebandiers avec lesquels il noue des liens. C'est grâce à ce bateau, sur lequel il travaille temporairement comme marin, qu'il parvient à atteindre l'île de Monte-Cristo. Devenu très riche grâce au trésor des Spada dont il prend possession, Dantès retourne à Marseille où il apprend la mort de son père et constate la disparition de ses quatre « amis » : Danglars, Fernand, Caderousse et Villefort."

nlp = spacy.load("fr_core_news_sm")
txt = nlp(sample_txt)

txt_tokenized = [t.text for t in txt]

stop_words_french = nlp.Defaults.stop_words #liste de stopwords fr

txt_token_stop = [t for t in txt_tokenized if t not in stop_words_french] #virer les "stopwords" à partir d'une liste

txt_lemmatized=[t.lemma_ for t in txt]

txt_lemma_stop = [t for t in txt_lemmatized if t not in stop_words_french]

txt_type=[(t.lemma_,t.tag_) for t in txt]
txt_type=[t for t in txt_type if t[0] not in stop_words_french]

pip install git+https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer.git
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
lemmatizer = FrenchLefffLemmatizer()
test=[lemmatizer.lemmatize(t,'all') for t in txt_token_stop]
test=[t[0] for t in test if len(t)!=0]
d_test=pd.DataFrame(data=test)


tk_count=Counter(txt_lemmatized)

type=pd.DataFrame(data=text_type, columns=['Word','Type'])


count=pd.DataFrame.from_dict(data=tk_count,orient='index',columns=["Count"])
count=count.reset_index()
count=count.rename(columns={"index":"Word"})

summary_order=type.rename_axis(index='Order')
summary=type.merge(count,on='Word')
summary=summary.sort_values('Count', ascending=False)
summary=summary.reset_index(drop=True)
summary=summary.drop_duplicates(subset=['Word'])

pip dans readme ou mieux --> requirements (version et packages necessaires --> pip install -r requirements.txt)



#bordel
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
pos = POSTagger()
french_lemmatizer = LefffLemmatizer(after_melt=True)
nlp.add_pipe(name='pos', after='parser')
nlp.add_pipe(french_lemmatizer, name='lefff', after='pos')

test=[d._.lefff_lemma for d in txt]
from spacy_lefff import LefffLemmatizer,POSTagger
test


french_lemmatizer = LefffLemmatizer(after_melt=True)
"""