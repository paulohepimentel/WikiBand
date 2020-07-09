/* SQL Methods for musical genres */
DROP TABLE IF EXISTS Genre;

CREATE TABLE Genre (
    id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL UNIQUE
);

INSERT INTO Genre (id, name) VALUES ('G00', 'Rock');
INSERT INTO Genre (id, name) VALUES ('G01', 'Pop/Rock');
INSERT INTO Genre (id, name) VALUES ('G02', 'Indie');
INSERT INTO Genre (id, name) VALUES ('G03', 'Hard Rock');
INSERT INTO Genre (id, name) VALUES ('G04', 'Power Metal');

/***************************************************************************************/

/* SQL Methods for musical bands */
DROP TABLE IF EXISTS Band;

CREATE TABLE Band (
    id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL UNIQUE,
    country_of_origin TEXT NOT NULL,
    FOREIGN KEY (id_genre) REFERENCES Genre(id)
);

/* ROCK */
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B00', 'Bon Jovi', 'Estados Unidos', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B01', 'Linkin Park', 'Estados Unidos', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B02', 'Nirvana', 'Estados Unidos', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B03', 'Red Hot Chili Peppers', 'Estados Unidos', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B04', 'Capital Inicial', 'Brasil', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B05', 'Charlie Brown Jr', 'Brasil', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B06', 'Legião Urbana', 'Brasil', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B07', 'Titãs', 'Brasil', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B08', 'Capital Inicial', 'Inglaterra', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B09', 'Queen', 'Inglaterra', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B10', 'The Beatles', 'Inglaterra', 'G00');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B11', 'U2', 'Irlanda', 'G00');
/* POP/ROCK */
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B12', 'Maroon 5', 'Estados Unidos', 'G01');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B13', 'Imagine Dragons', 'Estados Unidos', 'G01');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B14', 'Coldplay', 'Inglaterra', 'G01');
/* INDIE */
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B15', 'Foster The People', 'Estados Unidos', 'G02');
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B16', 'Kodaline', 'Irlanda', 'G02');
/* HARD ROCK */
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B17', 'Scorpions', 'Alemanha', 'G03');
/* POWER METAL */
INSERT INTO Band (id, name, country_of_origin, id_genre) VALUES ('B18', 'Helloween', 'Alemanha', 'G04');
