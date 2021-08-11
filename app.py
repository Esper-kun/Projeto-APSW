from usuario import Usuario
from flask import Flask, render_template
from config import banco
import datetime

TEMPLATES = './view'
STATIC = './static'

app = Flask(__name__, static_url_path='', template_folder=TEMPLATES, static_folder=STATIC)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'
banco.init_app(app)

with app.app_context():
    banco.create_all()

@app.route('/')
def helloWorld():
    return render_template('welcome.html')

@app.route('/home')
def home():
    data = datetime.datetime.now()
    usuarios = ['Flávio', 'Isabella', 'João', 'Maria']
    mostrarUsuarios = True
    return render_template('home.html', dataAtual=data, usuarios=usuarios, mostrarUsuarios=mostrarUsuarios)

@app.route('/cadastrarUsuario')
def cadastrarUsuario():
    usuario=Usuario("Flávio", "flavio@gmail.com")
    banco.session.add(usuario)
    banco.session.commit()
    return 'Usuário cadastrado com sucesso!'

app.run(host='0.0.0.0', port=5000)