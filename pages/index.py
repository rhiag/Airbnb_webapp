# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Welcome to San Fransisco!

            Enjoy some of the best weather , diverse cuisines , great shopping districts and attractions such as antique cable cars, the Golden Gate bridge, Fisherman’s Wharf and Pier 39, wine country, Alcatraz, Muir Woods’ 1000 year-old redwood forest and so much more!
            
            This app helps you find a place to stay that fits in your budget.          

            
            """
        ),
        dcc.Link(dbc.Button('Next', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        #dcc.Graph(figure=fig),
        html.Div(html.Img(src=app.get_asset_url('download.jpeg')), style={'height':'10%', 'width':'10%'})
    ]
)

layout = dbc.Row([column1, column2])