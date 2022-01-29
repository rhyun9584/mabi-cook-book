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

    # zip() 함수 사용을 위한 확장
    app.jinja_env.globals.update(zip=zip)

    # DB connecting
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # bp for routing
    from .views import main_views, auth_views, book_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(book_views.bp)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html')

    return app
