
# coding: utf-8

from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import progressbar

bar = progressbar.ProgressBar()
lst = []
lst_pass = []

for elem,i in zip(range(1,13000), bar((range(1,13000)))):

    url = "https://www.zueriwieneu.ch/report/" + str(elem)
    response = requests.get(url)
    züri_soup = BeautifulSoup(response.text, 'html.parser')

    if züri_soup.find('h1').text != 'Melden Sie Schäden an der Infrastruktur von Zürich':
        Mini_dict = {
            'Kategorie' : züri_soup.find('h1').text,
            'Meldedatum' : züri_soup.find('div', {'class':'problem-header clearfix'}).find('p').text.strip(),
            'Meldung' : züri_soup.find('div', {'class':'problem-header clearfix'}).find_all('p')[1],
            'Antwortdatum' : züri_soup.find('ul', {'class':'item-list item-list--updates'}).find_all('p')[0].text,
            'Antwort' : züri_soup.find('ul', {'class':'item-list item-list--updates'}).find_all('p')[1].text,
            'URL' : url,
            'Lat' : float(züri_soup.find('div', {'id':'js-map-data'}).get('data-latitude')),
            'Long': float(züri_soup.find('div', {'id':'js-map-data'}).get('data-longitude'))
            }
        lst.append(Mini_dict)
    else:
        lst_pass.append(url)

date = time.strftime("%Y-%m-%d%H:%M:%S")
pd.DataFrame(lst).to_csv(date+'züriwieneu.csv')
