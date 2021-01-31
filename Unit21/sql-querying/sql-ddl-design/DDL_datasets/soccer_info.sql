DROP DATABASE IF EXISTS soccer_match;
CREATE DATABASE soccer_match;

\c soccer_match

CREATE TABLE teams
(
    id SERIAL PRIMARY KEY,
    team_name TEXT NOT NULL,
    standing INTEGER NOT NULL
);

CREATE TABLE player
(
    id SERIAL PRIMARY KEY,
    player_name TEXT NOT NULL,
    team_id INTEGER REFERENCES teams
);

CREATE TABLE referee
(
    id SERIAL PRIMARY KEY,
    ref_name TEXT NOT NULL
);

CREATE TABLE season_info
(
    id SERIAL PRIMARY KEY,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL
);

CREATE TABLE match_info
(
    id SERIAL PRIMARY KEY,
    team1_id INTEGER REFERENCES teams,
    team2_id INTEGER REFERENCES teams,
    ref1_id INTEGER REFERENCES referee,
    ref2_id INTEGER REFERENCES referee,
    ref3_id INTEGER REFERENCES referee,
    season_id INTEGER REFERENCES season_info
);

CREATE TABLE match_details
(
    id SERIAL PRIMARY KEY,
    match_id INTEGER REFERENCES match_info,
    player_id INTEGER REFERENCES player,
    goals INTEGER
);

INSERT INTO teams (team_name, standing)
VALUES
('Lakers', 2),
('Dodgers', 3),
('Red Sox', 1),
('Mighty Ducks', 4),
('Giants', 7),
('Packers', 6),
('Tiger Woods', 5);

INSERT INTO player (player_name, team_id)
VALUES
('Mike', 4),
('Jordan', 6),
('Frank', 2),
('Steve', 1),
('Sally', 3),
('Harry', 5),
('Hermoine', 7),
('Ron', 7),
('Shneebly', 5),
('Gary', 3),
('Ash', 1),
('Oak', 2),
('Will', 4),
('Hannibal', 6);

INSERT INTO referee (ref_name)
VALUES
('Homer'),
('Marge'),
('Bart'),
('Lisa'),
('Cartman'),
('Kenny');

INSERT INTO season_info (start_date, end_date)
VALUES 
('03/01/2020', '06/01/2020');

INSERT INTO match_info (team1_id, team2_id, ref1_id, ref2_id, ref3_id, season_id)
VALUES
(1,2,2,3,4,1),
(3,4,1,2,4,1),
(4,5,1,2,3,1),
(6,7,3,4,5,1),
(1,3,1,3,5,1),
(4,7,1,2,4,1);

INSERT INTO match_details (match_id, player_id, goals)
VALUES
(1, 2, 5),
(1, 3, 3),
(2, 5, 1),
(2, 3, 2),
(3, 7, 3),
(4, 4, 4),
(4, 1, 5),
(5, 6, 6);

