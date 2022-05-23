from bs4 import BeautifulSoup as bs
import csv

data = []

with open("dwarfs.csv") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)


        
headers = data[0]

for i in headers:
    data = data[data[i].notna()]

body = data[1:]
   
temp_body = [] 

for row in body:
    value = float(row[3])*0.000954588
    row[3] = value
    temp_body.append(row)
    
new_body = []

for row in temp_body:
    value = float(row[4])*0.000954588
    row[4] = value
    new_body.append(row)
    
with open("updated_dwarfs.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(new_body)
