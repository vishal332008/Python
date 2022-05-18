from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)
soup = bs(page.text,'html.parser')
star_table = soup.find_all('table')
temp_list= []
for tr in star_table[5].find_all('tr'):
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
Names = []
Distance =[]
Mass = []
Radius =[]
for i in range(1,len(temp_list)):
    Names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(Names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])

df.to_csv('dwarfs.csv')
