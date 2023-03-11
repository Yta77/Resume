from dash import Dash, html, dcc, dash_table, Input, Output
import plotly.graph_objects as go
import yfinance as yf
import pandas as pd
from dash.dependencies import Input, Output
import dash_extensions as de
from dash.exceptions import PreventUpdate
from flask import send_file
import plotly.graph_objects as go
import numpy as np

app = Dash()
import yfinance as yf

price = yf.Ticker("EURUSD=X").history(period='5d', interval='60m').reset_index()
price['Numero_Candela'] = price.index


# S W I N G     H I G H

def is_swing_high(group):
    return group[1] > max(group[0], group[2])


price['Swing High'] = 0
price['Swing High'] = price['High'].rolling(3, center=True).apply(is_swing_high, raw=True)


# S W I N G     L O W

def is_swing_low(group):
    return group[1] < min(group[0], group[2])


price['Swing Low'] = 0
price['Swing Low'] = price['Low'].rolling(3, center=True).apply(is_swing_low, raw=True)


# S W E E P S




# Creazione di un oggetto Candlestick

candlestick = go.Candlestick(x=price['Numero_Candela'],
                              open=price['Open'],
                              high=price['High'],
                              low=price['Low'],
                              close=price['Close'],
                              increasing=dict(line=dict(color='#0000ff')),
                              decreasing=dict(line=dict(color='#5A5A5A'))
                             )

# Creazione di un oggetto Scatter per gli swing high

swing_high = go.Scatter(x=price[price['Swing High'] == True]['Numero_Candela'],
                        y=price[price['Swing High'] == True]['High'],
                        mode='markers',
                        name='Swing High',
                        marker=dict(color='red', size=10)
                       )

# Creazione di un oggetto Scatter per gli swing low

swing_low = go.Scatter(x=price[price['Swing Low'] == True]['Numero_Candela'],
                       y=price[price['Swing Low'] == True]['Low'],
                       mode='markers',
                       name='Swing Low',
                       marker=dict(color='blue', size=10),

                      )

# Creazione del layout del grafico

layout = go.Layout(title='Grafico a Candele Giapponesi con Swing Low e Swing High',xaxis_rangeslider_visible=False)

# Creazione della figura
fig = go.Figure(data=[candlestick, swing_high, swing_low], layout=layout)

fig.update_layout(height=600)



#DEFINIZIONE DEL LAYOUT

app.layout = html.Div([
    html.H1('H1 Sweep EURUSD Strategy'),
   # dcc.Download(id="download"),
    dash_table.DataTable(
        id='stock-data',
        data=price.tail(1000).to_dict('records'),
        columns=[{'name': col, 'id': col} for col in price.columns if
                 col not in ['Dividends', 'Volume', 'Stock Splits']]
    ),
    dcc.Graph(
        id='candlestick-chart',
        figure=fig  # passa la figura creata in precedenza
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)

