from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
import random

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
    all_songs = list(collection.find({}, {'Sangtittel': 1, 'Artist':1, '_id': 0}))
    
    # Randomly select a song
    random_song = random.choice(all_songs)
    
    return render_template('index.html', 
                          title=random_song['Sangtittel'],
                          artist=random_song['Artist'])

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
                return jsonify({"success": True, "message": f"Lyrics available for {song_title} by {artist_name}"})
            else:
                return jsonify({"error": "Lyrics not available in database. Searching online..."})

        else:
            # Song not found in database
            return jsonify({"error": "Song not found in database"})

    elif user_choice == 'no':
         return redirect(url_for('home'))
        # Logic for when user chooses no
        # This will trigger a page reload, which will call this function again
        # with a new random song
    
    return redirect(url_for('home'))
        

if __name__ == '__main__':
    app.run(debug=True)