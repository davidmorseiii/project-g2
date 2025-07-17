from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    games = relationship("GameResult", backref="user")
    question_sets = relationship("QuestionSet", backref="creator")

class QuestionSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    creator_id = db.Column(db.Integer, ForeignKey("user.id"))
    questions = relationship("Question", backref="question_set")

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer, ForeignKey("question_set.id"))
    prompt = db.Column(db.String(255), nullable=False)
    choices = db.Column(db.Text, nullable=False)  # store as JSON string
    correct_answer = db.Column(db.String(255), nullable=False)

    def set_choices(self, choice_list):
        self.choices = json.dumps(choice_list)

    def get_choices(self):
        return json.loads(self.choices)

class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    set_id = db.Column(db.Integer, ForeignKey("question_set.id"))
    score = db.Column(db.Integer, nullable=False)
