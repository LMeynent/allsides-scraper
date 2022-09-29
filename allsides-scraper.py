import pandas as pd
import os
import re
import requests

from bs4 import BeautifulSoup
from tqdm import tqdm
from time import sleep

rgx_type = re.compile(r"- ([\w\s]+).html")
rgx_title = re.compile(
    r"<td class=\"views-field views-field-title source-title\">\n<a href=\"([\S]+)\">([^<]+)<\/a> <\/td>")
rgx_bias = re.compile(
    r"<a href=\"https:\/\/www.allsides.com\/media-bias\/[\w-]+\"><img alt=\"AllSides Media Bias Rating: ([\w\s]+)\"")
rgx_agree = re.compile(r"<span class=\"agree\">(\d+)<\/span>\/<span class=\"disagree\">(\d+)<\/span>")
rgx_url = re.compile(r"href=\"([^\"]+)\"")
rgx_confidence = re.compile(r"<span>AllSides has <\/span>([^<\s]+)[^<]*<span>")

if __name__ == '__main__':
    files = os.listdir('html')

    df = pd.DataFrame(columns=['bias', 'type', 'allsides_url', 'agree', 'disagree'])

    for file in tqdm(files, desc='Reading files', unit='file'):
        with open(os.path.join('html', file), 'r') as html_page:
            media_type = rgx_type.search(file)[1]
            soup = BeautifulSoup(html_page, 'html.parser')
            for element in soup.find_all('tr', class_='even') + soup.find_all('tr', class_='odd'):
                try:
                    element = str(element)

                    match = rgx_title.search(element)
                    url, title = match[1], match[2]

                    match = rgx_bias.search(element)
                    rating = match[1]

                    match = rgx_agree.search(element)
                    agree, disagree = int(match[1]), int(match[2])

                    df.loc[title] = (rating, media_type, url, agree, disagree)
                except TypeError:
                    print('\nError in element:')
                    print(element)
                    print()

    for idx, data in tqdm(df.iterrows(), total=len(df), unit='element', desc='Scraping'):
        sleep(1)
        soup = BeautifulSoup(requests.get(data['allsides_url']).text, 'html.parser')

        match = rgx_url.search(str(soup.find('a', title=idx)))
        if match is not None:
            df.loc[idx, 'url'] = match[1]

        match = rgx_confidence.search(str(soup.find('ul', class_='b-list')))
        if match is not None:
            df.loc[idx, 'confidence'] = match[1]

    df.to_csv('allsides.csv')
