import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://ktu.edu.in/eu/core/announcements.htm')
soup = BeautifulSoup(page.content, 'html.parser')
contents = soup.find(class_='c-details')

date= [content.find(class_='news-date').get_text() for content in contents]
print(date)
"""
table = contents.find('table')
table_rows = table.find_all('tr')
file = open('ktunotifications.csv', 'a+', newline ='\n')

for tr in table_rows:
    td = tr.find_all('td')
    row.{i.text for i in td}
    

    #print(row)
print(row)
with file:     
    write = csv.writer(file) 
    write.writerows(row) 
"""



    

    