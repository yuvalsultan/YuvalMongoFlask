from flask import Flask
from exten import mongo
import requests
from website.models import Movie
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjahkjshkjdhjs'
    app.config['MONGO_URI'] = 'mongodb+srv://yuvalsultan:Yy200298@cluster0.bqvic.mongodb.net/MyDb?retryWrites=true&w=majority'

    mongo.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    print('Yay')

    return app


