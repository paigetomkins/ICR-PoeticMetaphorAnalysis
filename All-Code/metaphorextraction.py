import spacy
from spacy import displacy
import textacy
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import re

#Extracting the metaphors
pd.set_option('max_colwidth', None)
df = pd.read_csv('../fulldataset.csv', index_col = 'poem name')
newdf = df.head(273).copy()
newdf = newdf.drop_duplicates(subset=['content'])
newdf = newdf.drop('type', axis=1)
#
newdf['type one/two metaphors'] = None
newdf['type three metaphors'] = None
newdf['type four metaphors'] = None
newdf['type five metaphors'] = None
newdf['type six metaphors'] = None
newdf['type seven metaphors'] = None
newdf['type eight metaphors'] = None
newdf['type nine metaphors'] = None
newdf['total metaphors'] = None
newdf['ratio'] = None
#
for i, row in newdf.iterrows():
    nlp = spacy.load("en_core_web_sm")
    poem = row['content']
    processed = nlp(poem)
    TypeOne_Two = [[{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "NOUN"}], [{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}]]
    TypeThree = [{"POS": "ADJ"}, {"POS": "NOUN"}]
    TypeFour = [{"POS": "NOUN"}, {"POS": "VERB"}]
    TypeFive = [{"POS": "NOUN"}, {"POS": "AUX"}, {"POS": "VERB"}]
    TypeSix = [{"POS": "NOUN"}, {"POS": "PART"}, {"POS": "NOUN"}]
    TypeSeven = [{"POS": "NOUN"}, {"POS": "PART"}, {"POS": "ADJ"}, {"POS": "NOUN"}]
    TypeEight = [{"POS": "ADJ"}, {"POS": "CONJ"}, {"POS": "NOUN"}]
    TypeNine = [{"POS": "VERB"}, {"POS": "NOUN"}]
    total = [[{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "NOUN"}], [{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "DET"}, {"POS": "NOUN"}], [{"POS": "ADJ"}, {"POS": "NOUN"}], [{"POS": "NOUN"}, {"POS": "VERB"}], [{"POS": "NOUN"}, {"POS": "AUX"}, {"POS": "VERB"}], [{"POS": "NOUN"}, {"POS": "PART"}, {"POS": "NOUN"}], [{"POS": "NOUN"}, {"POS": "PART"}, {"POS": "ADJ"}, {"POS": "NOUN"}], [{"POS": "ADJ"}, {"POS": "CONJ"}, {"POS": "NOUN"}], [{"POS": "VERB"}, {"POS": "NOUN"}]]
    TypeOne_TwoMetaphors = list(textacy.extract.matches.token_matches(processed, patterns=TypeOne_Two))
    TypeThreeMetaphors = list(textacy.extract.matches.token_matches(processed, patterns=TypeThree))
    TypeFourMetaphors = list(textacy.extract.matches.token_matches(processed, patterns=TypeFour))
    TypeFiveMetaphors = list(textacy.extract.matches.token_matches(processed, patterns=TypeFive))
    TypeSix_metaphors = list(textacy.extract.matches.token_matches(processed, patterns = TypeSix))
    TypeSeven_metaphors = list(textacy.extract.matches.token_matches(processed, patterns = TypeSeven))
    TypeEight_metaphors = list(textacy.extract.matches.token_matches(processed, patterns = TypeEight))
    TypeNine_metaphors = list(textacy.extract.matches.token_matches(processed, patterns = TypeNine))
    total_metaphors = list(textacy.extract.matches.token_matches(processed, patterns = total))
    newdf.at[i, 'type one/two metaphors'] = TypeOne_TwoMetaphors
    newdf.at[i, 'type three metaphors'] = TypeThreeMetaphors
    newdf.at[i, 'type four metaphors'] = TypeFourMetaphors
    newdf.at[i, 'type five metaphors'] = TypeFiveMetaphors
    newdf.at[i, 'type six metaphors'] = TypeSix_metaphors
    newdf.at[i, 'type seven metaphors'] = TypeSeven_metaphors
    newdf.at[i, 'type eight metaphors'] = TypeEight_metaphors
    newdf.at[i, 'type nine metaphors'] = TypeNine_metaphors
    newdf.at[i, 'total metaphors'] = total_metaphors
    #print("allowed values to be entered")

