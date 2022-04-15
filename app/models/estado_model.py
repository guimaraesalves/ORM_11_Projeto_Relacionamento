from app.configs.database import db

class EstadoModel(db.Model):
    __tablename__ = 'estados'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    sigla = db.Column(db.String(2), nullable=False, unique=True)
    populacao = db.Column(db.Integer)
    area = db.Column(db.Float)

    # Definição da relação com a tabela regioes
    regiao_id = db.Column(
      db.Integer, 
      db.ForeignKey('regioes.id')
    )
