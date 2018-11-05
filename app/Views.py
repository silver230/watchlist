from flask import render_template
from app import app
from .request import get_movies

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'Hello World '
    # message = 'how about you'
    return render_template('index.html',message = message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)
def index ():
    '''
    view root page function that returns the index page and its data
    '''
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_movies)
    

def movie():

    '''
    View root page function that returns the movie page and its data
    '''

    title = f'Here is your best {movie_id}'
    return render_template('movie.html', title = title)
