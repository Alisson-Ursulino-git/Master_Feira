from flask import Flask
import dash
from dash import html
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import random

acturary = 'actuary.jpg'
plane    = 'plane.jpg'
accident = 'accident.jpg'
bank     = 'bank.jpg'
car      = 'car.jpg'
hacker   = 'hacker.jpg'


app = Flask(__name__)
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/')
server = dash_app.server

imagens = [
    {'url': plane, 'probabilidade': 0.1},
    {'url': accident, 'probabilidade': 0.8},
    {'url': bank, 'probabilidade': 0.3},
    {'url': car, 'probabilidade': 0.6},
    {'url': hacker, 'probabilidade': 0.2}
]

def selecionar_imagem():
    urls = [imagem['url'] for imagem in imagens]
    probabilidades = [imagem['probabilidade'] for imagem in imagens]
    indice = random.choices(range(len(imagens)), probabilidades)[0]
    print(indice)
    return urls[indice]

dash_app.layout = html.Div([
    html.Button('Exibir imagem aleatória', id='botao'),
    html.Img(id='imagem')
    #src=dash_app.get_asset_url('accident.jpg'),
])

@dash_app.callback(
    Output('imagem', 'src'),
    Input('botao', 'n_clicks')
)
def exibir_imagem(n_clicks):
    if n_clicks:
        url = selecionar_imagem()
        print(url)
        return dash_app.get_asset_url(url)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
