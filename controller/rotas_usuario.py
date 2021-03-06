from flask import render_template, request, Blueprint
from config import banco
from model.usuario import Usuario

TEMPLATES = './view'
STATIC = './static'

usuario_blueprint = Blueprint('usuarios', __name__, static_url_path='', template_folder=TEMPLATES, static_folder=STATIC)

@usuario_blueprint.route('/paginaLogin')
def login():
  return render_template('login.html')

@usuario_blueprint.route('/paginaCadastro')
def cadastro():
    return render_template('cadastrarUsuario.html')

@usuario_blueprint.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    nome = request.form.get('nome')
    email = request.form.get('email')

    usuario=Usuario(nome, email)
    banco.session.add(usuario)
    banco.session.commit()
    return render_template('usuarioCadastradoOK.html')

@usuario_blueprint.route('/consultarUsuarios')
def consultarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('listarUsuarios.html', usuarios=usuarios)
@usuario_blueprint.route('/editarUsuarios')
def removerUsuarios():
    return render_template('editarUsuarios.html')