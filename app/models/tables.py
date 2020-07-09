from app import db

'''
Representation of a musical genre in the database
Genre: | id | name |
'''
class Genre(db.Model):
    __tablename__ = "Generos Musicais"
    id = db.Column(db.String(20), primary_key=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return (self.name)


'''
Representation of a musical band in the database
Band: | id | name | country_of_origin | id_genre (name_genre) |
'''
class Band(db.Model):
    __tablename__ = "Bandas Musicais"
    id = db.Column(db.String(20), primary_key=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False) 
    country_of_origin = db.Column(db.String(20), nullable=False)

    # Relationship with the table of musical genres
    id_genre = db.Column(db.String(20), db.ForeignKey('Generos Musicais.id'), nullable=False)
    name_genre = db.relationship('Genre', backref='Generos Musicais', lazy=True)

    def __init__(self, id, name, country_of_origin, id_genre):
        self.id = id
        self.name = name
        self.country_of_origin = country_of_origin
        self.id_genre = id_genre

    def __repr__(self):
        return (self.name)