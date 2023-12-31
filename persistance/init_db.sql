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
    sel TEXT
);


-----------------------------------------------------
-- Recherche
-----------------------------------------------------
DROP TABLE IF EXISTS projet2A.recherche CASCADE ;

CREATE TABLE projet2A.recherche (
    id_recherche SERIAL PRIMARY KEY,
    query_params VARCHAR(255),
    utilisateur_id INT,
    FOREIGN KEY (utilisateur_id) REFERENCES projet2A.compte_utilisateur(id_compte_utilisateur) ON DELETE CASCADE
);

-----------------------------------------------------
-- Offres
-----------------------------------------------------
DROP TABLE IF EXISTS projet2A.offre CASCADE ;

CREATE TABLE projet2A.offre (
    id_offre BIGINT ,
    titre VARCHAR(255),
    domaine VARCHAR(255),
    lieu VARCHAR(255), 
    type_contrat VARCHAR(255),
    lien_offre VARCHAR(255),
    salaire_minimum INTEGER,
    entreprise VARCHAR(255),
    description TEXT,
    utilisateur_id INT,
    date_ajout DATE DEFAULT CURRENT_DATE,
    candidature_envoyee BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id_offre, utilisateur_id),
    FOREIGN KEY (utilisateur_id) REFERENCES projet2A.compte_utilisateur(id_compte_utilisateur) ON DELETE CASCADE
);

-----------------------------------------------------
-- Profil chercheur d'emploi
-----------------------------------------------------
DROP TABLE IF EXISTS projet2A.profil_chercheur_emploi CASCADE ;
CREATE TABLE projet2A.profil_chercheur_emploi (
    id_profil_chercheur_emploi SERIAL PRIMARY KEY,
    nom TEXT,
    mots_cles TEXT,
    lieu VARCHAR(255),
    salaire_minimum INTEGER,
    distance INTEGER,
    type_contrat VARCHAR(255),            
    utilisateur_id INT,
    FOREIGN KEY (utilisateur_id) REFERENCES projet2A.compte_utilisateur(id_compte_utilisateur) ON DELETE CASCADE
);

