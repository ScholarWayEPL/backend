
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS etablissements (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(), -- Ton UID/TrackingId
    nom VARCHAR(200) NOT NULL,
    type VARCHAR(50), 
    localisation VARCHAR(100), 
    site_web VARCHAR(255),
    description TEXT,
    contact VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS filieres (
    id_filiere UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    id_etablissement UUID REFERENCES etablissements(id) ON DELETE CASCADE,
    nom_filiere VARCHAR(255) NOT NULL,
    description TEXT,
    coefficient_base FLOAT DEFAULT 1.0,
    moyenne_min FLOAT, 
    frais_scolarite FLOAT 
);

CREATE TABLE IF NOT EXISTS bacheliers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
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