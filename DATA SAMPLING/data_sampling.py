import plotly.figure_factory as ff
import pandas as pd
import csv
import random
import statistics
import plotly.graph_objects as go

df  = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

# fig = ff.create_distplot([data],["Math Scores"],show_hist=False)
# fig.show()

mean = statistics.mean(data)
stdev = statistics.stdev(data)
print("Populating Mean :- ",mean)

# Giving Tablets
# Extra classes for 2 hours
# Fun quizzes for homework

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
    mean_of_sampling_data = statistics.mean((mean_list))
    print("Sampling Mean :- ",mean_of_sampling_data)
    
    
def setup():
    mean_list = []
    for i in range(0,1000):
        meanlist , stdev3 = random_set(100)
        mean_list.append(meanlist)
    stdev4 = statistics.stdev(mean_list)
        
    show_fig(mean_list)
    
setup()


