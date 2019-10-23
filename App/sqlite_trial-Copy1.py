#!/usr/bin/env python
# coding: utf-8

# import dependencies
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    # create a database connection to SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    #finally:
     #   if conn:
      #      conn.close()
            
if __name__ == '__main__':
    create_connection(r'../App/bechdel.db')


# function to create table 
def create_table(conn, create_table_sql):
    # create table from create_table_sql
    #:param conn: Connection object
    #:param create_table_sql: a CREATE TABLE statement
    #:return:
        
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        
    except Error as e:
        print(e)


def main():
    database = r'../App/bechdel.db'
    
    create_bechdel_table = CREATE TABLE IF NOT EXISTS bechdel (
                        imdbid INTEGER PRIMARY,
                        bechdel_rating INTEGER NOT NULL,
                        title TEXT NOT NULL,
                        year INTEGER NOT NULL,
                        binary INTEGER NOT NULL,
                        budget_2013 INTEGER NOT NULL,
                        domgross_2013 INTEGER NOT NULL,
                        intgross_2013 INTEGER NOT NULL,
                        genres TEXT NOT NULL,
                        A TEXT NOT NULL,
                        B TEXT NOT NULL,
                        C TEXT NOT NULL,
                        averageRating REAL NOT NULL,
                        numVotes INTEGER NOT NULL
                        );
    
    # create a database connection
    conn = create_connection(database)
    
    # create tables
    if conn is not None: 
        create_table(conn, create_bechdel_table)
        
    else:
        print("Error! Cannot connect!")

if __name__ == '__main__':
    main()







