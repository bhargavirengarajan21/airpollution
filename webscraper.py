from bs4 import BeautifulSoup
import requests
import re
from datetime import date
def scrapWeb(city):
  URL = "http://www.dpccairdata.com/dpccairdata/display/"+city
  r = requests.get(URL)
  soup = BeautifulSoup(r.content, 'html5lib')
  table =  soup.find_all('table')
  data = table[4].find_all('tr')
  p = re.compile("\d+\.\d+")
  a1 = {
  "NH3 (ug/m3)": p.findall(data[1].find_all('td')[4].text)[0],
  "NO2 (ug/m3)": p.findall(data[5].find_all('td')[3].text.encode("ascii","ignore").decode())[0],
  "NO (ug/m3)":  p.findall(data[6].find_all('td')[3].text.encode("ascii","ignore").decode())[0],
  "SO2 (ug/m3)": p.findall(data[10].find_all('td')[3].text.encode("ascii","ignore").decode())[0],
  "CO (mg/m3)":  p.findall(data[4].find_all('td')[3].text.encode("ascii","ignore").decode())[0],
  "Ozone (ug/m3)":p.findall(data[8].find_all('td')[3].text.encode("ascii","ignore").decode())[0]
  }
  data = table[7].find_all('tr')
  a2 = {
  'BP (mmHg)': p.findall(data[4].find_all('td')[3].text.encode("ascii","ignore").decode())[0], 
  'AT ()': p.findall(data[3].find_all('td')[3].text.encode("ascii","ignore").decode())[0], 
  'RH (%)': p.findall(data[6].find_all('td')[3].text.encode("ascii","ignore").decode())[0], 
  'WD': p.findall(data[10].find_all('td')[3].text.encode("ascii","ignore").decode())[0],
  'PM2.5 (ug/m3)': p.findall(data[5].find_all('td')[3].text.encode("ascii","ignore").decode())[0]
  }
  today = date.today()
  attribute = {
  'Date': today
  }
  attribute.update(a1)
  attribute.update(a2)
  return attribute
