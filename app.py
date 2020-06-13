#libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
from sqlalchemy import create_engine

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///soccer_data.db"
ENG = create_engine("sqlite:///./soccer_data.db")

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/api")
def skills_attributes():
   with ENG.connect() as con:
    rs = con.execute('SELECT Name, Wage FROM soccer_data')
    # for r in rs:
    #     print(r)

    # name = [rs[0] for r in rs]
    # name = [result[0] for result in results]
    # salary = [result[1] for result in results]

    # api_display = rs
    # return jsonify(api_display)

    
    return jsonify({'Result': [dict(r) for r in rs]})

    # api_display = [{
    #     "Player": rs,
    # }]
    # return jsonify(api_display)


if __name__ == "__main__":
    app.run()