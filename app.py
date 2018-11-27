from flask import Flask, session, request, render_template, make_response, redirect
from surveys import *

app = Flask(__name__)

app.secret_key = "secret"


@app.route('/')
def index():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions

    survey_satisfaction = surveys['satisfaction']
    survey_personality = surveys['personality']

    session['response'] = []
    url = ""
    picked_survey = request.form.get("surveys")
    print(picked_survey)
    # if customer pick go to question/0
    if picked_survey == "satisfaction":
        url = 'http://127.0.0.1:5000/questions/0'
    elif picked_survey == 'personality':
        url = '##'
    # if rithm picked go to $^^%

    return render_template(
        'index.html',
        title=title,
        instructions=instructions,
        satisfaction=survey_satisfaction,
        personality=survey_personality,
        url=url )

# session can be [ satisfaction: [q1, q2, q3], personality:[q1, q2, q3]]
# @app.route('/questions/<num>', methods=['GET'])
# def question():
#     question_0 = satisfaction_survey.questions[0].question

#     return render_template('questions.html', question_0 = question_0)
#  go to pick the surveyr page
# @app.route('/surveys')
# def choose_survey():

#     return render_template('surveys.html')


@app.route('/questions/<num>', methods=['POST'])
#   add to session and going on to next question
def question(num):
    next_page = int(num) + 1
    link = f'/questions/{next_page}'
    # import pdb
    # pdb.set_trace()
    if int(num) > 3:
        return redirect('/thanks')

    question = satisfaction_survey.questions[int(num)].question
    new_response = request.form.get('res', "wrong")
    print(num)

    if not int(num) == 0:
        test_session = session['response']
        test_session.append(new_response)
        session['response'] = test_session
    print(session['response'])

    # redirect
    # try:
    #     return render_template(
    #         'questions.html', question=question, link=link, num=int(num))
    # except IndexError:
    #     return redirect('/thanks')
    return render_template(
        'questions.html', question=question, link=link, num=int(num))


@app.route('/thanks')
def say_thanks():

    return render_template('thanks.html')
