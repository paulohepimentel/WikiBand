from flask import render_template
from app import app, db

# Application Tables
from app.models.tables import Genre
from app.models.tables import Band


# Genre Select
@app.route("/genres-list")
def genres_list():
    # Selecting from the database
    genres = Genre.query.all()
    return render_template("select/genre.html", genres=genres)


# Band Select
@app.route("/bands-list")
def bands_list():
    # Selecting from the database
    bands = Band.query.all()
    return render_template("select/band.html", bands=bands)