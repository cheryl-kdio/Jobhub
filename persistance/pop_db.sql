--- modifier avec de 'vraies' données 
---- completer avec les insertions dans les autres tables
INSERT INTO projet2A.compte_utilisateur (mdp, nom, age, mail, tel, ville, code_postal,sel)
VALUES
    ('$argon2id$v=19$m=65536,t=3,p=4$o2uZeuRofa7yQ/PPyU2/sA$SfOhgVvtruOajQpfjGX2I2D0/UF6MMxh1vD+S9O/kpk', 'cheryl', 25, 'ck@gmail.com', 0626340800, 'Rennes', 35170,'xbZb3OJ5InH9buJR');

INSERT INTO projet2A.recherche (query_params, utilisateur_id)
VALUES
    ('{"results_per_page": 20,"what": "python dev"}', 1),
    ('{"results_per_page": 20,"what": "data scientist"}', 1);

INSERT INTO projet2A.offre (titre,
    domaine ,
    lieu , 
    type_contrat ,
    lien_offre ,
    salaire_minimum,
    entreprise,
    description, utilisateur_id)
VALUES 
    ('offre_test', 'a', 'b', 'v', 'r', 6, 'b', 8,1)
    
