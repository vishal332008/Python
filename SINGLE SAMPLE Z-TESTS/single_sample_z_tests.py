import plotly.figure_factory as ff
import pandas as pd
import csv
import random
import statistics
import plotly.graph_objects as go

df  = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("Mean of Sampling Distribution : ",mean)
print("Standard Deviation of Sampling Distribution : ",stdev)


def random_set(counter):
    dataset = []

    for i in range(0,counter):
        index = random.randint(0,len(data)-1)
        value = data[index]
        dataset.append(value)
    
    mean_random = statistics.mean(dataset)
    stdev2 = statistics.stdev(dataset)
    return mean_random,stdev2

def show_fig(mean_list):
    df1 = mean_list
    mean_of_sampling_data = statistics.mean((mean_list))
    stdev4 = statistics.stdev(mean_list)
   
    first_std_deviation_start,first_std_deviation_end = mean_of_sampling_data -stdev4, mean_of_sampling_data+stdev4
    second_std_deviation_start,second_std_deviation_end = mean_of_sampling_data -(2*stdev4), mean_of_sampling_data+(2*stdev4)
    third_std_deviation_start,third_std_deviation_end = mean_of_sampling_data -(3*stdev4), mean_of_sampling_data+(3*stdev4)
    
    print("Mean of sample1 : ",mean_of_sampling_data)
    print("Z score : " , (mean_of_sampling_data-mean)/stdev)
    
    fig = ff.create_distplot([df1],["Mean"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean_of_sampling_data,mean_of_sampling_data],y=[0,0.17],mode="lines",name = "MEAN"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name = "STANDARD DEVIATION 1 END"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name = "STANDARD DEVIATION 2 END"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name = "STANDARD DEVIATION 3 END"))
    fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name = "STANDARD DEVIATION 1 START"))
    fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name = "STANDARD DEVIATION 2 START"))
    fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name = "STANDARD DEVIATION 3 START"))
    fig.show()
    
def setup():
    mean_list = []
    for i in range(0,1000):
        meanlist , stdev3 = random_set(100)
        mean_list.append(meanlist)
    stdev4 = statistics.stdev(mean_list)
        
    show_fig(mean_list)
    
setup()
