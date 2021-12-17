from random import randint
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

#Sr.No,Mobile Brand,Avg Rating
df = pd.read_csv('D:\Documents\school\jr\PRIVATE\Python\Project 108\data.csv')
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"],show_hist=False)
fig.show()