from app.configs.database import db

class CapitalModel(db.Model):
    __tablename__ = 'capitais'

    # Atributos que representam colunas da nossa tabela capitais
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False, unique=True)
    bairros = db.Column(db.Integer)
    populacao = db.Column(db.Integer)
    # Chave Estrangeira para relacionamento com a tabela estados
    estado_id = db.Column(
      db.Integer,
      db.ForeignKey("estados.id"),
      nullable=False,
      unique=True
      )

    # Variável criada para auxiliar no desenvolvimento, não
    # faz parte da criação das tabelas no banco.
    estado = db.relationship(
      "EstadoModel",
      backref=db.backref("capital", uselist=False)
    )