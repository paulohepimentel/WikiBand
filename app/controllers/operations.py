from flask import render_template, request, flash
from app import app, db

# Application Tables
from app.models.tables import Genre
from app.models.tables import Band


# Bands by Genre
@app.route("/bands-by-genre", methods=['GET', 'POST'])
def bands_by_genre():
    genres = Genre.query.all()
    bands = Band.query.all()
    
    if request.method == 'POST':
        name_genre = request.form.get("name_genre")
        genre = Genre.query.filter_by(name=name_genre).first()
        bands = Band.query.filter_by(id_genre=genre.id).all()

        if(bands == None):
            flash('OOPS! Não existe que pertence a esse gênero!')
        return render_template("operations/list_bands_by_genre.html", genres=genres, bands=bands)
    return render_template("operations/bands_by_genre.html", genres=genres, bands=bands)


# Auxiliary method to create a country dictionary
def dict_countries():
    bands = Band.query.all()
    countries = {}
    for band in bands:
        country = band.country_of_origin
        if country not in countries:
            countries[country] = 1
        else:
            countries[country] += 1
    return countries


# Bands by Country
@app.route("/bands-by-country", methods=['GET', 'POST'])
def bands_by_country():
    countries = dict_countries()

    if request.method == 'POST':
        print('FOI')
        country_of_origin = request.form.get("country_of_origin")
        bands = Band.query.filter_by(country_of_origin=country_of_origin).all()
        print(bands)
        return render_template("operations/list_bands_by_country.html", countries=countries, bands=bands)
    return render_template("operations/bands_by_country.html", countries=countries)


# Band counting by country
@app.route("/count-by-country")
def count_by_country():
    countries = dict_countries()
    return render_template("operations/count_by_country.html", countries=countries)