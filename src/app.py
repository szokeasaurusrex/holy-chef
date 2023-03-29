from flask import Flask, render_template, request
from src.python.elastic_manager import ElasticManager

app = Flask(__name__)

@app.route("/")
def home():
    """Home page"""
    return render_template('index.html', results = [])

@app.route('/generate_recipes', methods=['POST'])
def generate_recipies():
    """Handles submission of the "Generate Recipes" button."""
    # Maybe there is a better way to do this so we don't have to reinsantiate every time
    manager = ElasticManager('https://localhost:9200')
    # If the minutes field is not a float, return an error message
    try:
        float(request.form['time_to_cook'])
    except ValueError:
        return 'Error: You must enter a number for the "Time To Cook" field.'

    results = manager.retrieve_recipe(request.form)

    return render_template('results.html', results=results)

@app.route('/ping')
def ping():
    """Ping test (for unit testing)"""
    return 'pong'
