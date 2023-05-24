import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import json

# Читаем данные из файла
with open('D:\python_projects\Dash\data\my_series.json', 'r') as f:
    data = json.load(f)
print(data)
# Создаем приложение Dash
# app = dash.Dash()

# # Определяем макет приложения
# app.layout = html.Div([
#     html.H1('Круговая диаграмма кластеров'),
#     dcc.Graph(
#         id='cluster-pie-chart',
#         figure={
#             'data': [go.Pie(
#                 labels=list(data.keys()),
#                 values=list(data.values())
#             )],
#             'layout': go.Layout(title='Соотношение кластеров')
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)
