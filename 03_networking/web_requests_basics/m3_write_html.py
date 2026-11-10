movie_title = "Jaws"
movie_year = "1975"

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
        <p id="movie-title">Movie Title</p>

        <h3>Year</h3>
        <p id="movie-year">Movie Year</p>

        <h3>Director</h3>
        <p id="movie-director">Movie Director</p>

        <h3>Genre</h3>
        <p id="movie-genre">Movie Genre</p>

        <h3>Rating</h3>
        <p id="movie-rating">Movie Rating</p>

        <h3>Plot</h3>
        <p id="movie-plot">Movie Plot</p>

        <h3>Box-Office</h3>
        <p id="movie-box">Movie Box-Office</p>
      </div>
    </div>
  </body>
</html>
"""

with open("movie_output.html", "w") as file:
    file.write(html)

print("Created movie_output.html")
