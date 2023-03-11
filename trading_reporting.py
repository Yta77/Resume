from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


data = pd.read_excel("C:\\Users\\Workstation2\\Desktop\\Dash Input\\Statement3.xlsx")

df = data#.groupby(['Commodity'], as_index=False)

# Step 2: Creo App

app = Dash(__name__, external_stylesheets=[dbc.themes.YETI, dbc.icons.BOOTSTRAP])

# Step 3: Definisco Dropdown

selezione_trader=dcc.Dropdown(id='tr', #value=['John Smith', 'Kris Taylor'],
               multi=True,
               options=[{'label': x, 'value': x} for x in df['Activity'].unique()])

# Creo Dropdown 1
# Creo Dropdown 1
comm_dropdown = dcc.Dropdown(
   id='commodity-dropdown',
   options=[{'label': x, 'value': x} for x in data['Commodity'].unique()],
   value='NASDAQ',
   style={'width': '60%'}
)


# Creo Dropdown 2
comm2_dropdown = dcc.Dropdown(
   id='commodity-dropdown2',
   options=[{'label': x, 'value': x} for x in data['Commodity'].unique()],
   value='NASDAQ', style={'width': '60%'}
)


barchart = px.bar(


  data_frame=df[:30],
   x="date",
   y="total_volume",
   color="total_volume",
   opacity=0.9,
   orientation="v",
   barmode='overlay',
   title='Long or Short',
   width=1400,
   height=720,
   #facet_row='Activity',
   template='gridon')



PnLGraph = dcc.Graph(id='TP&L')
PnLGraph2 = dcc.Graph(id='TP&L2')
DDGraph = dcc.Graph (id='DD')
VaRGraph = dcc.Graph(id='VaR')
Book = dcc.RadioItems(
   options=data['Activity'].unique(),
   id='book-radio',
   value='ETFs',
   labelStyle={'display': 'inline-block', 'margin-right': '40px'}
)


# nav bar
navbar = dbc.NavbarSimple(


   brand="Trading Book",
   brand_href="#",
   color="primary",
   fluid=True,
   dark=True
)


# Step 6: Defizione dell app:


app.layout = html.Div(


   dbc.Col(
       [
           (dbc.Row(navbar)),
           html.Br(),
           html.P("Trader Selection"),
           dbc.Col(html.Div(selezione_trader)),
           html.Br(),
           html.Br(),


           dbc.Row(
               [
                   dbc.Col(html.Div(comm_dropdown)),
                   dbc.Col(html.Div(comm2_dropdown))
               ]
           ),




           dbc.Row(
               [
                   dbc.Col(html.Div(PnLGraph), width=4),
                   dbc.Col(html.Div(PnLGraph2), width=4),
                   dbc.Col(html.Div(VaRGraph), width=4)
               ]
           ),
           dcc.Graph(
               id='example-graph',
               figure=barchart
           )
       ]
   )
)



#CALL BACK


@app.callback(
   [Output("TP&L", "figure"), Output("VaR", "figure"),Output("TP&L2", "figure")],
   [Input(comm_dropdown, "value"), Input(comm2_dropdown, "value"), Input(selezione_trader,"value")])




# Definizioni delle Funzioni


def update_graph(selected_commodity,selected_commodity2,selected_activity):


   filtered_avocado = data[(data['Commodity'] == selected_commodity)]



   line_fig = px.histogram(filtered_avocado,
                      x='date', y='PnL',
                      title=f' PnL in {selected_commodity}')


   line_fig2 = px.area(filtered_avocado,
                      x='date', y='VaR',
                      title=f' VaR in {selected_commodity2}')


   line_fig3 = px.area(filtered_avocado,
                       x='date', y='variation_margin',
                       title=f' variation_margin in {selected_activity}')


   return line_fig,line_fig2,line_fig3


# Step 5: Running the dashboard


if __name__ == '__main__':
   app.run_server(debug=True)
