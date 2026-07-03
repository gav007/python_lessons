from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=['POST'])
def search():
    
    #get the key
    api_key=os.getenv("OMDB_API_KEY")
    
    # grap the input field of the form and give me the string value
    movie_title = request.form.get("movie").strip()
    
    # url to get the data
    url = "https://www.omdbapi.com"
    
    # query parameters
    query_params = {
        "apikey": api_key,
        "t": movie_title
    }
    
    # send response
    response = requests.get(url, params=query_params, timeout=5)

    # get json data
    data = response.json()
    
    return render_template(
    "index.html",
    title=data.get("Title"),
    year=data.get("Year"),
    director=data.get("Director"),
    genre=data.get("Genre"),
    rating=data.get("imdbRating"),
    plot=data.get("Plot"),
    box_office=data.get("BoxOffice")
)
    