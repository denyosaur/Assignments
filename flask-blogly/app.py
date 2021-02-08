"""Blogly application."""

from flask import Flask, redirect, request, render_template
from models import db, connect_db, Users
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'

connect_db(app)
db.create_all()
toolbar = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return redirect('/users')

@app.route('/users')
def user_page():

    user_list = Users.query.order_by(Users.first_name, Users.last_name)
    return render_template('users.html', userlist=user_list)

@app.route('/users/new', methods=['GET'])
def new_user():
    return render_template('submituser.html')

@app.route('/users/new', methods=['POST'])
def post_new_user():
    first_n = request.form['first']
    last_n = request.form['last']
    img_l = request.form['img'] or None
    new_user = Users(first_name=first_n, last_name=last_n, img_url=img_l)

    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_info(user_id):
    user_info = Users.query.get_or_404(user_id)
    return render_template('userinfor.html', user_info=user_info)

@app.route('/users/<int:user_id>/edit', methods=['GET'])
def user_edit(user_id):
    user_info = Users.query.get_or_404(user_id)
    return render_template('edituser.html', user_info=user_info)

@app.route('/users/<int:user_id>/edit', methods=['POST'])
def make_edit(user_id):
    user_info = Users.query.get_or_404(user_id)
    user_info.first_name = request.form['first']
    user_info.last_name = request.form['last']
    user_info.img_url = request.form['img']

    db.session.add(user_info)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def user_delete(user_id):
    user_info = Users.query.get_or_404(user_id)
    db.session.delete(user_info)
    db.session.commit()
    return redirect('/users')