import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import json

# Читаем данные из файла и конвертируем в датафрейм
with open('D:\python_projects\Dash\data\my_series.json', 'r') as f:
    my_ser = json.load(f)
with open('D:\python_projects\Dash\data\joind_keywords.json', 'r') as f:
    key_words = json.load(f)
merged_data = {**my_ser, **key_words}
df = pd.DataFrame(merged_data)




# Создаем приложение Dash
app = dash.Dash()

# Определяем макет приложения
app.layout = html.Div([
    html.H1('Гистограмма кластеров'),
    dcc.Graph(
        id='cluster-histogram',
        figure={
            'data': [go.Bar(
                x=df.index,
                y=df['nums'],
                hovertext=df['keywords']
            )],
            'layout': go.Layout(
                title='Количество документов в каждом кластере',
                xaxis=dict(title='Кластер'),
                yaxis=dict(title='Количество документов')
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
