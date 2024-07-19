import spacy
from spacy import displacy

with open("/home/paige-tomkins/Downloads/alice.txt", "r") as f:
    text = f.read().replace("\n\n", " ") #allows smaller spacy model to better separate sentences
    chapters = text.split("CHAPTER ")[1:]
    
  
chapter1 = chapters[0]

nlp = spacy.load("en_core_web_sm")

doc = nlp(text)
sentences = list(doc.sents)
sentence = (sentences[8])

html = displacy.render(doc, style="ent")

with open ("data_vis.html", "w") as f:
    f.write(html)
