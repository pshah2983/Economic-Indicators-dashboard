import pandas as pd
import wbgapi as wb
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

def get_country_list():
    """Get list of all available countries from World Bank API"""
    countries = {}
    for country in wb.economy.list():
        country_id = country['id']
        if len(country_id) == 3 and country_id not in ['INX', 'XKX']:
            countries[country_id] = country['value']
    return countries

def create_visualization(selected_countries):
    if not selected_countries:
        return go.Figure()
        
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    indicators = {
        'NY.GDP.MKTP.CD': 'GDP (current US$)',
        'FP.CPI.TOTL.ZG': 'Inflation Rate (%)',
        'SL.UEM.TOTL.ZS': 'Unemployment Rate (%)'
    }
    
    all_data = {}
    for indicator_code, indicator_name in indicators.items():
        df = wb.data.DataFrame(indicator_code, selected_countries, mrv=20)
        all_data[indicator_code] = df
    
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
    
    for i, (indicator_code, indicator_name) in enumerate(indicators.items()):
        df = all_data[indicator_code]
        years = [year[2:] for year in df.columns]
        
        for j, country in enumerate(df.index):
            values = df.loc[country].values
            color = colors[j % len(colors)]
            
            fig.add_trace(
                go.Scatter(
                    x=years,
                    y=values,
                    name=f"{country} - {indicator_name}",
                    mode='lines+markers',
                    visible=(i == 0),
                    line=dict(color=color, width=2),
                    marker=dict(size=8)
                )
            )
    
    fig.update_layout(
        title={
            'text': 'Economic Indicators Dashboard',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_title="Year",
        yaxis_title="Value",
        hovermode='x unified',
        template='plotly_white',
        height=600,
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        updatemenus=[{
            'buttons': [
                dict(
                    args=[{"visible": [j//len(df.index) == i for j in range(len(df.index)*len(indicators))]}],
                    label=name,
                    method="update"
                ) for i, (_, name) in enumerate(indicators.items())
            ],
            'direction': 'down',
            'showactive': True,
            'x': 0.1,
            'y': 1.15,
            'xanchor': 'left',
            'yanchor': 'top'
        }]
    )
    
    return fig

def main():
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    countries = get_country_list()
    country_options = [{'label': name, 'value': code} for code, name in sorted(countries.items(), key=lambda x: x[1])]
    
    app.layout = html.Div([
        # Header
        html.H1("Economic Indicators Dashboard", 
                style={'textAlign': 'center', 'margin': '20px 0'}),
        
        # Main content
        html.Div([
            # Left panel with controls
            html.Div([
                html.H3("Select Countries"),
                dcc.Dropdown(
                    id='country-selector',
                    options=country_options,
                    value=['USA', 'CHN', 'IND'],
                    multi=True,
                    placeholder="Select countries to compare..."
                ),
                html.Button('Update Dashboard', 
                           id='update-button', 
                           n_clicks=0,
                           style={
                               'marginTop': '20px',
                               'padding': '10px',
                               'width': '100%',
                               'backgroundColor': '#007bff',
                               'color': 'white',
                               'border': 'none',
                               'borderRadius': '5px'
                           })
            ], style={
                'width': '300px',
                'padding': '20px',
                'backgroundColor': '#f8f9fa',
                'borderRadius': '10px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
            }),
            
            # Right panel with graph
            html.Div([
                dcc.Loading(
                    id="loading",
                    type="default",
                    children=[dcc.Graph(id='main-graph')]
                )
            ], style={
                'flex': '1',
                'marginLeft': '20px',
                'padding': '20px',
                'backgroundColor': '#f8f9fa',
                'borderRadius': '10px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
            })
        ], style={
            'display': 'flex',
            'margin': '20px',
            'gap': '20px'
        })
    ])
    
    @app.callback(
        Output('main-graph', 'figure'),
        Input('update-button', 'n_clicks'),
        State('country-selector', 'value')
    )
    def update_graph(n_clicks, selected_countries):
        if not selected_countries:
            return go.Figure()
        return create_visualization(selected_countries)
    
    app.run(debug=True)

if __name__ == '__main__':
    main() 