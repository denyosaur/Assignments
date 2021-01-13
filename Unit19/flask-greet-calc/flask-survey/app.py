from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    '''Homepage for the questionnaire
    it only has a start button, the title of the survey, and instructions'''
    title = survey.title
    instructions = survey.instructions
    return render_template("home.html", title=title, instructions=instructions)


@app.route("/sess_save", methods=["GET", "POST"])
def sess_save():
    session["responses"] = []
    return redirect("/questions/0")


@app.route("/questions/<int:id>")
def questionnaire(id):
    '''
    Question page - presents the question and the the choices that go along with the question
    has a submit button that will record what the user selected
    If the length of the responses is shorted than the URL ID, the user is redirected back to their next question
    If there are enough repsonses, the user is redirected to thank you page
    '''
    responses = session.get("responses")
    if (responses is None):
        return redirect("/")
    if len(responses) != id:
        flash("trying to access out of order")
        return redirect(f"/questions/{len(session_ans)}")

    if len(responses) == len(survey.questions):
        return redirect("/thanks")

    query_set = survey.questions[id]
    question = query_set.question
    choices = query_set.choices

    return render_template("questionnaire.html", question=question, choices=choices, id=id)


@app.route("/answer", methods=["GET", "POST"])
def update_question():
    '''
    The user's responses are sent as a POST request and recorded in responses variable
    the user is then redirected back to their next question
    '''
    choice = request.form["choice"]

    session_ans = session["responses"]
    session_ans.append(choice)
    session["responses"] = session_ans

    if len(session_ans) == len(survey.questions):
        return redirect("/thanks")

    return redirect(f"/questions/{len(session_ans)}")


@app.route("/thanks")
def thanks_page():
    ''' thank you page that shows after user answers all questions'''
    return render_template("thanks.html")
