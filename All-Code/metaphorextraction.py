import spacy
import textacy

with open("/home/paige-tomkins/Downloads/archive(2)/all.txt", "r") as f:
    text = f.read().replace("\n\n", " ") #allows smaller spacy model to better separate sentences
    #chapters = text.split("CHAPTER ")[1:]
    
  
#chapter1 = chapters[0]

nlp = spacy.load("en_core_web_lg")

doc = nlp(text)
sentences = list(doc.sents)
sentence = (sentences[2])

patterns = [[{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "NOUN"}], [{"POS": "NOUN"}, {"POS": "VERB"}, {"POS": "DEP"}, {"POS": "NOUN"}], [{"POS": "ADJ"}, {"POS": "NOUN"}]]

verb_phrases = textacy.extract.matches.token_matches(doc, patterns=patterns)

for verb_phrase in verb_phrases:
    print (verb_phrase)


