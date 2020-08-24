import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?CityName=Franconia&state=NH&site=GYX&lat=44.2269&lon=-71.7483#.X0NdHMgzZPY')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-container')

items = week.find_all(class_='tombstone-container')
"""
print(items[3].find(class_='period-name').get_text())
print(items[3].find(class_='short-desc').get_text())
print(items[3].find(class_='temp').get_text())
"""
period_names = [item.find(class_='period-name').get_text() for item in items]
desc = [item.find(class_='short-desc').get_text() for item in items]
temp = [item.find(class_='temp').get_text() for item in items]
"""
code for test

print(period_names)
print(desc)
print(temp)
"""

weatherdata = pd.DataFrame(
    {
        'period': period_names,
        'short_description': desc,
        'tempratures': temp,
    })


#print(weatherdata)
weatherdata.to_csv('weatherforcast.csv')