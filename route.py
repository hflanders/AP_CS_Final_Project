from flask import Blueprint, render_template, request, redirect
from demigods import Demigods

ancient = Blueprint('ancient', __name__)

categories = Demigods(0,0,0,0,0)

@ancient.route('/welcome', methods = ['GET'])
def serve_image():
    return render_template('welcome_image.html')

@ancient.route('/reset')
def reset():
    categories.clear()
    return 'the categories has been reset'

@ancient.route('/question/1', methods = ['GET', 'POST'])
def first_question():
    answers = ['on a beach','in a library','in a forest', 'in your room', 'as a tree']

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
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/2')
    
@ancient.route('/question/2', methods = ['GET', 'POST'])
def second_question():
    answers = ['friends and family','knowledge','nature and animals', 'being recognized', 'freedom']

    if request.method == 'GET':
        return render_template('question_2.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/3')

@ancient.route('/question/3', methods = ['GET', 'POST'])
def third_question():
    answers = ['personal loyalty','hubris','low self-esteem', 'holding grudges', 'ambition']

    if request.method == 'GET':
        return render_template('question_3.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/4')

@ancient.route('/question/4', methods = ['GET', 'POST'])
def fourth_question():
    answers = ['drowning','spiders','small dark places', 'being outed', 'heights']

    if request.method == 'GET':
        return render_template('question_4.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/5')
    
@ancient.route('/question/5', methods = ['GET', 'POST'])
def fifth_question():
    answers = ['a medium length sword','a dagger','reed pipes', 'a long sword','a bow and arrows']

    if request.method == 'GET':
        return render_template('question_5.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/6')
    
@ancient.route('/question/6', methods = ['GET', 'POST'])
def sixth_question():
    answers = ['loyal','ambitious','trustworthy', 'curious','confident']

    if request.method == 'GET':
        return render_template('question_6.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/7')
    
@ancient.route('/question/7', methods = ['GET', 'POST'])
def seventh_question():
    answers = ['In a New York Apartment','In a lake cabin','In a cabin in the forest', 'In a Hotel','In a tree']

    if request.method == 'GET':
        return render_template('question_7.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/8')

@ancient.route('/question/8', methods = ['GET', 'POST'])
def eighth_question():
    answers = ['power over the water','super smarts and photographic memory','power over nature', 'the power of necromancy','power over lightning']

    if request.method == 'GET':
        return render_template('question_8.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/9')
    
@ancient.route('/question/9', methods = ['GET', 'POST'])
def ninth_question():
    answers = ['Posiedon','Athena','Pan', 'Hades','Zeus']

    if request.method == 'GET':
        return render_template('question_9.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/10')

@ancient.route('/question/10', methods = ['GET', 'POST'])
def tenth_question():
    answers = ['Hestia','Athena','Pan', 'Zeus','Artemis']

    if request.method == 'GET':
        return render_template('question_10.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/question/11')
    
@ancient.route('/question/11', methods = ['GET', 'POST'])
def eleventh_question():
    answers = ['Hestia','Athena','Pan', 'Zeus','Artemis']

    if request.method == 'GET':
        return render_template('question_11.html', answers = answers)
    
    if request.method == 'POST':
        selected = request.form['selected']
        if selected == answers[0]:
            categories.add('percy')
        if selected == answers[1]:
            categories.add('annabeth')
        if selected == answers[2]:
            categories.add('grover')
        if selected == answers[3]:
            categories.add('nico')
        if selected == answers[4]:
            categories.add('thalia')

        return redirect('/results')

@ancient.route('/results')
def get_results():
    return 'the character you best fit is ' + categories.select()