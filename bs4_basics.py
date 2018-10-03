from bs4 import BeautifulSoup
import requests

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")

soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")

forecast_items = seven_day.find_all(class_="tombstone-container")
data = []
for e in forecast_items:
    period = e.find(class_="period-name").get_text()

    desc = e.find('img').get('title', None) + '\n'

    temp = e.find(class_="temp temp-low")
    if type(temp) != type(None):
        temp = temp.get_text() + ' '
    else:
        temp = e.find(class_="temp temp-high").get_text() + ' '
    data.append((period, temp,desc))


with open('file_1.txt','w') as f:
    for e in data:
        f.write(e[0])
        f.write(e[1])
        f.write(e[2])
