from flask import Flask, render_template, session, request, redirect, jsonify
from boggle import Boggle
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
boggle_game = Boggle()


@app.route("/")
def homepage():
    """homepage for the game. Only has a 'Play' button"""
    session["board"] = None
    return render_template("homepage.html")


@app.route("/play")
def play_boggle():
    """Page that returns the Boggle board game page.
    Also sets up session with the board and number of plays"""
    games_played = session.get("nplays", 0)
    if (session["board"] == None):
        board = boggle_game.make_board()
        session["board"] = board
        return render_template("play.html", board=board, games_played=games_played)
    board = session["board"]
    return render_template("play.html", board=board, games_played=games_played)


@app.route("/check-word")
def check_word():
    """page for get request that checks whether a user submitted word is [valid, valid but not on board, not real word]"""
    guess = request.args["guess"]
    sess_board = session["board"]
    result = boggle_game.check_valid_word(sess_board, guess)
    print("help")
    return jsonify({'result': result})


@app.route("/high-score", methods=["POST"])
def high_score():
    """POST request to update the session of high score and games played"""
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    games_played = session.get("nplays", 0)
    session['games_played'] = games_played + 1
    session['highscore'] = max(score, highscore)
    return jsonify(brokeRecord=score > highscore)
