# routes/main_routes.py
from flask import Blueprint, jsonify, request
from services.db import collection
from services.lyrics_search import search_lyrics
import random

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def home():
    # Get a list of all songs
    all_songs = list(collection.find({}, {'Sangtittel': 1, 'Artist':1, 'Spraak':1,'_id': 0}))

    if not all_songs:
        return jsonify({"error": "No songs in database"}), 404
    
    # Randomly select a song
    random_song = random.choice(all_songs)

    # Store the language in session
    # session['song_language'] = random_song['Spraak']
    
    return jsonify( title=random_song['Sangtittel'],
                    artist=random_song['Artist'],
                    language=random_song['Spraak'])

@main_routes.route('/process_request', methods=['POST'])
def process_request():
    data = request.json
    song_title = data.get['song_title']
    artist_name = data.get['artist']
    user_choice = data.get['choice']

    print(f"Received request for {song_title} by {artist_name}, choice: {user_choice}")  # Debug print

    result = collection.messages.find_one({
        "Sangtittel": song_title,
        "Artist": artist_name
            })

    print(f"Database result: {result}")
        
    if result["Tekst_tilgjengelig"]:
    # Step 3: Return the text file
    # Note: This is a placeholder. You'll need to implement the actual file retrieval.
        print("Tekst tilgjengelig")
        return jsonify({"success": True, "message": f"Tekst tilgjengelig for {song_title} med {artist_name}"})
    else:
        print("Tekst ikke tilgjengelig, starter internettsøk")
        
        return jsonify({"error": "Tekst ikke tilgjengelig i databasen. Søker online..."})
        lyrics = search_lyrics(song_title, artist_name, session.get('song_language'))
        return jsonify({"success": True, "message": f"Lyrics searched for {song_title}", "search_results": search_results})
    else:
        # Song not found in database
        print("Sang ikke funnet i databasen")
        return jsonify({"error": "Sang ikke funnet i databasen"})

    print("Feil - laster siden om igjen")
    return jsonify({"error": str(e)})

