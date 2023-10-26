DROP SCHEMA IF EXISTS projet2A CASCADE;
CREATE SCHEMA projet2A;

-----------------------------------------------------
-- Compte utilisateur
-----------------------------------------------------
DROP TABLE IF EXISTS projet2A.compte_utilisateur CASCADE ;

CREATE TABLE projet2A.compte_utilisateur (
    id_compte_utilisateur SERIAL PRIMARY KEY,
    nom VARCHAR(255),
    mail VARCHAR(255),
    mdp VARCHAR(255),
    age INTEGER,
    tel BIGINT,
    ville VARCHAR(255), 
    code_postal INT,
    sel VARCHAR(255)
);


-----------------------------------------------------
-- Recherche
-----------------------------------------------------
DROP TABLE IF EXISTS projet2A.recherche CASCADE ;

CREATE TABLE projet2A.recherche (
    id SERIAL PRIMARY KEY,
    requete VARCHAR(255),
    reponse TEXT,
    utilisateur_id INT,
    FOREIGN KEY (utilisateur_id) REFERENCES projet2A.compte_utilisateur(id_compte_utilisateur)
);

-----------------------------------------------------
-- Offres
-----------------------------------------------------
DROP TABLE IF EXISTS projet2A.offre CASCADE ;

CREATE TABLE projet2A.offre (
    id_offre SERIAL PRIMARY KEY,
    titre VARCHAR(255),
    domaine VARCHAR(255),
    lieu VARCHAR(255), 
    type_contrat VARCHAR(255),
    lien_offre VARCHAR(255),
    salaire_minimum INTEGER,
    etre_en_favoris BOOLEAN,
    utilisateur_id INT,
    FOREIGN KEY (utilisateur_id) REFERENCES projet2A.compte_utilisateur(id_compte_utilisateur)
);
-- A completer avec les autres tables