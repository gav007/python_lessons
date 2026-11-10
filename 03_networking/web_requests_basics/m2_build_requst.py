import os
import requests
from pprint import pprint

# key
api_key=os.getenv("OMDB_API_KEY")

# input
movie_title = input("Enter the movie name here >> ")

url = "https://www.omdbapi.com"

query_params = {
    "apikey": api_key,
    "t": movie_title
}

response = requests.get(url, params=query_params, timeout=5)

data = response.json()

html = f"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>The Movie Hub</title>
  </head>
  <body>
    <div class="main-container">
      <div class="title-box">
        <h1>MOVIE INFO</h1>
      </div>

      <div class="display-container">
        <label for="movie-input">Enter your movie</label>
        <input type="text" name="movie" id="movie-input" />

        <h3>Title</h3>
        <p id="movie-title">{data.get("Title")}</p>

        <h3>Year</h3>
        <p id="movie-year">{data.get("Year")}</p>

        <h3>Director</h3>
        <p id="movie-director">{data.get("Director")}</p>

        <h3>Genre</h3>
        <p id="movie-genre">{data.get("Genre")}</p>

        <h3>Rating</h3>
        <p id="movie-rating">{data.get("imdbRating")}</p>

        <h3>Plot</h3>
        <p id="movie-plot">{data.get("Plot")}</p>

        <h3>Box-Office</h3>
        <p id="movie-box">{data.get("BoxOffice")}</p>
      </div>
    </div>
  </body>
</html>
"""

with open("movie_output.html", "w") as file:
    file.write(html)

print("Created movie_output.html")


print()
print("Selected MOVIE INFO")
print("Title:", data.get("Title"))
print("Year:", data.get("Year"))
print("Director:", data.get("Director"))
print("Genre:", data.get("Genre"))
print("IMDb Rating:", data.get("imdbRating"))
print("Plot:", data.get("Plot"))
print("Box Office:", data.get("BoxOffice"))

