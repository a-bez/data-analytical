import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

# Создаем датафрейм
df = pd.DataFrame({
    'cluster': [3, 1, 4, 2, 0],
    'nums': [4348, 2066, 807, 304, 206],
    'key_words': [
        'get, like, day, time, know, want, got, one, too, really',
        'like, feel, know, want, life, get, time, even, people, way',
        'depression, http, anxiety, people, help, one, support, mental, illness, https',
        'work, day, get, like, want, job, back, got, week, time',
        'sleep, get, hour, day, going, night, like, feel, want, bed'
    ]
})

# Создаем объект Scatter и указываем данные для оси x и y
trace = go.Scatter(
    x=df['cluster'],
    y=df['nums'],
    mode='markers',
    text=df['key_words'],
    marker=dict(
        size=15,
        color=df['cluster'],
        opacity=0.7,
        line=dict(width=0.5, color='white')
    )
)

# Создаем объект Layout для настройки внешнего вида графика
layout = go.Layout(
    xaxis=dict(title='Cluster'),
    yaxis=dict(title='Nums'),
    hovermode='closest'
)

# Создаем объект Figure, который объединяет объект Scatter и объект Layout
fig = go.Figure(data=[trace], layout=layout)

# Создаем приложение Dash
app = dash.Dash(__name__)

# Создаем макет для приложения Dash
app.layout = html.Div(children=[
    html.H1(children='Scatter plot'),

    # Выводим график с помощью объекта dcc.Graph и объекта Figure
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Запускаем приложение Dash
if __name__ == '__main__':
    app.run_server(debug=True)
