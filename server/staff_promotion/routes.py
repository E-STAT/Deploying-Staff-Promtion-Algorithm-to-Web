import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)

Secret_key = os.environ.get("SECRET_KEY")
Database_Uri = os.environ.get("SQLALCHEMY_DATABASE_URI")

app.config["SECRET_KEY"] = Secret_key
app.config["SQLALCHEMY_DATABASE_URI"] = Database_Uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Qualification = db.Column(db.String(5), nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Trainings_Attended = db.Column(db.Integer, nullable=False)
    Last_performance_score = db.Column(db.Integer, nullable=False)
    Targets_met = db.Column(db.Boolean, nullable=False)
    Previous_Award = db.Column(db.Boolean, nullable=False)
    Training_score_average = db.Column(db.Integer, nullable=False)
    Foreign_schooled = db.Column(db.Boolean, nullable=False)
    Marital_Status = db.Column(db.Boolean, nullable=False)
    Past_Disciplinary_Action = db.Column(db.Boolean, nullable=False)
    Previous_IntraDepartmental_Movement = db.Column(db.Boolean, nullable=False)
    No_of_previous_employers = db.Column(db.Boolean, nullable=False)
    Age_employed = db.Column(db.Integer, nullable=False)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


@app.route("/form", methods=["POST"])
def fun_forms():
    user_schema = UserSchema()

    Qualification = request.json['Qualification']
    Gender = request.json['Gender']
    Trainings_Attended = request.json['Trainings_Attended']
    Last_performance_score = request.json['Last_performance_score']
    Targets_met = request.json['Targets_met']
    Previous_Award = request.json['Previous_Award']
    Training_score_average = request.json['Training_score_average']
    Foreign_schooled = request.json['Foreign_schooled']
    Marital_Status = request.json['Marital_Status']
    Past_Disciplinary_Action = request.json['Past_Disciplinary_Action']
    Previous_IntraDepartmental_Movement = request.json['Previous_IntraDepartmental_Movement']
    No_of_previous_employers = request.json['No_of_previous_employers']
    Age_employed = request.json['Age_employed']

    subject = User(Qualification, Gender, Trainings_Attended, Last_performance_score, Targets_met, Previous_Award,
                   Training_score_average, Foreign_schooled, Marital_Status, Past_Disciplinary_Action,
                   Previous_IntraDepartmental_Movement, No_of_previous_employers, Age_employed)

    try:
        db.session.add(subject)
        db.session.commt()

        return user_schema.jsonify(subject)
    except IntegrityError:
        db.session.rollback()
