from demigods import Demigods

def test_equality():
    quiz = Demigods(0,0,0,0,0)
    quiz.add('percy')
    assert quiz.select() == 'Percy Jackson'

def test_quiz():
    quiz = Demigods(3,1,1,0,0)
    assert quiz.select() == 'Percy Jackson'