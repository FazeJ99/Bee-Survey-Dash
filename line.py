import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

df = pd.read_csv("Dataset/intro_bees.csv")
#df = pd.read_csv("https://raw.githubusercontent.com/LubangaD/beesurveydashboard/refs/heads/main/Dataset/intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df.head()) 

dff = df.copy()
dff = dff[(dff['State'] == 'Idaho') | (dff['State'] == "New York") | (dff['State'] == "New Mexico")]
dff = dff[(dff['Year'] == 2015) | (dff['Year'] == 2016) | (dff['Year'] == 2017)]

app.layout = html.Div(children=[html.H1(children = 'Bees Line Plot') ,
                      dcc.Graph(
                          id = 'line-plot',
                          figure = {
                              'data' : [
                                  go.Line(
                                  x = dff['Year'],
                                  y = dff['Pct of Colonies Impacted'],
                                  color = 'Affected by'
                              )
                              ],
                          }
                      )
                      ]
                      )

if __name__ == '__main__':
    app.run_server(debug = True)