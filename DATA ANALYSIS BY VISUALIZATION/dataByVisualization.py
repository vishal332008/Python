import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("levels.csv")

fig = px.scatter(df,x="student_id",y="level",color = "attempt",title="Levels")
fig.show()
