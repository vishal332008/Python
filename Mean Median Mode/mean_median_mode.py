import csv
import pandas as pd
import statistics

df  = pd.read_csv("SOCR-HeightWeight.csv")
data = df["Weight(Pounds)"].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

print("Mean (Average) is -> " + str(mean) + "\n" + "Median is -> " + str(median) + "\n" + "Mode is -> " + str(mode))
