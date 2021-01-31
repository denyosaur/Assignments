-- from the terminal run:
-- psql < outer_space.sql

DROP DATABASE IF EXISTS outer_space;

CREATE DATABASE outer_space;

\c outer_space

CREATE TABLE moons
(
  id SERIAL PRIMARY KEY,
  planet_id INTEGER REFERENCES planets,
  moons TEXT
);

CREATE TABLE galaxies
(
  id SERIAL PRIMARY KEY,
  galaxy_name TEXT
);

CREATE TABLE orbits_around
(
  id SERIAL PRIMARY KEY,
  body_name TEXT
);

CREATE TABLE planets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  orbital_period_in_years FLOAT NOT NULL,
  orbits_around INTEGER REFERENCES orbits_around,
  galaxy_id INTEGER REFERENCES galaxies,
  moon_id INTEGER REFERENCES moons
);


INSERT INTO moons(planet_id, moons)
VALUES
(1, '{"The Moon"}'),
(2, '{"Phobos", "Deimos"}'),
(3, '{}'),
(4, '{"Naiad", "Thalassa", "Despina", "Galatea", "Larissa", "S/2004 N 1", "Proteus", "Triton", "Nereid", "Halimede", "Sao", "Laomedeia", "Psamathe", "Neso"}'),
(5, '{}'),
(6, '{}');

INSERT INTO galaxies(galaxy_name)
VALUES
('Milky Way');

INSERT INTO orbits_around(body_name)
VALUES
('The Sun'),
('Gliese 876'),
('Proxima Centauri');

INSERT INTO planets
  (name, orbital_period_in_years, orbits_around, galaxy, moons)
VALUES
  ('Earth', 1.00, 1, 1, 1),
  ('Mars', 1.88, 1, 1, 2),
  ('Venus', 0.62, 1, 1, 3),
  ('Neptune', 164.8, 1, 1, 4),
  ('Proxima Centauri b', 0.03, 3, 1, 5),
  ('Gliese 876 b', 0.23, 2, 1, 6);

