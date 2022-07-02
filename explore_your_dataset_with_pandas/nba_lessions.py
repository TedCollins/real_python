#script goes through the nba lessons section of working with pandas

#libraries
import pandas as pd
import requests

#pandas settings
pd.set_option('display.max.columns', None)
pd.set_option('display.precision', 2)

#load the data
download_url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv'
response = requests.get(download_url)
with open('nba_all_elo.csv', 'wb') as f:
    f.write(response.content)
nba = pd.read_csv('nba_all_elo.csv')

#exploratory data analysis
print(nba.head())
print(nba.info())
print(nba.describe())

