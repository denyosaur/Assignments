-- from the terminal run:
-- psql < music.sql

DROP DATABASE IF EXISTS music;

CREATE DATABASE music;

\c music

CREATE TABLE artists
(
  id SERIAL PRIMARY KEY,
  artists TEXT[] NOT NULL
);

CREATE TABLE albums
(
  id SERIAL PRIMARY KEY,
    album_name TEXT NOT NULL,
);

CREATE TABLE producers
(
  id SERIAL PRIMARY KEY,
  producer_name TEXT[] NOT NULL
);

CREATE TABLE songs
(
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  duration_in_seconds INTEGER NOT NULL,
  release_date DATE NOT NULL,
  artist1_id INTEGER REFERENCES artists,
  artist2_id INTEGER REFERENCES artists,
  album_id INTEGER REFERENCES album,
  producer1_id INTEGER REFERENCES producers,
  producer2_id INTEGER REFERENCES producers,
);

INSERT INTO artists(artists)
VALUES
("Hanson"),
("Queen"),
("Mariah Cary"),
("Boyz II Men"),
("Lady Gaga"),
("Bradley Cooper"),
("Nickelback"),
("Jay Z"),
("Alicia Keys"),
("Katy Perry"),
("Juicy J"),
("Maroon 5"),
("Christina Aguilera"),
("Avril Lavigne"),
("Destiny''s Child");

INSERT INTO albums(album_name)
VALUES
("Middle of Nowhere"),
("A Night at the Opera"),
("Daydream"),
("A Star Is Born"),
("Silver Side Up"),
("The Blueprint 3"),
("Prism"),
("Hands All Over"),
("Let Go"),
("The Writing''s on the Wall");

INSERT INTO producers(album_name)
VALUES
("Dust Brothers"),
("Stephen Lironi"),
("Roy Thomas Baker"),
("Walter Afanasieff"), 4
("Benjamin Rice"),
("Rick Parashar"), 6
("Al Shux"),
("Max Martin"),
("Cirkut"),
("Shellback"),10
("Benny Blanco"),
("The Matrix"),
("Darkchild");



INSERT INTO songs
  (title, duration_in_seconds, release_date, artist1, artist2, album, producers1, producers2)
VALUES
  ('MMMBop', 238, '04-15-1997', 1, NULL,  1, 1,2),
  ('Bohemian Rhapsody', 355, '10-31-1975', 2,NULL, 2, 3, NULL),
  ('One Sweet Day', 282, '11-14-1995', 3, 4, 3, 4, NULL),
  ('Shallow', 216, '09-27-2018', 5, 6, 4, 5, NULL),
  ('How You Remind Me', 223, '08-21-2001', 7, NULL, 5, 6, NULL),
  ('New York State of Mind', 276, '10-20-2009', 8, 9, 6, 7, NULL),
  ('Dark Horse', 215, '12-17-2013', 10, 11, 7, 8,9),
  ('Moves Like Jagger', 201, '06-21-2011', 12, 13, 8, 10, 11),
  ('Complicated', 244, '05-14-2002', 14, NULL, 9, 12, NULL),
  ('Say My Name', 240, '11-07-1999', 15, NULL, 10, 13, NULL);
