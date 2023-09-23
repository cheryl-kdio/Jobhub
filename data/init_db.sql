DROP SCHEMA IF EXISTS projet2A CASCADE;
CREATE SCHEMA projet2A;

-----------------------------------------------------
-- Compte utilisateur
-----------------------------------------------------
DROP TABLE IF EXISTS projet2A.compte_utilisateur CASCADE ;

CREATE TABLE projet2A.compte_utilisateur (
    id_compte_utilisateur SERIAL PRIMARY KEY,
    mdp VARCHAR(255),
    nom VARCHAR(255),
    age INTEGER,
    mail VARCHAR(255), 
    tel BIGINT,
    ville VARCHAR(255), 
    code_postal INT
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
