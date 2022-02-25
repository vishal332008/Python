import csv
import math

with open("marks.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
data = file_data[0]

def mean(data):
    m = 0
    for i in data:
        m = m+float(i)
    n = len(data)
    o = m/n
    return o

slist = []

for num in data:
    p = float(num)-mean(data)
    p = p**2
    slist.append(p)
    
sum = 0

for j in slist:
    sum = sum + float(j)
    
result = sum/(len(data)-1)

sd = math.sqrt(result)

print(sd)
