import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('exports.csv')

app.config['suppress_callback_exceptions'] = True

available_exports = df['Export'].unique()
available_states = df['State'].unique()

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_exports],
                value='Pork'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Log',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_exports],
                value='Beef'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Log',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ],  style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
}),

    html.Div([
        dcc.Graph(id='indicator-graphic',
        hoverData={'points': [{'customdata': 'total exports'}]}
            )
        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ], style={'display': 'inline-block', 'width': '49%'}),
    ])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type):

    return {
        'data': [dict(
            x=df[df['Export'] == xaxis_column_name]['Value'],
            y=df[df['Export'] == yaxis_column_name]['Value'],
            text=df[df['Export'] == yaxis_column_name]['State'],
            customdata=df[df['Export'] == yaxis_column_name]['State'],
            mode='markers',
            marker={
                'color': ['yellow', 'blue', 'green', 'red', 'orange', 'pink', 'yellow', 'blue', 'green', 'red', 'orange', 'pink', 'yellow', 'blue', 'green', 'red', 'orange', 'pink', 'yellow', 'blue', 'green', 'red', 'orange', 'pink', 'yellow', 'blue', 'green', 'red', 'orange', 'pink', 'yellow', 'blue', 'green', 'red', 'orange', 'pink', 'yellow', 'blue', 'green', 'red', 'orange', 'pink', 'yellow', 'blue', 'green', 'red', 'orange', 'pink'
                          'yellow', 'blue'],
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'blue'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_column_name,
                'type': 'log' if xaxis_type == 'Log' else 'linear'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'log' if yaxis_type == 'Log' else 'linear'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            height=450,
            hovermode='closest'
        )
    }


def create_time_series(dff, axis_type, title):
    return {
        'data': [
            { 'x': dff['Value'], 'y': dff['Value'], 'type': 'bar', 'name': 'Exports'},
        ],
        'layout': {
            'height': 200,
            'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
            'annotations': [{
                'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'yaxis': {'type': 'log' if axis_type == 'Log' else 'linear'},
            'xaxis': {'showgrid': False}
        }
    }


@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('indicator-graphic', 'hoverData'),
     dash.dependencies.Input('xaxis-column', 'value'),
     dash.dependencies.Input('xaxis-type', 'value')])
def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
    state_name = hoverData['points'][0]['customdata']
    dff = df[df['State'] == state_name]
    dff = dff[dff['Export'] == xaxis_column_name]
    title = '<b>{}</b><br>{}'.format(state_name, xaxis_column_name)
    return create_time_series(dff, axis_type, title)


@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('indicator-graphic', 'hoverData'),
     dash.dependencies.Input('yaxis-column', 'value'),
     dash.dependencies.Input('yaxis-type', 'value')])
def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
    dff = df[df['State'] == hoverData['points'][0]['customdata']]
    dff = dff[dff['Export'] == yaxis_column_name]
    return create_time_series(dff, axis_type, yaxis_column_name)


if __name__ == '__main__':
    app.run_server(debug=True)