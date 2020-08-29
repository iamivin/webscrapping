import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
Url = 'https://www.whitehouse.gov/presidential-actions/page/'
pgno = 1
link = []
while pgno<150:
    if pgno == 1:
        page = requests.get('https://www.whitehouse.gov/presidential-actions/')
        soup = BeautifulSoup(page.content, 'html.parser')
        contents = soup.find_all(class_='presidential-action__title')
        link2 =[content.find('a').text for content in contents]
        link.extend(link2)
        pgno = pgno + 1
    else:
        page = requests.get(Url + str(pgno) )
        soup = BeautifulSoup(page.content, 'html.parser')
        contents = soup.find_all(class_='presidential-action__title')
        link2 = [content.find('a').text for content in contents]
        link.extend(link2)
        pgno = pgno + 1
        
        
while ('' in link):
    link.remove('')

whitehousenotifications = pd.DataFrame(
    {
        'Data': link
    })

whitehousenotifications.to_csv('whitehousekeralanotifications.csv')
