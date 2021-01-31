DROP DATABASE IF EXISTS med_center;
CREATE DATABASE med_center;

\c med_center
CREATE TABLE employed_docs
(
    id SERIAL PRIMARY KEY,
    doc_name TEXT NOT NULL,
    specialty TEXT NOT NULL,
    dept TEXT NOT NULL
);

CREATE TABLE patient_info
(
    id SERIAL PRIMARY KEY,
    patient_name TEXT NOT NULL,
    phone_num TEXT NOT NULL,
    p_address TEXT NOT NULL
);

CREATE TABLE disease_code
(
    id SERIAL PRIMARY KEY,
    disease_name TEXT NOT NULL,
    treatment TEXT NOT NULL
);

CREATE TABLE patient_diagnosis
(
    id SERIAL PRIMARY KEY,
    d_id INTEGER REFERENCES disease_code,
    p_id INTEGER REFERENCES patient_info,
    doc_id INTEGER REFERENCES employed_docs
);

INSERT INTO employed_docs (doc_name, specialty, dept) VALUES 
('Kevin', 'Cardiology', 'heart'),
('Mike', 'Oncology', 'cancer'),
('Sally', 'Dermatology', 'Skin'),
('Nancy', 'ENT', 'eye and throat'),
('Steve', 'Orthodontics', 'mouth');

INSERT INTO patient_info (patient_name, phone_num, p_address) VALUES 
('Kelly', '123-321-1231', '123 Octavia St.'),
('Michelle', '321-123-3212', '678 Orange St.'),
('Samuel', '123-321-1213', '453 Taraval St.'),
('Nathan', '213-213-2133', '372 4th Ave.'),
('Stella', '213-213-3232', '7890 11th Ave.');

INSERT INTO disease_code (disease_name, treatment) VALUES
('heartache', 'chocolate'),
('crooked tooth', 'braces'),
('tooth pain', 'tooth removal'),
('cavity', 'teeth drilling'),
('ear pain', 'ear ointment'),
('throat pain', 'medicinal syrup'),
('gamma radiation', 'therapy'),
('cancer', 'dialysis'),
('skin scrape', 'bandaid'),
('mole', 'removal');
