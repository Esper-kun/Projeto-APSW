from config import banco

class Usuario(banco.Model):
    __tablename__ = 'usuarios'
    id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String(256))
    email = banco.Column(banco.String(128), unique=True)

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return 'Usuário' + self.nome + ' | ' + self.email