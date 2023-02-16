from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """Home page"""
    return render_template('index.html', results = [])

@app.route('/generate_recipes', methods=['POST'])
def generate_recipies():
    """Handles submission of the "Generate Recipes" button."""
    return render_template('index.html', results=[
        {
            'title': 'Basic Omelette',
            'ingredients': ['Eggs', 'Cheese', 'Butter', 'Bacon Bits'],
            'url': 'https://natashaskitchen.com/perfect-omelette-recipe/',
            'minutes': 5,
        },
        {
            'title': 'Vegetable Stuffed Omelette',
            'ingredients': ['Eggs', 'Cheese', 'Butter', 'Mushrooms', 'Onion', 'Red pepper',
                            'Spinach'],
            'url': 'https://natashaskitchen.com/perfect-omelette-recipe/',
            'minutes': 15,
        },
        {
            'title': 'Frittata ',
            'ingredients': ['Eggs', 'Cheese', 'Butter', 'Cream', 'Tomatoes','Spinach'],
            'url': 'https://natashaskitchen.com/perfect-omelette-recipe/',
            'minutes': 30,
        },
    ])
