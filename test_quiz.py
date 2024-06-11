from demigods import Demigods

def test_equality():
    quiz = Demigods(0,0,0,0,0)
    # create a list of all possible outcomes
    heroes = ['Percy Jackson', 'Grover Underwood', 'Annabeth Chase', 'Nico Di Angelo', 'Thalia Grace']
    quiz.add('percy')
    # 
    assert quiz.select() in heroes

def test_quiz():
    quiz = Demigods(5,1,1,2,2)
    assert quiz.select() == 'Percy Jackson'