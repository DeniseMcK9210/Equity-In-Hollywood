import os

import pandas as pd
import numpy as np

from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

#################################################
# Database Setup
#################################################

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

#Render intro page
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

#Pull data from db
@app.route("/movies")
def moviedata():
    #Create dataframe
    movie_df = pd.DataFrame(list(mongo.db.collection_name.find({}))

    # Sort by domestic gross for bubble chart?
    movie_df.sort_values(by=dom_gross2013, ascending=False, inplace=True)

    #Create decades column. round down to nearest 10
    def round_down(num, divisor):
    return num - (num%divisor)

    year = movie_df.year.values.tolist()
    decade = []
    for y in year:
        decade.append(round_down(y, 10))

    # Format the data to send as json
    data = {
        "id": movie_df.imdbid.values.tolist(),
        "bechdel_rating": movie_df.bechdel_rating.values.tolist(),
        "title": movie_df.title.values.tolist(),
        "year": movie_df.year.values.tolist(),
        "binary": movie_df.binary.values.tolist(),
        "budget": movie_df.budget_2013.values.tolist(),
        "dom_gross": movie_df.dom_gross2013.values.tolist(),
        "int_gross": movie_df.int_gross2013.values.tolist(),
        "genre": movie_df.genres.values.tolist(),
        "genreA": movie_df.A.values.tolist(),
        "genreB": movie_df.B.values.tolist(),
        "genreC": movie_df.C.values.tolist(),
        "decade": decade,
        "imdb_rating": movie_df.averageRating.values.tolist(),
        "num_votes": movie_df.numVotes.values.tolist()
    }
    return jsonify(data)



if __name__ == "__main__":
    app.run()