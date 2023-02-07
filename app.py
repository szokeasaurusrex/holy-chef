from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/generate_recipes', methods=['POST'])
def generate_recipies():
    return request.form