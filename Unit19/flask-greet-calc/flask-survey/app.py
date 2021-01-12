from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


responses = []


@app.route("/")
"""
Homepage for the questionnaire
it only has a start button, the title of the survey, and instructions
"""


def homepage():
    title = survey.title
    instructions = survey.instructions
    responses.clear()
    return render_template("home.html", title=title, instructions=instructions)


@app.route("/questions/<int:id>")
"""
Question page - presents the question and the the choices that go along with the question
has a submit button that will record what the user selected
If the length of the responses is shorted than the URL ID, the user is redirected back to their next question
If there are enough repsonses, the user is redirected to thank you page
"""


def questionnaire(id):
    if id > len(responses):
        flash("trying to access out of order")
        return redirect(f"/questions/{len(responses)}")

    if len(responses) == len(survey.questions):
        return redirect("/thanks")

    query_set = survey.questions[id]
    question = query_set.question
    choices = query_set.choices

    return render_template("questionnaire.html", question=question, choices=choices, id=id)


@app.route("/answer", methods=["GET", "POST"])
""" 
The user's responses are sent as a POST request and recorded in responses variable
the user is then redirected back to their next question
"""


def update_question():
    answer = request.form["choice"]
    responses.append(answer)

    if len(responses) == len(survey.questions):
        return redirect("/thanks")

    return redirect(f"/questions/{len(responses)}")


@app.route("/thanks")
""" thank you page that shows after user answers all questions"""


def thanks_page():
    return render_template("thanks.html")
