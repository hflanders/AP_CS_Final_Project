# AP_CS_Final_Project
This is an AP computer science submission where the student created a web questionnaire.

in-depth description: talk about how the questionnaire works using html flask user selects the answer and then you get the result talk about how the selection works and how it is a very simple selection thing that doesn't have a good way to solve ties

In this questionnaire we created html files that creates a class and a url for each individual html file, so each question is it's own url. The flask user will select the answer they feel best fits the question, then whatever the leader the answer coincides with will gain a point. The url will then direct the computer to the next question's url. After answering all the questions, whatever leader has the most points will then be printed as the "character that best fits you". If there is a tie then the code will randomly pick one of the characters from the two characters tied in the leader list. After getting your character you can type in the url: http://localhost:8081/reset, to reset the quiz to take again. There is a seperate url: http://localhost:8081/welcome, which directs  the viewer to a picture depicting the possible characters they can fit. 

 what the question is in the questionnaire

Mention the technologies used with link to place
Flask:
https://flask.palletsprojects.com/en/1.1.x/testing/
https://flask.palletsprojects.com/en/3.0.x/

pytest:
https://docs.pytest.org/en/8.0.x/