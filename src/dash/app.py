import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import requests

app = dash.Dash(__name__, prevent_initial_callbacks=True)

server = app.server

app.layout = html.Div([
    html.H1("Dash Template"),
    html.Button('Test API', id='test-api', n_clicks=0),
    html.Div(id='container-api-result',
             children='')
])

@app.callback(
    dash.dependencies.Output('container-api-result', 'children'),
    [dash.dependencies.Input('test-api', 'n_clicks')])
def update_output(n_clicks):
    greeting = requests.get("http://127.0.0.1:80/test/HelloWorld")
    return html.H2(greeting)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')