import spacy
import textacy
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

#Extracting the metaphors
newdf = pd.read_csv('../fulldataset.csv')
newdf['metaphors'] = None
for i, row in newdf.iterrows():
    nlp = spacy.load("en_core_web_sm")
    poem = row['content']
    processed = nlp(poem)
    patterns = [[{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "NOUN"}], [{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "DEP"}, {"POS": "NOUN"}], [{"POS": "ADJ"}, {"POS": "NOUN"}]]
    metaphorical_phrases = list(textacy.extract.matches.token_matches(processed, patterns=patterns))
    newdf.at[i, 'metaphors'] = metaphorical_phrases
results = newdf.loc[:, 'metaphors']
print(results)

#Extracting the number of metaphors present per row
newdf['number of metaphors'] = None
for i, row in newdf.iterrows():
    num_metaphors = len(newdf.loc[i, 'metaphors'])
    newdf.at[i, 'number of metaphors'] = num_metaphors
amount = newdf.loc[:, 'number of metaphors']
print(amount)



