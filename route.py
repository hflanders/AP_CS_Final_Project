from flask import Blueprint, render_template

fight = Blueprint('fight', __name__)

@fight.route('/say', methods = ['GET'])
def say_hi():
    return 'hello world'