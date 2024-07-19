import spacy
import textacy 

with open("/home/paige-tomkins/Downloads/alice.txt", "r") as f:
    text = f.read().replace("\n\n", " ") #allows smaller spacy model to better separate sentences
    chapters = text.split("CHAPTER ")[1:]
    
  
chapter1 = chapters[0]

nlp = spacy.load("en_core_web_sm")

doc = nlp(chapter1)
sentences = list(doc.sents)
sentence = (sentences[2])

patterns = [[{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "PRON"}], [{"POS": "PRON"}, {"POS": "VERB"}]]

verb_phrases = textacy.extract.matches.token_matches(doc, patterns=patterns)

for verb_phrase in verb_phrases:
    print (verb_phrase)

