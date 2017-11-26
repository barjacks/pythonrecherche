
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
import progressbar

bar = progressbar.ProgressBar()
new_lst = []

# showcase for the first 9 pages / to get all pages change to range(1,1443)
for elem,i in zip(range(1,1443), bar((range(1,1443)))):

    page = "https://daphnecaruanagalizia.com/page/" + str(elem)

    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'html.parser')

    posts = soup.find_all("div", class_="postmaster")

    for element in posts:

        url = element.a["href"]

        url_temp = url.replace("https://daphnecaruanagalizia.com/", "")
        date_y = url_temp[:4]
        date_m = url_temp[5:7]

        # dealing with error message stemming from one post on page 127
        try:
            date_t = element.find(class_="time").get_text()
        except AttributeError:
            date_t = "n.a."

        title = element.a["title"]
        title = title.replace("Permanent Link to ", "")

        post_id = element.get('data-postid')

        response = requests.get(url)
        abc = BeautifulSoup(response.text, 'html.parser')
        text = abc.find('div', {'class': 'entry'}).text.strip()
        text = text.replace('\n', ' ')

        temp_dict = {'Link': url,
                    'Title': title,
                    'Txt': text,
                    'Date_1': date_y,
                    'Date_2': date_m,
                    'Date_3': date_t,
                    'ID_post': post_id,
                    'ID_page': i }

        new_lst.append(temp_dict)


df = pd.DataFrame(new_lst)
df.to_csv('daphne.csv', sep='\t', encoding='utf-16')
