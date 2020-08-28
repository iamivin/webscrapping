import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.whitehouse.gov/presidential-actions/')
soup = BeautifulSoup(page.content, 'html.parser')
contents = soup.find_all(class_='presidential-action__title')
link = [content.find('a').text for content in contents]


prdnotifications = pd.DataFrame(
    {
        'Data': link
    })

prdnotifications.to_csv('prdkeralanotifications.csv')
