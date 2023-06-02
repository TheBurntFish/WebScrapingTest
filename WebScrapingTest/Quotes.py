

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



driver = webdriver.Firefox()
driver.get("https://quotes.toscrape.com")

all_quotes = []
all_authors = []

while True:
    
    quotes = (driver.find_elements(By.CLASS_NAME, 'text'))
    authors = (driver.find_elements(By.CLASS_NAME, 'author'))

    for quote, author in zip(quotes,authors):
        all_quotes.append(quote.text)
        all_authors.append(author.text)

    try:
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Next')
    except:
        break
    else:
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Next').click()

for quote, author in zip(all_quotes, all_authors):
    print(quote + "\n- " + author)

driver.close()


