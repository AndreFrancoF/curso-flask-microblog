from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    nome = 'André Franco'
    dados = {'nome':'Marcos André Franco', 'profissao':'Dev'}
    return render_template('index.html', dados=dados)

@app.route('/contatos')
@app.route('/contato')
def contatos():
    return render_template('contatos.html')