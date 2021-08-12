from flask import Flask, render_template, request
from config import banco
from model.usuario import Usuario
from controller.rotas_usuario import usuario_blueprint

TEMPLATES = './view'
STATIC = './static'

app = Flask(__name__, static_url_path='', template_folder=TEMPLATES, static_folder=STATIC)
app.register_blueprint(usuario_blueprint)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'
banco.init_app(app)

with app.app_context():
    banco.create_all()

@app.route('/')
def helloWorld():
    return render_template('welcome.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('index.html')

app.run(host='0.0.0.0', port=5000)