from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, Length, URL, ValidationError

def check_animal(form, field):
    if field.data.lower() not in ["cat", "dog", "porcupine"]:
        raise ValidationError('Sorry, we only have room left for dogs, cats, and porcupines.\nPlease try again later.')

class PetForm(FlaskForm):
    """Form for adding a pet"""
    name = StringField("Pet Name", validators=[InputRequired(), Length(max=31)])
    species = StringField("Species", validators=[InputRequired(), Length(max=31), check_animal])
    photo_url = StringField("Photo URL", validators=[Length(max=2047), URL(message = "You must enter a valid URL")])
    age = IntegerField("Age", validators=[NumberRange(min=0,max=30, message="Age must be between 0 and 30")])
    notes = TextAreaField("Notes")
    available = BooleanField(default="checked")

