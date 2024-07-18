import spacy

with open("/home/paige-tomkins/Downloads/alice.txt", "r") as f:
    text = f.read()
   # print (text)
    chapters = text.split("CHAPTER ")[1:]
    #print (chapters[1])

chapter1 = chapters[0]

nlp = spacy.load("en_core_web_sm")

doc = nlp(chapter1)
sentences = list(doc.sents)
sentence = (sentences[2])

for token in sentence:
    print (token.text, token.pos_)
    
