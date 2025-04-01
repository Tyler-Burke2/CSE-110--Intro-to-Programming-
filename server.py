from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('subpage.html')  # Make sure the HTML is in the templates folder

# Route to start the Snake game
@app.route('/start_snake')
def start_snake():
    # This will run your snake game script
    # Make sure asdgsgd.py is in the same directory as server.py or provide the full path
    subprocess.Popen(['python', 'asdgsgd.py'])  # This runs the game in the background
    return "Snake game started!"  # You can return a response or redirect

if __name__ == '__main__':
    app.run(debug=True)
