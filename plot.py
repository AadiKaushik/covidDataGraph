import pandas as pd
import plotly.express as px

df = pd.read_csv('C:/Users/aadi_\Desktop/coding/python/dataVisulation/covivd-19.csv')
fig = px.scatter(df,x='date',y='cases',color='country')
fig.show()