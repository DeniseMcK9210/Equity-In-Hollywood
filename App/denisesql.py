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
 
    return conn


#Function to create table and insert csv data
def create_table(conn, create_table_sql, csvfile):
    """ create a table from the create_table_sql statement then import csv
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        df = pd.read_csv(csvfile)
        df.to_sql('bechdel', conn, if_exists='append', index=False)
      
      #close connection
       # conn.close()
        
    except Error as e:
        print(e)


#Query the table
def select_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM bechdel")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

     #close connection
        conn.close()


#Connect to db, create table, import csv data
def main():
    database = r'../App/bechdel.db'
 
    create_bechdel_table = """CREATE TABLE IF NOT EXISTS bechdel (
                        imdbid integer NOT NULL,
                        bechdel_rating integer NOT NULL,
                        title text NOT NULL,
                        year integer NOT NULL,
                        binary integer NOT NULL,
                        budget_2013 integer NOT NULL,
                        domgross_2013 integer NOT NULL,
                        intgross_2013 integer NOT NULL,
                        genres text NOT NULL,
                        A text NOT NULL,
                        B text NOT NULL,
                        C text NOT NULL,
                        averageRating real NOT NULL,
                        numVotes integer NOT NULL);"""
    
    csv = "../bechdel_final.csv"
 
    # create a database connection
    conn = create_connection(database)
 
    # create tables
    if conn is not None:
        # create projects table and insert csv
        create_table(conn, create_bechdel_table, csv)
        select_all(conn)
    else:
        print("Error! cannot create the database connection.")
 
 
if __name__ == '__main__':
    main()