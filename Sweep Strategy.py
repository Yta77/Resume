import pandas as pd
import plotly.graph_objs as go
import dash
from dash import dcc
from dash import html
import yfinance as yf
from dash import Dash, html, dcc, dash_table

# Load data
data = yf.Ticker("EURUSD=X").history(period='5d', interval='60m').reset_index()
n = len(data)

def is_swing_high(group):
    return group[1] > max(group[0], group[2])

data['Swing High'] = 0
data['Swing High'] = data['High'].rolling(3, center=True).apply(is_swing_high, raw=True)


def is_swing_low(group):
    return group[1] < min(group[0], group[2])


data['Swing Low'] = 0
data['Swing Low'] = data['Low'].rolling(3, center=True).apply(is_swing_low, raw=True)

# Sweep calculation
threshold_swing_high = 0.0
threshold_swing_low = 999999999.9
bullish_sweep = [False] * n
bearish_sweep = [False] * n

for i in range(1, n - 1):
    # Bearish Sweep
    if data['High'][i] > threshold_swing_high:
        threshold_swing_high = data['High'][i]
    if data['High'][i] >= data['High'][i + 1] and threshold_swing_high >= data['High'][i]:
        if data['High'][i - 1] < data['High'][i] and data['High'][i] > data['High'][i + 1] and data['Close'][i] <= \
                data['High'][i] and data['Open'][i] < data['High'][i]:
            bearish_sweep[i] = True

    # Bullish Sweep
    if data['Low'][i] < threshold_swing_low:
        threshold_swing_low = data['Low'][i]
    if data['Low'][i] <= data['Low'][i + 1] and threshold_swing_low <= data['Low'][i]:
        if data['Low'][i - 1] > data['Low'][i] and data['Low'][i] < data['Low'][i + 1] and data['Close'][i] >= \
                data['Low'][i] and data['Open'][i] > data['Low'][i]:
            bullish_sweep[i] = True


# Add bullish_sweep and bearish_sweep columns to data DataFrame
data['bullish_sweep'] = bullish_sweep
data['bearish_sweep'] = bearish_sweep

# Plot
bullish_sweep_indices = [i for i, x in enumerate(bullish_sweep) if x]
bearish_sweep_indices = [i for i, x in enumerate(bearish_sweep) if x]

fig = go.Figure(data=[go.Candlestick(x=data['Datetime'],
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'],
                                     name='Candlestick'),
                      go.Scatter(x=data.iloc[bullish_sweep_indices]['Datetime'],
                                 y=data.iloc[bullish_sweep_indices]['Close'],
                                 mode='markers',
                                 marker=dict(color='green', size=10),
                                 name='Bullish Sweep',
                                 hovertemplate='Bullish Sweep'),
                      go.Scatter(x=data.iloc[bearish_sweep_indices]['Datetime'],
                                 y=data.iloc[bearish_sweep_indices]['Close'],
                                 mode='markers',
                                 marker=dict(color='red', size=10),
                                 name='Bearish Sweep',
                                 hovertemplate='Bearish Sweep')
                      ])

fig.update_layout(xaxis_rangeslider_visible=False, title='Sweep Indicator')

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='stock-data',
        data=data.tail(1000).to_dict('records'),
        columns=[{'name': col, 'id': col} for col
                 in data.columns if
                 col not in ['Dividends', 'Volume', 'Stock Splits']]
    ),

    dcc.Graph(
        id='sweep',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
