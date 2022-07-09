import spacy

# Loading pre-trained model
NLP = spacy.load("en_core_web_sm")

contents = ""

# Processing whole documents
with open("../input.txt", "r") as inputFile:
        contents = inputFile.read()

document = NLP(contents)

# Find phrases and concepts
for word in document:
        if(word.pos_ == "VERB" or word.pos_ == "NOUN"):
                print(word, spacy.explain(word.pos_))

# Find named entities
for word in document.ents:
        print(word.text, word.label_, sep="-")