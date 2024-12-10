"""
les pip :
spacy
spacy-lefff
collections
pandas
git+https://github.com/ClaudeCoulombe/FrenchLefffLemmatizer.git

le reste :
spacy download fr_core_news_sm 
"""

#Imports
import spacy 
from spacy_lefff import LefffLemmatizer
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer
import pandas as pd
from collections import Counter


#Set up

sample_txt="Le malheureux Dantès désespère dans sa captivité jusqu'à songer au suicide. Il a la chance de faire la connaissance de l'abbé Faria, un autre prisonnier qui, voulant s'évader, a creusé un tunnel qui débouche non sur la mer mais dans la cellule de Dantès, et sauve Dantès qui se laissait mourir de faim. Edmond Dantès découvre alors en l'abbé Faria une personne exceptionnelle, érudit dans tous les domaines scientifiques et philosophiques. L'abbé Faria fait la lumière sur le complot machiné contre Edmond en lui montrant son écriture de la main gauche qui ressemble étrangement à celle de la lettre et en lui expliquant que M. Noirtier est en réalité le père de Villefort. Ces révélations instillent la vengeance dans le cœur d'Edmond. L'abbé Faria, très érudit, se lie d'amitié avec Dantès et lui donne une éducation exceptionnelle tant en économie qu'en sciences, en politique, en philosophie mais aussi en langues. Faria fait une première crise de catalepsie qui le laisse paralysé d'un bras et d'une jambe rendant ainsi l'évasion qu'ils préparaient impossible. Il lui fait alors part d'un secret qui le fait lui-même passer pour fou aux yeux de ses geôliers et, pendant un court moment, de Dantès : il est le dépositaire d'un immense trésor, celui des Spada, enfoui depuis des siècles dans l'île de Monte Cristo. Le vieux prêtre meurt d'un troisième accès et Edmond, pensant pouvoir s'échapper, prend la place du cadavre dans le linceul, en se munissant d'un couteau au cas où il serait découvert. Il comprend au dernier moment que tous les prisonniers morts en captivité sont jetés à la mer avec aux pieds un boulet de trente-six1 au château d'If et se libère grâce à son couteau. Sa captivité aura duré quinze ans. Edmond nage jusqu'à l'île de Tiboulen et est récupéré par un bateau de contrebandiers avec lesquels il noue des liens. C'est grâce à ce bateau, sur lequel il travaille temporairement comme marin, qu'il parvient à atteindre l'île de Monte-Cristo. Devenu très riche grâce au trésor des Spada dont il prend possession, Dantès retourne à Marseille où il apprend la mort de son père et constate la disparition de ses quatre « amis » : Danglars, Fernand, Caderousse et Villefort."

nlp = spacy.load("fr_core_news_sm")  #modèle français
txt = nlp(sample_txt) #adapte le texte au modèle français
txt_tokenized = [t.text for t in txt]
stop_words_french = nlp.Defaults.stop_words #liste de stopwords fr

#Treatment with Spacy
txt_token_stop = [t for t in txt_tokenized if t not in stop_words_french] #vire les "stopwords"

txt_lemmatized=[t.lemma_ for t in txt]

txt_lemma_stop = [t for t in txt_lemmatized if t not in stop_words_french]

#Treatment with Claude Coulombe
lemmatizer = FrenchLefffLemmatizer()
type_lemmatized_CC=[lemmatizer.lemmatize(t,'all') for t in txt_token_stop]
type_lemmatized_CC=[t[0] for t in type_lemmatized_CC if len(t)!=0]
txt_lemmatized_CC=[t[0] for t in type_lemmatized_CC]


#Tables
txt_type=[(t.lemma_,t.tag_) for t in txt]
txt_type=[t for t in txt_type if t[0] not in stop_words_french]
d_type=pd.DataFrame(data=text_type, columns=['Word','Type'])

tk_count=Counter(txt_lemmatized)
d_count=pd.DataFrame.from_dict(data=tk_count,orient='index',columns=["Count"])
d_count=count.reset_index()
d_count=count.rename(columns={"index":"Word"})

d_summary_order=d_type.rename_axis(index='Order')
d_summary=d_type.merge(d_count,on='Word')
d_summary=d_summary.sort_values('Count', ascending=False)
d_summary=d_summary.reset_index(drop=True)
d_summary=d_summary.drop_duplicates(subset=['Word'])


d_type_CC=pd.DataFrame(data=type_lemmatized_CC,columns=["Word","Type"])
tk_count_CC=Counter(txt_lemmatized_CC)
d_count_CC=pd.DataFrame.from_dict(data=tk_count,orient='index',columns=["Count"])
d_count_CC=count.reset_index()
d_count_CC=count.rename(columns={"index":"Word"})

d_summary_order_CC=d_type_CC.rename_axis(index='Order')
d_summary_CC=d_type_CC.merge(d_count_CC,on='Word')
d_summary_CC=d_summary_CC.sort_values('Count', ascending=False)
d_summary_CC=d_summary_CC.reset_index(drop=True)
d_summary_CC=d_summary_CC.drop_duplicates(subset=['Word'])




#fonctioniser
#pip dans readme ou mieux --> requirements (version et packages necessaires --> pip install -r requirements.txt)



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