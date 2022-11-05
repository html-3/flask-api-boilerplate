from app.config import config
from app.extensions import db, migrate, ma
from app.posts.router import post_router
from app.users.router import user_router
from flask import Flask

from dd import create_dd

def create_app():

    ### Create APP
    app = Flask(__name__)
    app.config.from_object(config)


    ### Create ORM
    db.init_app(app)

    ### Create Migrations
    migrate.init_app(app)

    ### Create Validator
    ma.init_app(app)

    ### Blueprints
    app.register_blueprint(user_router)
    app.register_blueprint(post_router)

    create_dd(app)


    return app