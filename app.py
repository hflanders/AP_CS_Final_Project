from flask import Flask
from route import ancient

def create_app():
    """creates an app and adds a blueprint"""
    app = Flask(__name__)
    app.register_blueprint(ancient)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=8081)