import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://ktu.edu.in/eu/core/announcements.htm')
soup = BeautifulSoup(page.content, 'html.parser')
contents = soup.find(class_='c-details')
items= contents.find_all('tr')

date = [item.find(class_='news-date').get_text() for item in items]
maindata = []
subdata = []
i = 0
while len(items)>i:
    data = items[i].get_text().splitlines()
    while ('' in data):
        data.remove('')
    maindata.append(data[3])
    subdata.append(data[4:])
    i = i+1
while ('' in maindata):
    maindata.remove('')
while ('' in subdata):
    subdata.remove()

ktunotifications = pd.DataFrame(
    {
        'Date': date,
        'notificatin': maindata,
        'details': subdata,
    })


#print(weatherdata)
ktunotifications.to_csv('ktunotifications.csv')
