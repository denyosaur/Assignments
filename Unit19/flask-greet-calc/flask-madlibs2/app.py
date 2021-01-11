from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/home")
def homepage():
    words = story.prompts
    return render_template("homepage.html", words=words)

@app.route("/madlib")
def return_madlib():
    text = story.generate(request.args)
    req = request.args
    return render_template("madlib_results.html", text=text, req=req)
