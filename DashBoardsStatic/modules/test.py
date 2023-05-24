import pandas as pd
import json

with open('D:\python_projects\Dash\data\my_series.json', 'r') as f:
    my_ser = json.load(f)
with open('D:\python_projects\Dash\data\joind_keywords.json', 'r') as f:
    key_words = json.load(f)
merged_data = {**my_ser, **key_words}
gisto = pd.DataFrame(merged_data)
gisto.reset_index(inplace=True)
gisto.columns = ['cluster', 'nums', 'key_words']


series_df = pd.DataFrame(my_ser)
series_df.reset_index(inplace=True)
series_df.columns = ['cluster', 'count']

print(gisto)