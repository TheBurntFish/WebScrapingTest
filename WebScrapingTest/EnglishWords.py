import json
import random


myFile = open('words_dictionary.json')
myDictionary = json.loads(myFile.read())
myKeys = list(myDictionary.keys())
rand = random.randint(0, len(myKeys))
word = myKeys[rand]
print(len(myKeys))
print('Word #{0}: {1}'.format(rand, word))