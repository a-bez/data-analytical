import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import json
# импортируем данные
with open('D:\python_projects\Dash\data\processed_sentiment_df.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

fig = px.scatter(df, x='cluster', y='sentiment_score')
# Create the Dash app
app = dash.Dash()

# Define the layout of the app
app.layout = html.Div(children=[
    html.H1(children='Точечная диаграмма кластеров и счета сентимент-анализа'),
    dcc.Graph(
        id='sentiment-cluster-plot',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

