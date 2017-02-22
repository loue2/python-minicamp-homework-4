from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ('home.html')

@app.route('/new_movie', methods = ['POST'])
def new_movie():
    connection = sqlite3.connect('movie_database.db')
    cursor = connection.cursor()
    try:
        movie_name = request.form['movie_name']
        year = request.form['year']
        rating = request.form['rating']
        genre = request.form['genre']
        movie_info = (movie_name, year, rating, genre)
        print (movie_info)
        cursor.execute('INSERT INTO movies VALUES (?,?,?,?)', movie_info)
        connection.commit()
        message = 'Movie added. Thank you.'
    except:
        connection.rollback()
        message = 'Error.'
    finally:
        connection.close()
        return render_template('result.html', message = message)

@app.route('/movies')
def movies():
    connection = sqlite3.connect('movie_database.db')
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM movies')
        connection.commit()
        result = cursor.fetchall()
    except:
        connection.rollback()
        result = ('Database error')
    finally:
        connection.close()
        return jsonify(result)

@app.route('/search/')
def search():
    connection = sqlite3.connect('movie_database.db')
    cursor = connection.cursor()
    try:
        searchname = (request.args.get('name'),)

        cursor.execute('SELECT * FROM movies WHERE name =?', searchname)
        connection.commit()
        result = cursor.fetchall()
    except:
        connection.rollback()
        result = ('Database error')
    finally:
        return jsonify(result)
        connection.close()
