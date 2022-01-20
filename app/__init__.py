from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # jinja2에서 {% break %} 사용을 위한 구문
    # app.jinja_env.add_extension('jinja2.ext.loopcontrols')

    # DB connecting
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # bp for routing
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
