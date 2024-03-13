from flask import Flask, request, redirect, render_template
from demigods import Demigods
from route import ancient

app = Flask(__name__)

categories = Demigods(0,0,0)

@ancient.route('/reset')
def reset():
    categories.clear()
    return 'the categories has been reset'

@ancient.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    answers = ['','','']

    if request.method == 'GET':
        return render_template('question_1.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')

        return redirect('/results')

@ancient.route('/results')
def get_results():
    return 'the character you best fit is ' + categories.select()

def create_app():
    """creates an app and adds a blueprint"""
    app = Flask(__name__)
    app.register_blueprint()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=8081)