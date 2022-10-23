import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'}

link = pd.read_csv('files/masakapa_links.csv')
urls = link['loc'].to_list()
print('load dataset')

recipes = []

l = len(urls)
try:
    for i, url in enumerate(urls):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        print('scraping: '+str(i) +'/'+str(l))
        recipe = {
            'id': i,
            'title': soup.find('h1', class_='title text-center mb-4').text,
            'ingredients': [item.text for item in soup.find_all('div', class_='ingredient-wrapper d-inline-flex')],
            'step': [item.text for item in soup.find_all('div', class_='col step-description d-flex align-items-center ml-md-2')]
        }
        recipes.append(recipe)
        print('scraped: '+ url)
except:
    print('Error')

print('finished scraping')
#saving to json
with open('files/masakapa_recipes.json', 'w') as fp:
    json.dump(recipes, fp)
print('saved to json')
