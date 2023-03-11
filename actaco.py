from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dash_table

# Step 1: data source

data = pd.read_excel("C:\\Users\\Workstation2\\Desktop\\Dash Input\\Statement3.xlsx")
df = data

# Step 2: Creo App

app = Dash(__name__, external_stylesheets=[dbc.themes.YETI, dbc.icons.BOOTSTRAP])

# Step 3: Definisco variabili

# Creo Dropdown 1
comm_dropdown = dcc.Dropdown(id='commodity-dropdown',
                             options=data['Commodity'].unique(),
                             value='NASDAQ',
                             style={
                                 'width': '30%'
                             }
                             )

# Creo Dropdown 2

comm2_dropdown = dcc.Dropdown(id='commodity-dropdown2',
                              options=data['Commodity'].unique(),
                              value='NASDAQ',
                              style={
                                  'width': '30%'
                              }
                              )



PnLGraph = dcc.Graph(id='TP&L')
VaRGraph = dcc.Graph(id='VaR')
Book = dcc.RadioItems(
    options=data['Activity'].unique(),
    value='running',
    labelStyle={'display': 'inline-block', 'margin-right': '10px'}
)
card = dbc.Card(
   dbc.CardBody(
         [
             html.H1("P&L"),
             html.H3("$104.2M", className="text-success")
         ],
     ),
     className="text-center"
 )

card1 = dbc.Card(
   dbc.CardBody(
         [
             html.H1("Equity"),
             html.H3("$14.2M", className="text-success")
         ],
     ),
     className="text-center"
 )

card2 = dbc.Card(
   dbc.CardBody(
         [
             html.H1("Capital Used"),
             html.H3("$324.2M", className="text-success")
         ],
     ),
     className="text-center"
 )

card3 = dbc.Card(
   dbc.CardBody(
         [
             html.H1("VaR"),
             html.H3("$3.2M", className="text-success")
         ],
     ),
     className="text-center"
 )

#Cards unite

cards = dbc.Row([
    dbc.Col(card, width=3),
    dbc.Col(card1, width=3),
    dbc.Col(card2, width=3),
    dbc.Col(card3, width=3)
])

# nav bar
navbar = dbc.NavbarSimple(

    brand="Trading Book",
    brand_href="#",
    color="primary",
    fluid=True,
    dark=True
)

# Step 6: Defizione dell app:

app.layout = html.Div([
    (html.H1(navbar),
    html.Br(),
   html.Div(children=[
        html.Div(className='container', children=[
            cards,
            html.Br(),
            Book,
            html.Br(),
            comm_dropdown,
            PnLGraph,
            comm2_dropdown,
            VaRGraph,
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records')
            )
        ])
    ]))
])


@app.callback(
    [Output("TP&L","figure"),Output("VaR","figure")],
    [Input(comm_dropdown,"value"),
     Input(comm2_dropdown,"value")]

)

# Definizioni delle Funzioni

def update_graph(selected_commodity,selected_commodity2,):

    filtered_avocado = data[data['Commodity'] == selected_commodity]
    line_fig = px.line(filtered_avocado,
                       x='date', y='PnL',
                       title=f' PnL in {selected_commodity}')

    line_fig2 = px.area(filtered_avocado,
                       x='date', y='VaR',
                       title=f' VaR in {selected_commodity2}')

    return line_fig,line_fig2


# Step 5: Running the dashboard
if __name__ == '__main__':
    app.run_server(debug=True)

    