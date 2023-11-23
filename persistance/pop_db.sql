--- modifier avec de 'vraies' données 
---- completer avec les insertions dans les autres tables
INSERT INTO projet2A.compte_utilisateur (mdp, nom, age, mail, tel, ville, code_postal,sel)
VALUES
    ('$argon2id$v=19$m=65536,t=3,p=4$o2uZeuRofa7yQ/PPyU2/sA$SfOhgVvtruOajQpfjGX2I2D0/UF6MMxh1vD+S9O/kpk', 'Carine Koffi', 25, 'ck@gmail.com', 0626340800, 'Rennes', 35170,'xbZb3OJ5InH9buJR'),
    ('$argon2id$v=19$m=65536,t=3,p=4$1jiabcS5nMOy3VzMSLF2ug$bPvka7mUC1siWnOBiQCt86m1VRUx9GXZEaPgATweQw8','John Doe',30,'jd@yahoo.fr',0928301802,'Paris',75011,'jg0LD0XKOu45tdNy'),
    ('$argon2id$v=19$m=65536,t=3,p=4$azY5TAeh7TNey9Ximzzg3w$xqObKaU/qX6SiR2p2l2LwaCP/Bz/l8yrvaidhEgVDzw','Melissa Hougard',29,'mel@gmail.com',0689546723,'Perpignan',66100,'4YJLIMlYkIXMpnUk');


INSERT INTO projet2A.recherche (query_params, utilisateur_id)
VALUES
    ('{"results_per_page": 20, "what": "python dev"}', 1),
    ('{"results_per_page": 20, "what": "data scientist"}', 1),
    ('{"results_per_page": 20, "what": "deisgner"}', 3),
    ('{"results_per_page": 20, "what": "architecte"}', 2),
    ('{"results_per_page": 20, "what": "3d"}', 2);


INSERT INTO projet2A.offre (id_offre,titre,domaine , lieu , type_contrat ,entreprise, utilisateur_id,candidature_envoyee)
VALUES 
    (4418009682, 'Lead Dév API Python Js H/F', ' Emplois Autres/Général', 'Talence, Bordeaux ', '', 'Externatic', 1,TRUE),
    (4298646981 ,'Dev Python / react Montpellier ASAP (IT) '  ,   'Emplois Informatique' ,  'Hérault, Occitanie',' contract'  ,' WorldWide People  ',3,FALSE),   
    (4298646981 ,'Dev Python / react Montpellier ASAP (IT) '  ,   'Emplois Informatique' ,  'Hérault, Occitanie',' contract'  ,' WorldWide People  ',1,TRUE),   
    (4411217653,'Dév Python ' , 'Emplois Informatique '  ,'Saint-Cloud, Boulogne-Billancourt ','',' Extia' ,2,TRUE),
    (4426020939,'100% Télétravail - Senior Dev Python', 'Unknown','Paris, Ile-de-France','','SEPT LIEUES SAS',1,FALSE),   
    (4405757805, 'STAGE 2A - DEV PYTHON - Dashboarding Solution for CI Server & Team KPIs','Emplois Comptabilité et Finance','Paris, Ile-de-France','contract', 'Murex',2,FALSE),
    (4405757805, 'STAGE 2A - DEV PYTHON - Dashboarding Solution for CI Server & Team KPIs','Emplois Comptabilité et Finance','Paris, Ile-de-France','contract', 'Murex',3,TRUE)  ;

    


INSERT INTO projet2A.candidatures (id_offre,titre,domaine , lieu , type_contrat ,entreprise, utilisateur_id)
VALUES 
    (4426020939,'100% Télétravail - Senior Dev Python', 'Unknown','Paris, Ile-de-France','','SEPT LIEUES SAS',3),   
    (4418009682, 'Lead Dév API Python Js H/F', ' Emplois Autres/Général', 'Talence, Bordeaux ', '', 'Externatic', 1),
    (4298646981 ,'Dev Python / react Montpellier ASAP (IT) '  ,   'Emplois Informatique' ,  'Hérault, Occitanie',' contract'  ,' WorldWide People  ',1),   
    (4411217653,'Dév Python ' , 'Emplois Informatique '  ,'Saint-Cloud, Boulogne-Billancourt ','',' Extia' ,1),
    (4405757805, 'STAGE 2A - DEV PYTHON - Dashboarding Solution for CI Server & Team KPIs','Emplois Comptabilité et Finance','Paris, Ile-de-France','contract', 'Murex',2)  ;
    

INSERT INTO projet2A.profil_chercheur_emploi (nom, mots_cles, lieu, distance, type_contrat, utilisateur_id)
VALUES 
('Alerte Ingénieur Paris', 'ingénieur, développement, agile', 'Paris', 10, 'CDI', 1),
('Alerte Scientifique Lyon', 'recherche, physique, chimie', 'Lyon', 15, 'CDD', 2),
('Alerte Artiste Marseille', 'art, peinture, créativité', 'Marseille', 20, 'TEMPS PLEIN', 3),
('Alerte Écrivain Toulouse', 'écriture, philosophie, éducation', 'Toulouse', 5, 'TEMPS PARTIEL', 2),
('Alerte Biologiste Nice', 'biologie, recherche, laboratoire', 'Nice', 25, 'CDD', 1);
