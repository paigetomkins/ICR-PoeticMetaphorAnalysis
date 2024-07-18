import spacy

with open("/home/paige-tomkins/Downloads/alice.txt", "r") as f:
    text = f.read().replace("\n\n", " ") #allows smaller spacy model to better separate sentences
    chapters = text.split("CHAPTER ")[1:]
    
  
chapter1 = chapters[0]

nlp = spacy.load("en_core_web_sm")

doc = nlp(chapter1)
sentences = list(doc.sents)
sentence = (sentences[1])
#print(sentence)
ents = list(doc.ents) #looks for all instances of named entities in a text
print(ents[0].label)
print(ents[0].label_)
print(ents[0].text)

people = []

for ent in ents:
    if ent.label_ == "PERSON":
        people.append(ent)
print (people)


#for token in sentence:
 #   print (token.text, token.pos_)
    
