from flask import Flask

def init_app(app: Flask) -> None:
  from .estado_blueprint import bp as bp_estados
  app.register_blueprint(bp_estados)

  # Registrando a blueprint de capitais
  from .capital_blueprint import bp as bp_capitais
  app.register_blueprint(bp_capitais)

 # Registrando a blueprint de regioes
  from .regiao_blueprint import bp as bp_regioes
  app.register_blueprint(bp_regioes)

  # Registrando a blueprint de bacias
  from .bacia_hidro_blueprint import bp as bp_bacias
  app.register_blueprint(bp_bacias)


    