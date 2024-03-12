from flask import Flask, request, redirect
from demigods import Demigods
from route import ancient

app = Flask(__name__)

@ancient.route('/reset')
def reset():
    demigods.clear()
    return 'the list has been reset'

@ancient.route('/question/1', methods = ['GET', 'POST'])




def create_app():
    """creates an app and adds a blueprint"""
    app = Flask(__name__)
    app.register_blueprint()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=8081)