"""Import to create Flask UI"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Hello word"""
    return render_template('index.html')
