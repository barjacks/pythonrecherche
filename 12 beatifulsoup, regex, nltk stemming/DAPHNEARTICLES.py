# coding: utf-8

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import progressbar


df = pd.read_csv('allPosts.csv', sep='\t', encoding='utf-16')
urls = list(df['Link'])
titles = list(df['Title'])

bar = progressbar.ProgressBar()

text_list = []
for url,i in zip(urls, bar(range(len(urls)))):
    response = requests.get(url)
    t = BeautifulSoup(response.text, 'html.parser')
    at = ''
    for elem in t.find_all('p'):
        at += elem.text
    text_list.append({'Text':at})

txt_lst = list(pd.DataFrame(text_list)['Text'])
df['Text'] = txt_lst
df.to_csv('allPostText.csv')
