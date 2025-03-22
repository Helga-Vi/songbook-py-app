from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import random
from lyrics_search import search_lyrics


app = Flask(__name__)

#Upload static (style) files
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(app.config['UPLOAD_FOLDER'], path)


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['songbook_db']  # Create a database named 'songbook_db'
collection = db['messages']  # Create a collection named 'messages'

@app.route('/')
def home():
    # Get a list of all songs
    all_songs = list(collection.find({}, {'Sangtittel': 1, 'Artist':1, 'Spraak':1,'_id': 0}))
    
    # Randomly select a song
    random_song = random.choice(all_songs)
    
    return render_template('index.html', 
                          title=random_song['Sangtittel'],
                          artist=random_song['Artist'],
                          language=random_song['Spraak'])

@app.route('/process_request', methods=['POST'])
def process_request():
    song_title = request.form['song_title']
    artist_name = request.form['artist']
    user_choice = request.form['choice']

    print(f"Received request for {song_title} by {artist_name}, choice: {user_choice}")  # Debug print
    
    if user_choice == 'yes':
        # Logic for when user chooses yes
         # Step 1: Query the database
        result = db.messages.find_one({
            "Sangtittel": song_title,
            "Artist": artist_name
        })

        print(f"Database result: {result}")

        if result:
            # Step 2: Check Tekst_tilgjengelig field
            if result["Tekst_tilgjengelig"]:
                # Step 3: Return the text file
                # Note: This is a placeholder. You'll need to implement the actual file retrieval.
                print("Tekst tilgjengelig")
                return jsonify({"success": True, "message": f"Tekst tilgjengelig for {song_title} med {artist_name}"})
            else:
                print("Tekst ikke tilgjengelig, starter internettsøk")
                return jsonify({"error": "Tekst ikke tilgjengelig i databasen. Søker online..."})
                lyrics = search_lyrics(song_title, artist_name, language)

                return lyrics
        else:
            # Song not found in database
            print("Sang ikke funnet i databasen")
            return jsonify({"error": "Sang ikke funnet i databasen"})

    elif user_choice == 'no':
        print("Laster siden om igjen")
        return jsonify({"error": "Vi finner en ny sang til deg"})
        # Logic for when user chooses no
        # This will trigger a page reload, which will call this function again
        # with a new random song


    print("Feil - laster siden om igjen")
    return jsonify({"error": str(e)})
    
        

if __name__ == '__main__':
    app.run(debug=True)