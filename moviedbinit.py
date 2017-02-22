import sqlite3

connection = sqlite3.connect('movie_database.db')
print ('Opened database successfully')

    connection.execute('CREATE TABLE movies (name TEXT, year INTEGER, rating TEXT, genre TEXT)')
print ('Table created successfully')

connection.close()
