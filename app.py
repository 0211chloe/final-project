from flask import Flask, render_template, request
from functions import movie_recs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        period = request.form.get("period")
        movies = movie_recs(city, period)
    return render_template("index.html", movies=movies)
