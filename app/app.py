# app.py

from flask import Flask, render_template

def handle_bad_request(e):
    return render_template('404.html'), 404

def create_app():
    # added the static path so it can load images and stuff
    app = Flask(__name__, static_url_path='/static')

    app.config['SECRET_KEY'] = 'vikek-aurobindo'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.register_error_handler(400, handle_bad_request)
    
    return app