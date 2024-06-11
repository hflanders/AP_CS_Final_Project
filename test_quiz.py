from demigods import Demigods

def test_equality():
    quiz = Demigods(0,0,0,0,0)
    # create a list of all possible outcomes
    heroes = ['Percy Jackson', 'Grover Underwood', 'Annabeth Chase', 'Nico Di Angelo', 'Thalia Grace']
    quiz.add('percy')
    # we are asserting that the answer if none of the characters are selected will be randomly selected
    assert quiz.select() in heroes

def test_quiz():
    # this tests to make sure that if this were the points it would provide this answer
    quiz = Demigods(2,1,1,2,5)
    assert quiz.select() == 'Thalia Grace'