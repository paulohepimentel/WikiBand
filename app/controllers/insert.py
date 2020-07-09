from flask import render_template, request, flash
from app import app, db

# Application Tables
from app.models.tables import Genre
from app.models.tables import Band

# Genre Insertion
@app.route("/add-genre", methods=['GET', 'POST'])
def add_genre():
    sucess = None
    if request.method == 'POST':
        id = request.form.get("id")
        name = request.form.get("name")

        # Parameter correction
        id = id.upper()
        name = name.title()

        id_inserted = Genre.query.filter_by(id=id).first()        
        name_inserted = Genre.query.filter_by(name=name).first()

        if(id_inserted is None) and (name_inserted is None):
            new_genre = Genre(id, name)

            # Storing in the database
            db.session.add(new_genre)
            db.session.commit()
            flash('SUCESSO! Um novo gênero musical foi cadastrado!')
            sucess = True
        else:
            if(id_inserted is not None):
                flash('ERRO! Esse ID já está cadastrado!')
            if(name_inserted is not None):
                flash('ERRO! Esse nome já está cadastrado!')
            sucess = False
    return render_template("insert/genre.html", sucess=sucess)


# Band Insertion
@app.route("/add-band", methods=['GET', 'POST'])
def add_band():
    sucess = None
    # List of registered genres
    genres = Genre.query.all()

    if request.method == 'POST':
        id = request.form.get("id")
        name = request.form.get("name")
        country_of_origin = request.form.get("country_of_origin")
        name_genre = request.form.get("name_genre")

        # Parameter correction
        id = id.upper()
        name = name.title()
        country_of_origin = country_of_origin.title()
        name_genre = name_genre.title()

        id_inserted = Band.query.filter_by(id=id).first()
        name_inserted = Band.query.filter_by(name=name).first()
        genre = Genre.query.filter_by(name=name_genre).first()

        if(id_inserted is None) and (name_inserted is None):
            new_band = Band(id, name, country_of_origin, genre.id)

            # Storing in the database
            db.session.add(new_band)
            db.session.commit()
            flash('SUCESSO! Uma nova banda musical foi cadastrada!')
            sucess = True
        else:
            if(id_inserted is not None):
                flash('ERRO! Esse ID já está cadastrado!')
            if(name_inserted is not None):
                flash('ERRO! Esse nome já está cadastrado!')
            sucess = False
    return render_template("insert/band.html", genres=genres, sucess=sucess)