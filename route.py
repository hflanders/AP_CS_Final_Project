from flask import Blueprint, render_template

ancient = Blueprint('ancient', __name__)

@ancient.route('/welcome_image', methods = ['GET'])
def serve_image():
    return render_template('image.html')