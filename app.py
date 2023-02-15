
"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet, make_db, seed_db
from forms import PetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Pet_Agency' #use this for production
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Pet_Agency_Test' #use this for testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


app.config['SECRET_KEY'] = 'chickenzarcool21837'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def homepage():
    """The homepage"""
    select = Pet.query.all()
    return render_template("home.html", pets=select)


@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """Adding a new pet"""
    form = PetForm()
    if form.validate_on_submit():
        Pet.add(form)
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)



@app.route('/<int:pet_id>', methods = ["GET", "POST"])
def show_edit_pet(pet_id):
    """Show pet information and allow edit"""
    select = Pet.query.get_or_404(pet_id)
    form = PetForm(obj = select)

    if form.validate_on_submit():
        Pet.edit(pet_id, form)
        return redirect("/")

    else:
        return render_template("edit_pet_form.html", form=form, pet=select)