#Extracting the number of metaphors present per row
newdf['number of metaphors'] = None
newdf['number of one/two metaphors'] = None
newdf['number of three metaphors'] = None
newdf['number of four metaphors'] = None
newdf['number of five metaphors'] = None
newdf['number of six metaphors'] = None
newdf['number of seven metaphors'] = None
newdf['number of eight metaphors'] = None
newdf['number of nine metaphors'] = None
for i, row in newdf.iterrows():
    num_metaphorstotal = len(newdf.loc[i, 'total metaphors'])
    newdf.at[i, 'number of metaphors'] = num_metaphorstotal
    num_metaphorsone_two = len(newdf.loc[i, 'type one/two metaphors'])
    newdf.at[i, 'number of one/two metaphors'] = num_metaphorsone_two
    num_metaphorsthree = len(newdf.loc[i, 'type three metaphors'])
    newdf.at[i, 'number of three metaphors'] = num_metaphorsthree
    num_metaphorsfour = len(newdf.loc[i, 'type four metaphors'])
    newdf.at[i, 'number of four metaphors'] = num_metaphorsfour
    num_metaphorsfive = len(newdf.loc[i, 'type five metaphors'])
    newdf.at[i, 'number of five metaphors'] = num_metaphorsfive
    num_metaphorssix = len(newdf.loc[i, 'type six metaphors'])
    newdf.at[i, 'number of six metaphors'] = num_metaphorssix
    num_metaphorsseven = len(newdf.loc[i, 'type seven metaphors'])
    newdf.at[i, 'number of seven metaphors'] = num_metaphorsseven
    num_metaphorseight = len(newdf.loc[i, 'type eight metaphors'])
    newdf.at[i, 'number of eight metaphors'] = num_metaphorseight
    num_metaphorsnine = len(newdf.loc[i, 'type nine metaphors'])
    newdf.at[i, 'number of nine metaphors'] = num_metaphorsnine    

"""    
amount = newdf.loc[:, 'number of metaphors']
print(amount)
"""
#Mean
averagemetaphor = (newdf['ratio'].mean())
print(averagemetaphor)
averagemetaphor = averagemetaphor/1

#Overall Number of Metaphors per Era
newdf.groupby(['age'])['number of metaphors'].sum().plot(kind='bar')
plt.xlabel("Time Period")
plt.ylabel("Number of Metaphors")
plt.title("Metaphor Frequency Between Eras")
plt.show()

#Author Metaphor Usage Frequency--Raw
newdf.groupby(['author'])['number of metaphors'].sum().astype(int).nlargest(10).plot(kind='bar')
plt.xlabel("Author")
plt.ylabel("Number of Metaphors")
plt.title("Metaphor Frequency By Author (raw)")
plt.show()

#Author Metaphor Usage Frequency--metaphor to poem length ratio
for i, row in newdf.iterrows(): #iterates through each row of newdf
    numwords = len(re.findall(r'\w+', (newdf.at[i, 'content'])))
    metaphor_ratio = (newdf.at[i, 'number of metaphors'])/(numwords)
    #calculates the metaphor to poem length ratio by taking the number of total metaphors,
    #converting it to a float, and then dividing it by the length of the content at the specific index in the newdf
    newdf.at[i, 'ratio'] = metaphor_ratio #inserts newfound value into the correct slot of 'ratio'
newdf.groupby(['author'])['ratio'].sum().astype('float64').nlargest(10).plot(kind='bar', width=1)
plt.xlabel("Author")
plt.ylabel("Metaphor to Poem Length Ratio")
plt.title("Metaphor Frequency By Author (refined)")
plt.show()

#Metaphor Type Usage Over Time Graph
newdf.plot(x="age", y=["number of one/two metaphors", "number of three metaphors", "number of four metaphors", "number of five metaphors", "number of six metaphors", "number of seven metaphors", "number of eight metaphors", "number of nine metaphors"], kind="bar", figsize=(10, 10), stacked=True)
plt.show()


