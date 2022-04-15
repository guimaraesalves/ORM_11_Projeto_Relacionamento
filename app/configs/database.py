from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.estado_model import EstadoModel
    from app.models.capital_model import CapitalModel
    # Declarando a nova model
    from app.models.regiao_model import RegiaoModel

# Declarando a model e a tabela pivo
    from app.models.bacia_hidro_model import BaciaHidroModel
    from app.models.bacia_estado_table import bacias_estados

