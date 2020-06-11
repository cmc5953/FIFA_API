#libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///soccer_data.db"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/api")
def skills_attributes():
    results = db.session.query(soccer_data.name, soccer_data.Wage).all()

    name = [result[0] for result in results]
    salary = [result[1] for result in results]

    api_display = [{
        "Player": name,
        "Salary": salary,
    }]
    return jsonify(api_display)


if __name__ == "__main__":
    app.run()