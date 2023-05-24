import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()
# Читаем данные из файла
with open('D:\python_projects\Dash\data\my_series.json', 'r') as f:
    data = json.load(f)
    
df = pd.DataFrame(data)
df.reset_index(inplace=True)
df.columns = ['cluster', 'count']

fig = go.Figure(
    data=[go.Pie(labels=df['cluster'], values=df['count'])],
    layout=go.Layout(title='Pie chart of clusters')
)

app.layout = html.Div([
    html.H1('Pie chart of clusters'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
