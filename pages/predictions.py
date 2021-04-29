# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
import pandas as pd
pipeline = load('./notebooks/model.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

neighbourhood_list = ['Mission', 'South of Market', 'Bernal Heights', 'Nob Hill', 'Potrero Hill', 'Crocker Amazon', 'Bayview', 'Castro/Upper Market', 'Pacific Heights', 'Excelsior', 'Haight Ashbury', 'Downtown/Civic Center', 'Noe Valley', 'Outer Sunset', 'Western Addition', 'Parkside', 'Chinatown', 'North Beach', 'Twin Peaks', 'Financial District', 'Marina', 'Inner Sunset', 'Glen Park', 'Outer Mission', 'West of Twin Peaks', 'Inner Richmond', 'Ocean View', 'Seacliff', 'Russian Hill', 'Lakeshore', 'Presidio Heights', 'Outer Richmond', 'Golden Gate Park', 'Presidio', 'Visitacion Valley', 'Diamond Heights']

room_type_list = ['Private room', 'Shared room', 'Entire home/apt', 'Hotel room']


column1 = dbc.Col(
    [
      
     dcc.Markdown(
            """
        
            ## Budget for Stay
            
            """

        ), 

    ],
    

    md=4,

    
)


column2 = dbc.Col(
    [

     dcc.Markdown(
        """
        #### Neighbourhood
        """),

     dcc.Dropdown(
        id='neighbourhood-dropdown',
        options=[
        {'label': i, 'value': i} for i in neighbourhood_list
       ],
        value='Golden Gate Park',
        className='mb-4'
    ),  

     dcc.Markdown(
        """
        #### No. of Guests
        """),
     dcc.Slider(
        id='accommodates-slider',
        min=0,
        max=20,
        step=1,
        value=2,
     ),
     dcc.Markdown('', id='slider-accommodates-container'),


    dcc.Markdown("""
     #### Room Type
     """),

     dcc.Dropdown(
        id='roomtype-dropdown',
        options=[
            {'label': i, 'value': i} for i in room_type_list
           
        ],
        value='Private room',
        className='mb-4'
    ), 


     dcc.Markdown(
        """
        #### Duration of Stay
        """),
     dcc.Slider(
        id='nights-slider',
        min=1,
        max=31,
        step=1,
        marks={
        1: '1',
        5: '5',
        10: '10',
        20: '20',
        30: '30'        
    },
        value=2,
     ),
     dcc.Markdown('', id='slider-nights-container'),
    

    dcc.Markdown(
        """
        #### Bedrooms
        """),
     dcc.Slider(
        id='bedrooms-slider',
        min=1,
        max=10,
        step=1,
        marks={
        1: '1',
        5: '5',
        10: '10'
               
    },
        value=2,
     ),
     dcc.Markdown('', id='slider-beds-container'),


     dcc.Markdown(
        """
        #### Bathrooms
        """),
     dcc.Slider(
        id='bath-slider',
        min=1,
        max=10,
        step=0.5,
        marks={
        1: '1',
        5: '5',
        10: '10'
               
    },
        value=2,
     ),
     dcc.Markdown('', id='slider-bath-container'),


    dcc.Markdown('',id='prediction-content', style={
        'textAlign':'center',
        'font-size':30})
        

    ]
    
)


@app.callback(
    dash.dependencies.Output('slider-accommodates-container', 'children'),
    [dash.dependencies.Input('accommodates-slider', 'value')])
def update_output(value):
    return 'You have selected "{}" guests'.format(value)

@app.callback(
    dash.dependencies.Output('slider-nights-container', 'children'),
    [dash.dependencies.Input('nights-slider', 'value')])
def update_output(value):
    return 'You have selected "{}" nights'.format(value)

@app.callback(
    dash.dependencies.Output('slider-beds-container', 'children'),
    [dash.dependencies.Input('bedrooms-slider', 'value')])
def update_output(value):
    return 'You have selected "{}" bedrooms'.format(value)

@app.callback(
    dash.dependencies.Output('slider-bath-container', 'children'),
    [dash.dependencies.Input('bath-slider', 'value')])
def update_output(value):
    return 'You have selected "{}" baths'.format(value)


@app.callback(
    Output('prediction-content','children'),
    [ Input('neighbourhood-dropdown', 'value'),
      Input('accommodates-slider', 'value'),
      Input('roomtype-dropdown', 'value'),
      Input('nights-slider', 'value'),
      Input('bedrooms-slider', 'value'),
      Input('bath-slider', 'value')
     ])

def predict(neighbourhood,accommodates,room_type,min_nights,bedrooms,baths):
    df = pd.DataFrame(columns=['neighbourhood_cleansed','accommodates','room_type','minimum_nights','bedrooms','bathrooms'], 
    data=[[neighbourhood,accommodates,room_type,min_nights,bedrooms,baths]])
    y_pred = pipeline.predict(df)[0]
    return "Predicted Price  is ${}.".format(round(y_pred,2))





layout = dbc.Row([column2])
