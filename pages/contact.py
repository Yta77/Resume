import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

green_text = {'color':'green'}

def layout():
    return dbc.Row([
        dbc.Col([
    dcc.Markdown('# Carlo Longo', className='mt-3'),
    dcc.Markdown('### Risk Manager', className='mb-5'),
    dcc.Markdown('### Personal info', style={'color':'gray'}),
    dcc.Markdown('Address', style=green_text),
    dcc.Markdown('Roma, Italy 00179'),
    dcc.Markdown('Phone Number', style=green_text),
    dcc.Markdown('+39-389-66-27583'),
    dcc.Markdown('Email', style=green_text),
    dcc.Markdown('longocarlo77@gmail.com'),
    dcc.Markdown('Linkedin', style=green_text),
    dcc.Markdown('[www.linkedin.com/in/carlo-l-929029a/](https://www.linkedin.com/in/carlo-l-929029a/)', link_target='_blank'),
    #dcc.Markdown('YouTube', style=green_text),
   #dcc.Markdown('[www.youtube.com/charmingdata](https://www.youtube.com/charmingdata)', link_target='_blank'),
        ], width={'size':6, 'offset':2})
], justify='center')