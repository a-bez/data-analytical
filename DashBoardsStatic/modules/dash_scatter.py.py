import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import json
# импортируем данные
with open('D:\python_projects\Dash\data\main_data.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

print(df)
# Create the Dash app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Scatter Plot'),

    # Create the scatter plot
    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['cluster'] == i]['cluster'],
                    y=df[df['cluster'] == i]['processed_text'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='Cluster {}'.format(i)
                ) for i in df['cluster'].unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'clusters'},
                yaxis={'title': 'processed_text'},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

