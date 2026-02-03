
CREATE TABLE IF NOT EXISTS etablissements (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(200) NOT NULL,
    type VARCHAR(50), 
    localisation VARCHAR(100), 
    site_web VARCHAR(255),
    description TEXT,
    contact VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS filieres (
    id_filiere SERIAL PRIMARY KEY,
    id_etablissement INTEGER REFERENCES etablissements(id) ON DELETE CASCADE,
    nom_filiere VARCHAR(255) NOT NULL,
    description TEXT,
    coefficient_base FLOAT DEFAULT 1.0,
    moyenne_min FLOAT, 
    frais_scolarite FLOAT 
);


CREATE TABLE IF NOT EXISTS bacheliers (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    telephone VARCHAR(20),
    serie_bac VARCHAR(10), 
    moyenne_bac FLOAT CHECK (moyenne_bac >= 0 AND moyenne_bac <= 20),
    budget_max FLOAT
);


INSERT INTO etablissements (nom, type, localisation, site_web) VALUES
('EPL (Polytechnique)', 'Ecole', 'Lomé (Adidogomé)', 'https://epl.univ-lome.tg'),
('ENSI', 'Ecole', 'Lomé (Université)', 'https://ensi.univ-lome.tg'),
('Université de Kara', 'Université', 'Kara', 'https://univ-kara.tg');

INSERT INTO filieres (id_etablissement, nom_filiere, moyenne_min, frais_scolarite) VALUES
(1, 'Génie Logiciel', 14.0, 500000),
(1, 'Génie Civil', 13.5, 500000),
(2, 'Génie Électrique', 13.0, 450000),
(3, 'Droit', 10.0, 150000);