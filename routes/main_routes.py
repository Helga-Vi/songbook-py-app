# routes/main_routes.py
from flask import Blueprint, jsonify

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    def home():
    # Get a list of all songs
    all_songs = list(collection.find({}, {'Sangtittel': 1, 'Artist':1, 'Spraak':1,'_id': 0}))
    
    # Randomly select a song
    random_song = random.choice(all_songs)

    # Store the language in session
   # session['song_language'] = random_song['Spraak']
    
    return render_template('index.html', 
                          title=random_song['Sangtittel'],
                          artist=random_song['Artist'],
                          language=random_song['Spraak'])

