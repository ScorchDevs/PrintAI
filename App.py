import os

from flask import Flask
import urllib.request, json 

import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)

bp = Blueprint('auth', __name__, url_prefix='/auth')


def create_app():
    # create and configure the app
    app = Flask(__name__)
    
    url = urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google")
    data = json.loads(url.read().decode())
    
    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello World!'

    from . import auth
    app.register_blueprint(auth.bp)

    return app

create_app().run()