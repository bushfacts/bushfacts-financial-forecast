import os

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

server = app.server

app.layout = html.Div([
                dcc.Tabs(id='navigation', value='forecast', children=[
                    dcc.Tab(label='Expenses', value='expenses', children=[
                        html.H6('enter new expenses'),
                        html.H6('see all expenses'),
                        html.H6('summary of expenses'),
                        html.H6('chart of expenses')
                    ]),
                    dcc.Tab(label='Income', value='income', children=[
                        html.H6('enter new income'),
                        html.H6('see all income'),
                        html.H6('summary of income'),
                        html.H6('chart of income')
                    ]),
                    dcc.Tab(label='Summary', value='summary', children=[
                        html.H6('combined')
                    ]),
                    dcc.Tab(label='Forecast', value='forecast', children=[
                        html.H6('table of day by day money change?'),
                        html.H6('graph with changeable/zoomable range'),
                        html.H6('enter bottom threshold and highlight those values in red on graph/display in table'),
                        html.H6('enter upper threshold and highlight those values in green on graph/display in table')
                    ])
                ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
