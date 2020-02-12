#author: João Victor de Mesquita
#based on: https://sigmoidal.ai/como-analisar-acoes-da-bolsa-com-python/?utm_campaign=inscritos_-_vagas_remanescentes&utm_medium=email&utm_source=RD+Station 
import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go

df = pd.DataFrame() #creating an empty dataframe

acao = 'ITUB3.SA' #choosing a share
df = web.DataReader(acao, data_source='yahoo', start='01-01-2000') #importing data from Yahoo

#generating the candlestick graph to analyze the shares throughout the years since 2000
trace1 = {
    'x' : df.index,
    'open': df.Open,
    'close': df.Close,
    'high' : df.High,
    'low' :  df.Low,
    'type' : 'candlestick',
    'name' : acao,
    'showlegend' : False
}

data = [trace1]
layout = go.Layout()

fig = go.Figure(data=data, layout=layout)
fig.show()