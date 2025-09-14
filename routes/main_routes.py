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
    try:
        print(f"Request headers: {request.headers}")
        data = request.json
        song_title = data.get('song_title')
        artist_name = data.get('artist')
        language = data.get('language')

        print(f"Received request for {song_title} by {artist_name} in {language}")  # Debug print

        if not song_title or not artist_name or not language:
            return jsonify({"error": "Missing required fields"}), 400


        result = collection.messages.find_one({
            "Sangtittel": song_title,
            "Artist": artist_name,
            "Language": language
                })

        print(f"Database result: {result}")
        
        if result:
        # Step 3: Return the text file
        # Note: This is a placeholder. You'll need to implement the actual file retrieval.
            return jsonify({"success": True, "message": f"Tekst tilgjengelig for {song_title} med {artist_name} på {language}"})
        else:
            print("Tekst ikke tilgjengelig, starter internettsøk")
            lyrics = search_lyrics(song_title, artist_name, language)

        if lyrics:
            return jsonify({"success": True, "message": f"Lyrics searched for {song_title}", "search_results": lyrics})
        else:
        # Song not found in database
            return jsonify({"error": "Sang ikke funnet i databasen"})

    except Exception as e:
        # Generic error handling
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@main_routes.route('/new_song')
def new_song():
    #Needs to be turned into a post route when the frontend comes up
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

@main_routes.route('/choose_lyrics_source', methods=['POST'])
def choose_lyrics_source():
    try:
        print(f"Request headers: {request.headers}")
    
    except Exception as e:
        # Generic error handling
        print(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500
