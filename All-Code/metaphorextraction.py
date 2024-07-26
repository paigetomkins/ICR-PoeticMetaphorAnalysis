import spacy
import textacy
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

def extract():
    
    nlp = spacy.load("en_core_web_sm")

    #doc = nlp(text)

    patterns = [[{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "NOUN"}], [{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "DEP"}, {"POS": "NOUN"}], [{"POS": "ADJ"}, {"POS": "NOUN"}]]
    
    metaphorical_phrases = list(textacy.extract.matches.token_matches(row[1], patterns=patterns))
    return(metaphorical_phrases)

def main():
    
    df = pd.read_csv('../fulldataset.csv')

    rows = df.head(2)
    print(rows)

    newdf = df.copy()

    newdf['metaphors'] = np.nan

    for i, row in newdf.iterrows():
        metaphor = newdf['content'].apply(extract)
        newdf[i].fillna(metaphor)

    results = newdf.loc['metaphors']
    print(results)
        
        
main()

