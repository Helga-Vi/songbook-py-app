from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form.get('message')

         # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['songbook_db']  # Create a database named 'songbook_db'
        collection = db['messages']  # Create a collection named 'messages'

        # Insert the message into MongoDB
        result = collection.insert_one({'text': message})
        print(f"Inserted document with ID: {result.inserted_id}")

        return render_template('index.html', message=message)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)