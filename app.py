from flask import Flask, render_template, request, redirect, url_for
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
    user_choice = request.form['choice']
    
    if user_choice == 'yes':
        # Logic for when user chooses yes
        pass
    elif user_choice == 'no':
        # Logic for when user chooses no
        # This will trigger a page reload, which will call this function again
        # with a new random song
        pass
    
    return redirect(url_for('home'))
        

if __name__ == '__main__':
    app.run(debug=True)