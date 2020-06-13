#libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_cors import CORS
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)

from flask_sqlalchemy import SQLAlchemy
ENG = create_engine("sqlite:///soccer_data.db")

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def skills_attributes():
   with ENG.connect() as con:
    rs = con.execute('SELECT Name, Age, Height, Weight, Nationality, Value, Overall, Potential, Club, Position FROM soccer_data')

    return jsonify({'Result': [dict(r) for r in rs]})

@app.route("/GK")
def goalkeeper():
   with ENG.connect() as con:
    rs = con.execute("SELECT Name, Age, Height, Weight, Nationality, Value, Overall, Potential, Club FROM soccer_data WHERE Position='GK'")

    return jsonify({'Result': [dict(r) for r in rs]})

@app.route("/DEF")
def defender():
   with ENG.connect() as con:
     rs = con.execute("SELECT Name, Age, Height, Weight, Nationality, Value, Overall, Potential, Club FROM soccer_data WHERE Position='DEF'")

     return jsonify({'Result': [dict(r) for r in rs]})

@app.route("/MID")
def midfield():
   with ENG.connect() as con:
    rs = con.execute("SELECT Name, Age, Height, Weight, Nationality, Value, Overall, Potential, Club FROM soccer_data WHERE Position='MID'")

    return jsonify({'Result': [dict(r) for r in rs]})

@app.route("/FWD")
def attack():
   with ENG.connect() as con:
    rs = con.execute("SELECT Name, Age, Height, Weight, Nationality, Value, Overall, Potential, Club FROM soccer_data WHERE Position='FWD'")

    return jsonify({'Result': [dict(r) for r in rs]})

if __name__ == "__main__":
    app.run()