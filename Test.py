from dash import Dash, html, dash,dcc
import plotly.subplots as sp
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objs as go


app = dash.Dash()

# Use yfinance to grab EUR/USD data from Yahoo Finance
eur_usd = yf.download("EURUSD=X", start="2020-01-01", end="2022-12-31")
eur_usd['Swing High'] = 0
eur_usd.loc[(eur_usd['High'].shift(1) < eur_usd['High']) & (eur_usd['High'].shift(-1) < eur_usd['High']), 'Swing High'] = eur_usd['High']


# Create the candlestick plot
trace = go.Candlestick(x=eur_usd.index,
                       open=eur_usd['Open'],
                       high=eur_usd['High'],
                       low=eur_usd['Low'],
                       close=eur_usd['Close'])

candlestick = go.Candlestick(x=eur_usd.index,
                       open=eur_usd['Open'],
                       high=eur_usd['High'],
                       low=eur_usd['Low'],
                       close=eur_usd['Close'])



scatter = go.Scatter(x=eur_usd.index, y=eur_usd['Swing High'], mode='markers', marker=dict(size=10, color="red"))
data = [candlestick, scatter]

layout = go.Layout(title="EUR/USD", xaxis=dict(title="Date"), yaxis=dict(title="EUR/USD",range=[1.10, 1.20]))
fig = sp.make_subplots(rows=1, cols=1)

fig.add_trace(go.Candlestick(x=eur_usd.index,
                             open=eur_usd['Open'],
                             high=eur_usd['High'],
                             low=eur_usd['Low'],
                             close=eur_usd['Close'],
                             increasing_line_color= 'green',
                             decreasing_line_color= 'red'))

fig.update_layout(title="EUR/USD", xaxis=dict(title="Date"), yaxis=dict(title="EUR/USD",range=[1.10, 1.20]))



# Include the plot in the Dash layout
app.layout = html.Div([
    dcc.Graph(
        id='eur-usd-plot',
        figure=fig,
        style={'height': '800px', 'width': '200%'}
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)