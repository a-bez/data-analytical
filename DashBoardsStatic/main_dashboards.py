import pandas as pd
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import json

# завантаження даних
with open('D:\python_projects\Dash\data\my_series.json', 'r') as f:
    my_ser = json.load(f)

series_df = pd.DataFrame(my_ser)
series_df.reset_index(inplace=True)
series_df.columns = ['cluster', 'count']

with open('D:\python_projects\Dash\data\joind_keywords.json', 'r') as f:
    key_words = json.load(f)
merged_data = {**my_ser, **key_words}

gisto = pd.DataFrame(merged_data)
gisto.reset_index(inplace=True)
gisto.columns = ['cluster', 'nums', 'key_words']

with open('D:\python_projects\Dash\data\main_data.json', 'r') as f:
    main_data = json.load(f)

mainData_df = pd.DataFrame(main_data)

with open('D:\python_projects\Dash\data\processed_sentiment_df.json', 'r') as f:
    data = json.load(f)
sentiment_df = pd.DataFrame(data)


# утворення екземпляру Dash
app = dash.Dash()

# утворення фігури кругової діагрыми
fig = go.Figure(
    data=[go.Pie(labels=series_df['cluster'], values=series_df['count'])],
    layout=go.Layout(title='Кругова діаграма відображає співвідношення кластерів у відсотковому відношенні')
)

# утворення фігури гістограми
fig_gisto = go.Figure(
    data=[go.Bar(x=gisto['cluster'], y=gisto['nums'],
                 hovertext=gisto['key_words'])],
    layout=go.Layout(title='Количество документов в каждом кластере', xaxis=dict(
        title='Кластер'), yaxis=dict(title='Количество документов'))
)

# утворення фігури діаграми розсіювання на базі сантімент-аналіза
fig_sentiment = px.scatter(sentiment_df, x='cluster', y='sentiment_score')

# утворення розмітки
app.layout = html.Div([
    html.H1('Відображання дашбордів сформованих у модулі обробки вхідних даних'),

    html.Div([
        html.Div([
            html.H3('Кругова діаграма кластерів'),
            dcc.Graph(figure=fig)
        ], className='four columns'),

        html.Div([
            html.H3('Гістограма кластерів та кількості їх наповнення'),
            dcc.Graph(figure=fig_gisto)
        ], className='four columns'),

        html.Div([
            html.H3('Діаграма розсіювання кластерів та даних'),
            dcc.Graph(
                id='scatter-plot',
                figure={
                    'data': [
                        # утворення фігури діаграми розсіювання
                        go.Scatter(
                            x=mainData_df[mainData_df['cluster']
                                          == i]['cluster'],
                            y=mainData_df[mainData_df['cluster']
                                          == i]['processed_text'],
                            mode='markers',
                            opacity=0.7,
                            marker={
                                'size': 15,
                                'line': {'width': 0.5, 'color': 'white'}
                            },
                            name='Cluster {}'.format(i)
                        ) for i in mainData_df['cluster'].unique()
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'clusters'},
                        yaxis={'title': 'processed_text'},
                        hovermode='closest'
                    )
                }
            )
        ], className='four columns'),

        html.Div([
            html.H3('Діаграма розсіюваня вмісту кластерів засновуючись на аналізі тональності'),
            dcc.Graph(
                id='sentiment-plot',
                figure=fig_sentiment
            )
        ])
    ])
])

# метод запуску застосунку
if __name__ == '__main__':
    app.run_server(debug=True)
