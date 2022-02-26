import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("StudentsPerformance.csv")

list = df["math score"].tolist()


mean = statistics.mean(list)
median = statistics.median(list)
mode = statistics.mode(list)

std_dev = statistics.stdev(list)

print(f"mean , median and mode of math score are {mean},{median} and {mode}.")

stdev1,stdev2 = mean-std_dev,mean+std_dev

stdev12,stdev22 = mean-(2*std_dev),mean+(2*std_dev)

stdev13,stdev23 = mean-(3*std_dev),mean+(3*std_dev)

center_list = [result for result in list if result>stdev1 and result<stdev2]

center_list2 = [result for result in list if result>stdev12 and result<stdev22]

center_list3 = [result for result in list if result>stdev13 and result<stdev23]

print("{}% of data lies in center of math score list".format(len(center_list)*100/len(list)))

print("{}% of data lies in center of math score list".format(len(center_list2)*100/len(list)))

print("{}% of data lies in center of math score list".format(len(center_list3)*100/len(list)))

fig = ff.create_distplot([df["math score"].tolist()],["Math Score"],show_hist=False)
fig.show()
