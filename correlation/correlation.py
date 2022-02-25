import numpy as np
import csv

def getdatasource(datapath):
    with open(datapath) as f:
        data = csv.reader(f)
        datalist = list(data)
        
    datalist.pop(0)
    list1 = []
    list2 =[]
       
    for i in datalist:
        list1.append(float(i[0]))
        list2.append(float(i[1]))
        
    return {"x":list1,"y":list2}

def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
    
    
findcorrelation(getdatasource("cupOfCoffeevsHoursOfSleep.csv"))

findcorrelation(getdatasource("marksVsAttendence.csv"))
 
