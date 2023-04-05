import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

# resume sample template from https://zety.com/
layout = html.Div([
    dcc.Markdown('# Carlo Longo', style={'textAlign':'center'}),
    dcc.Markdown('Roma, Italy', style={'textAlign': 'center'}),
    dcc.Markdown('### Professional Summary', style={'textAlign': 'center'}),
    html.Hr(),
    dcc.Markdown('Proactive and result driven Risk Manager with more than 10 of experience in the Commodity Trading Industry. \n'
                 'I am forward-looking and strategic minded, with the ability to understand potential risks for the firm, both at departmental level as well as in a wider firm perspective.\n'
                 'Along my career I have developed important skills such as: Critical Thinking, Eye on details, Leadership and Communication.',
                 style={'textAlign': 'center', 'white-space': 'pre'}),

    dcc.Markdown('### Skills', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
            * Market Risk
            * Trading
            * Data Analysis
            * Data Visualization
            
            ''')
        ], width={"size": 3, "offset": 1}),
        dbc.Col([
            dcc.Markdown('''
            * Renewable Energy 
            * Hedging
            
            ''')
        ], width=3)
    ], justify='center'),

    dcc.Markdown('### Work History', style={'textAlign': 'center'}),
    html.Hr(),

#Esperienza in CRE

    dbc.Row([
        dbc.Col([
            dcc.Markdown('03/2019 to current', style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Risk Manager      \n'
                         'Consorzio per Risorse Energetiche - Cesena, Italy',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li('Written Market Risk Policy for a Portfolio of Gas and Electricity, with a Sale book of 70 Mio Smc and 1.1 TWh respectively. '),
                html.Li('Managed Market Risk for Prop Trading activity on EEX and ICE exchange'),
                html.Li('Update of Risk Limits and Key Risks Indicator. (VaR, PaR,Open Position,P&L) '),
                html.Li('Spread Risk Culture within the Company and Trained Local staff on Risk topics')
            ])
        ], width=5)
    ], justify='center'),

#Esperienza in Al Baraa

    dbc.Row([
        dbc.Col([
            dcc.Markdown('06/2018 to 03/2019',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Risk Manager \n'
                         'Al Baraa - Dubai, UAE',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Responsible for providing independent, timely, aligned, and accurate valuations of trading book positions. Book Exposure is about 1 Mio of Barrel per Month of Gasoil.'),
                html.Li(
                    'Generate, confirm, and report daily P&L. Explanation of the Variances trough a PnL Breakdown'),
                html.Li(
                    'Preparing and Leading the Risk Committee monthly, attended by Traders Managers and CFO of the Company. '),
                html.Li(
                    'Managed Exposure of €/USD for 32M USD. Discussed Best Strategy with Treasury Dpt. to Hedge Position with Future Contracts.')
            ])
        ], width=5)
    ],  justify='center'),

#Esperienza in Cefetra

    dbc.Row([
        dbc.Col([
            dcc.Markdown('06/2016 to 03/2018',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Risk Manager \n'
                         'Cefetra - Roma, Italy',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Managed the full Risk and Credit processes and reported to the local CFO and Global Chief Risk Officer.'),
                html.Li(
                    'Oversee the risks of a Portfolio of 1.2 Mio of MT Physicals sales (Soy, Beans, Grains), with major focus on Cash Risk, Futures Risk, Price Risk and Counterparty Risk.'),
                html.Li(
                    'Monitored any changes of MtM. Reviewed, set, and monitored VaR and Position Limits. Daily check and resolution of Equity/Margin changes to prevent Margin Calls.'),
                html.Li(
                    'Attended weekly meeting with CRO to review Books Exposure and discuss on company’s Risk Profile.')
            ])
        ], width=5)
    ], justify='center'),

#Esperienza in ENGIE

    dbc.Row([
        dbc.Col([
            dcc.Markdown('06/2008 to 05/2018',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Senior Risk Analyst \n'
                         'ENGIE - Roma, Italy',
                         style={'white-space': 'pre'},
                         className='ms-3'),
            html.Ul([
                html.Li(
                    'Supervising the Risk of Front Office desks (Mainly Power and Gas) through Risk Metrics (MtM, VaR,GrossMargin@Risk).'),
                html.Li(
                    'Maintaining and periodical review of the Book Structures and Risk Policy. '),
                html.Li(
                    'Monitor adherence to Risk limits and ensure that Products are in line with their mandates and agreed Risk Profiles.'),
                html.Li(
                    'Checking and Implementing Risk Indicator (Var, MtM, Gross Margin@Risk) in the RMS System (Risk Management System) for the Italian Portfolio')
            ])
        ], width=5)
    ], justify='center'),

    #EDUCATION


    dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('2013',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('Master Degree: Statistics\n'
                         '"La Sapeinza" - Università di Roma, Italy',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5)
    ], justify='center'),
])