from flask import render_template, redirect, url_for
from app import app, db

# Application Tables
from app.models.tables import Genre
from app.models.tables import Band


# Genre Delete
@app.route("/genre-delete/<string:id>")
def genre_delete(id):
    genre = Genre.query.filter_by(id=id).first()

    # Excluding all bands associated with a genre
    bands = Band.query.all()
    for band in bands:
        if(band.id_genre == id):
            db.session.delete(band)

    # Deleting in the database
    db.session.delete(genre)
    db.session.commit()
    genres = Genre.query.all()
    return redirect(url_for('genres_list'))


# Métodos e rotas necessárias para a exclusão de uma Banda Musical
@app.route("/band-delete/<string:id>")
def band_delete(id):
    band = Band.query.filter_by(id=id).first()

    # Deleting in the database
    db.session.delete(band)
    db.session.commit()
    bands = Band.query.all()

    return redirect(url_for('bands_list'))