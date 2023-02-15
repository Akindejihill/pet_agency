"""Models for Pet Adoption Agency."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = 'pets'
    def __repr__(self):
        return f"<user id={self.id} first name={self.name} species={self.species} age={self.age}>"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    name = db.Column(db.String(31),
                        nullable = False)

    species = db.Column(db.String(31),
                        nullable = False)

    photo_url = db.Column(db.Text,
        default = "https://2.bp.blogspot.com/-aeSomVAI-90/WW9MMVR1D4I/AAAAAAAA-fI/DWSV8lY6fI8MwjeZx_IMntaVNgrBhXqQACLcBGAs/s1600/No%2523-Puzzle-Collie-Brown-LPS-1.jpg")

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, 
                            nullable = False,
                            default = True)

    @classmethod
    def add(self, form):
        pet = Pet(name = form.name.data, species = form.species.data, photo_url = form.photo_url.data, age = form.age.data, notes = form.notes.data, available = form.available.data)
        db.session.add(pet)
        db.session.commit()

    
    @classmethod
    def edit(self, pet_id, form):
        pet = Pet.query.get(pet_id)
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
    
    @classmethod
    def delete(self, pet_id):
        Pet.query.filter_by(id = pet_id).delete()
        db.session.commit()



def make_db():
    db.drop_all()
    db.create_all()

def seed_db():
    pet1 = Pet(name = "Alen", species = "Kangaroo", age = 5, 
    notes = "Alen loves to box, so watch out!  Great companion!")

    pet2 = Pet(name = "Mooey", species = "Cow", age = 3, 
    notes = "Mooey is a pink cow and give strawberry milk!  Your kids will love her")

    pet3 = Pet(name = "Garfield", species = "Cat", age = 7, 
    notes = "Garfield loves to eat and sleep.  He eats PASTA, No lie!  Hates exercise though.  Makes a great door stop")

    pet4 = Pet(name = "King", species = "Dog", age = 1, 
    notes = "King is a doberman, of course.  Born for being tied to a stake in your front yard")

    pet5 = Pet(name = "Alexis", species = "Daughter", age = 15, 
    notes = "I mean. she's practically a cat.  She comes out of her room once a week to hiss at you.  Don't forget to feed her.")



    db.session.add_all([pet1, pet2, pet3, pet4, pet5])
    db.session.commit()
 