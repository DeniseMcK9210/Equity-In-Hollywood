import os

import pandas as pd
import numpy as np

import psycopg2
import sqlite3
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

app = Flask(__name__)


#################################################
# Database Setup
#################################################


class Movies(object):
    pass
 
#----------------------------------------------------------------------
   
engine = create_engine('sqlite:///db/trial.db', echo=False)
metadata = MetaData(engine)
bechdel_table = Table('bechdel_table', metadata, Column("imdbid", Integer, primary_key=True),
                      autoload=True)

mapper(Movies, bechdel_table)
 
Session = sessionmaker(bind=engine)
session = Session()

Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


# Save reference to table
#movies= Base.classes.bechdel_table
movies = metadata.tables['bechdel_table']

#Render intro page
@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

#Render home page
@app.route("/home")
def home():
    """Return the homepage."""
    return render_template("home.html")

#Render dashboard page
@app.route("/dashboard")
def dashboard():
    """Return the homepage."""
    return render_template("dashboard.html")

#Render viz1 page
@app.route("/genres-over-time")
def viz1():
    """Return the homepage."""
    return render_template("viz1.html")

#Render viz2 page
@app.route("/women-of-their-word")
def viz2():
    """Return the homepage."""
    return render_template("viz2.html")

#Render resources page
@app.route("/resources")
def resources():
    """Return the homepage."""
    return render_template("resources.html")

#Render resources page
@app.route("/title-search")
def titlesearch():
    """Return the homepage."""
    return render_template("title_search.html")

#Pull data from db
@app.route("/rmovies")
def movierows():
    # Use Pandas to perform the sql query
    #results = session.query(movies).all()
    #print(results[0])
    stmt = session.query(movies).statement
    movie_df = pd.read_sql_query(stmt, session.bind)


    # Sort by domestic gross for bubble chart?
    movie_df.sort_values(by="domgross_2013", ascending=False, inplace=True)

    #Create decades column. round down to nearest 10
    def round_down(num, divisor):
        return num - (num%divisor)

    year = movie_df.year.values.tolist()
    decade = []
    for y in year:
        decade.append(round_down(y, 10))

    movie_df["decade"] = decade

    # Format the data to send as json
    data = movie_df.to_json(orient='records')
    return jsonify(data)

#Pull data from db
@app.route("/cmovies")
def moviecolumns():
    # Use Pandas to perform the sql query
    stmt = session.query(movies).statement
    movie_df = pd.read_sql_query(stmt, session.bind)

    # Sort by domestic gross for bubble chart?
    movie_df.sort_values(by="domgross_2013", ascending=False, inplace=True)

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
        "dom_gross": movie_df.domgross_2013.values.tolist(),
        "int_gross": movie_df.intgross_2013.values.tolist(),
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
    app.run(debug=True)