from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json
import random

def chooseWord():
    inp = input("Choose an English word\n")
    if(inp == ""):
        print("Selecting random word...")
        myFile = open('words_dictionary.json')
        myDictionary = json.loads(myFile.read())
        myKeys = list(myDictionary.keys())
        rand = random.randint(0, len(myKeys))
        word = myKeys[rand]

        myFile.close()
        print('Word #{0}: {1}'.format(rand, word))
        inp = word
    return inp

inp = chooseWord()

driver = webdriver.Firefox()
driver.get("https://www.merriam-webster.com")



search = driver.find_element(By.ID, "search-term")
search.send_keys(inp)
search.send_keys(Keys.RETURN)

driver.implicitly_wait(10)
print("Word: " + inp)

parts = driver.find_element(By.CLASS_NAME, "important-blue-link")
print("Part of speech: " + parts.text)

definitions = driver.find_elements(By.CLASS_NAME,"dtText")
for count, define in enumerate(definitions, 0):
    print(count, define.text)

driver.close()







