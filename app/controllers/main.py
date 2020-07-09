from flask import render_template, url_for
from app import app, db

# Default route
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')