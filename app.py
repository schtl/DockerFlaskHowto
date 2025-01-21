from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')
