
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.euroairport.com/en/flights/daily-arrivals.html"
response = requests.get(url)
arrivals_soup = BeautifulSoup(response.text, 'html.parser')

table = arrivals_soup.find('div', {'class': 'cblock modules-flights-flightlist modules-flights'})
row0 = table.find_all('tr', {'class': 'row-0'})
row1 = table.find_all('tr', {'class': 'row-1'})

fluege = []

for elem in row0:
    ga_zeit = elem.find('td', {'class': 'first'}).text
    herkunft = elem.find('td', {'class': 'first'}).find_next_sibling('td').text
    airline = elem.find('td', {'class': 'first'}).find_next_sibling('td').find_next_sibling('td').text.replace('\n', '').replace('\t','')
    nummer = elem.find('td', {'class': 'first'}).find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace('\t','').replace('\n', '')
    a_zeit = elem.find('td', {'class': 'first'}).find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace('\t','').replace('\n', '')
    typ = elem.find('td', {'class': 'last'}).text

    mini_dict = {'Geplante Ankunft': ga_zeit,
                 'Ankunft': a_zeit,
                 'Ankunft aus': herkunft,
                 'Flugnummer': nummer,
                 'Passagier/Cargo': typ}

    fluege.append(mini_dict)

fluege1 = [] #das ändern

for elem in row1:
    ga_zeit = elem.find('td', {'class': 'first'}).text
    herkunft = elem.find('td', {'class': 'first'}).find_next_sibling('td').text
    airline = elem.find('td', {'class': 'first'}).find_next_sibling('td').find_next_sibling('td').text.replace('\n', '').replace('\t','')
    nummer = elem.find('td', {'class': 'first'}).find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace('\t','').replace('\n', '')
    a_zeit = elem.find('td', {'class': 'first'}).find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text.replace('\t','').replace('\n', '')
    typ = elem.find('td', {'class': 'last'}).text

    mini_dict = {'Geplante Ankunft': ga_zeit,
                 'Ankunft': a_zeit,
                 'Ankunft aus': herkunft,
                 'Flugnummer': nummer,
                 'Passagier/Cargo': typ}

    fluege1.append(mini_dict) #und hier

f = fluege + fluege1

pd.DataFrame(f).to_csv('scraped_data.csv')
