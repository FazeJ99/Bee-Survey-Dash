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
df_sorted = df.sort_values(by='Pct of Colonies Impacted', ascending=False)

app.layout = html.Div(children=[html.H1(children='Bees Bar Plot')  ,
          dcc.Graph(
              figure = {
                  'data':[go.Bar(
                      x = df_sorted['State'],
                      y = df_sorted['Pct of Colonies Impacted'],
                      marker = dict(color='blue')
                  )
                      ],
                  'layout':go.Layout(
                      title  = 'Bees Bar Plot',
                  )
              }
          )                      
                                ])

if __name__ == '__main__':
    app.run_server(debug = True)
    