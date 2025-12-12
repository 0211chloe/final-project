from flask import Flask, render_template, request
from functions import movie_recs

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/results", methods=["POST"])
def results():
    movies = []
    city = request.form.get("city")
    period = request.form.get("period")
    movies, temp, condition, clouds = movie_recs(city, period)
    return render_template("results.html", movies=movies, city=city, temp=temp, condition=condition, clouds=clouds)
