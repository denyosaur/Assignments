DROP DATABASE IF EXISTS craigslist;
CREATE DATABASE craigslist;

\c craigslist

CREATE TABLE category
(
    id SERIAL PRIMARY KEY,
    category TEXT NOT NULL
);

CREATE TABLE location_info
(
    id SERIAL PRIMARY KEY,
    location_name TEXT NOT NULL
);

CREATE TABLE user_info
(
    id SERIAL PRIMARY KEY,
    user_email TEXT NOT NULL,
    location_id INTEGER REFERENCES location_info
);
CREATE TABLE post_info
(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    text_info TEXT,
    user_info_id INTEGER REFERENCES user_info,
    category_id INTEGER REFERENCES category,
    location_id INTEGER REFERENCES location_info
);

INSERT INTO category (category)
VALUES 
('houses'),
('toys'),
('games'),
('furniture'),
('jobs'),
('cars'),
('free stuff');

INSERT INTO location_info (location_name)
VALUES
('San Francisco'),
('Seattle'),
('Los Angeles'),
('New York'),
('Salt Lake City'),
('Las Vegas'),
('San Diego'),
('Reno');

INSERT INTO user_info (user_email, location_id)
VALUES 
('qwert@gmail.com', 1),
('asdfg@yahoo.com', 3),
('fakeemail@aol.com', 4),
('mnbv@gmail.com', 3),
('asldfk@yahoo.com', 5),
('iuahsd@hotmail.com', 8),
('dfsggsd@gmail.com', 2),
('zxcxcxcvbvmn@gmail.com', 1),
('poiyiuo@gmail.com', 4),
('zxcvmasn@gmail.com', 2),
('wrtiuy@gmail.com', 7),
('qrwewer@gmail.com', 6);

INSERT INTO post_info (title, text_info, user_info_id, category_id, location_id)
VALUES
('video games $5', 'video games for sale infor here', 3, 3, 4),
('chairs $500', 'chairs for sale. 5 chairs', 6, 4, 8),
('apartment $1500', 'apt for rent. 2 beds', 7, 1, 2);