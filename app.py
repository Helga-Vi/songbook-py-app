from flask import Flask, render_template, request
from pymongo import MongoClient
import random

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongdb://localhost:27017/')
db = client['songbook_db']  # Create a database named 'songbook_db'
collection = db['messages']  # Create a collection named 'messages'

@app.route('/')
def home():
    # Get a list of all songs
    all_songs = list(collection.find({}, {'title': 1, '_id': 0}))
    
    # Randomly select a song
    random_song = random.choice(all_songs)
    
    return render_template('index.html', 
                          title=random_song['title'],
                          artist=random_song['title'].split()[0])

@app.route('/process_request', methods=['POST'])
def process_request():
    song_title = request.form['song_title']
    user_choice = request.form['choice']
    
    # Your logic here to handle the user's choice
    
    return redirect(url_for('home'))
        

if __name__ == '__main__':
    app.run(debug=True)