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

app.layout = html.Div(children=[html.H1(children = 'Bees Line Plot') ,
                      dcc.Graph(
                          id = 'line-plot',
                          figure = {
                              'data' : [
                                  go.Line(
                                  x = df['State'],
                                  y = df['Pct of Colonies Impacted'],
                                  marker = dict(color = 'indigo')
                              )
                              ],
                          }
                      )
                      ]
                      )

if __name__ == '__main__':
    app.run_server(debug = True)