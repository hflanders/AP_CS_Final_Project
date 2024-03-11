from flask import Flask
from route import fight
import random

app = Flask(__name__)

@fight.route('/say', methods = ['GET'])
def say_hi():
    return 'hello world'




def create_app():
    """creates an app and adds a blueprint"""
    app = Flask(__name__)
    app.register_blueprint()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=8081)