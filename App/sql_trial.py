#Import dependencies
import pandas as pd
import csv, sqlite3
from sqlite3 import Error

#Function to connect to database
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 

CREATE TABLE "bechdel" (
                "imdbid" integer NOT NULL,
                "bechdel_rating" integer NOT NULL,
                "title" text NOT NULL,
                "year" integer NOT NULL,
                "binary" integer NOT NULL,
                "budget_2013" integer NOT NULL,
                "domgross_2013" integer NOT NULL,
                "intgross_2013" integer NOT NULL,
                "genres" text NOT NULL,
                "A" text NOT NULL,
                "B" text NOT NULL,
                "C" text NOT NULL,
                "averageRating" real NOT NULL,
                "numVotes" integer NOT NULL);
.mode csv
.separator ","
.import "../bechdel_final.csv" bechdel