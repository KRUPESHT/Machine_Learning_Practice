import plotly.graph_objs as go
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True)
import pandas as pd

df1 = pd.read_csv('2014_World_Power_Consumption')

data = dict(type='choropleth',
            locations=df1['Country'],
            locationmode='country names',
            z=df1['Power Consumption KWH'],
            text=df1['Country'],
            colorbar={'title':'Power Consumption KWH'})
layout = dict(title='2014 Power Consumption',
              geo=dict(showframe=False, projection={'type':'mercator'}))
choromap = go.Figure(data=[data], layout = layout)
iplot(choromap, validate=False)