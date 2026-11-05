import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

db = SQLAlchemy(app)

class Review(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    reviewer_name = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    date= db.Column(db.Date)
    sentiment_score=db.Column(db.Float)
    sentiment_label=db.Column(db.String(20))


@app.route("/")
def home():
    return "Hello from v2"


if __name__ == "__main__":
    app.run(debug=True)