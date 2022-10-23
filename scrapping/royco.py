import pandas as pd
import requests
from bs4 import BeautifulSoup
import http.client 
import json

http.client._MAXHEADERS = 1000

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'}

link = pd.read_csv('files/royco_links.csv')
urls = link['loc'].to_list()
print('load dataset')

recipes = {}

l = len(urls)
for i, url in enumerate(urls):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    print('scraping: '+str(i) +'/'+str(l))
    recipe = {
    'id': i+1414,
    'title': soup.find('h1', class_='o-text__heading-1').text,
    'ingred ients': [item.text for item in soup.find_all('li', class_='c-recipe-content-ingredients__list-item')],
    'step': [item.text for item in soup.find_all('span', class_='c-recipe-cooking-method__description')]
    }
        
    recipes.append(recipe)
    print('scraped: '+ url)

print('finished scraping')
#saving to json
with open('files/royco_recipes.json', 'w') as fp:
    json.dump(recipes, fp)
print('saved to json')
