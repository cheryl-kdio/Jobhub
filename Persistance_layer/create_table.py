import psycopg2

# """
# connexion = psycopg2.connect(
#    user="id2230",
#    password="id2230",
#    host="sgbd-eleves.domensai.ecole",
#    port="5432",
#    database="id2230",
# )
#
# cur = connexion.cursor()
#
# table_account = """CREATE TABLE account(
#        ID INT PRIMARY KEY NOT NULL,
#        name_user TEXT NOT NULL,
#        password TEXT NOT NULL
#      ); """
#
# cur.execute(table_account)
# connexion.commit()
# print("Table créée avec succès dans PostgreSQL")

# fermeture de la connexion à la base de données
# cur.close()
# connexion.close()
# print("La connexion PostgreSQL est fermée")

from psycopg2 import sql

# Connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    host="sgbd-eleves.domensai.ecole",
    database="id2230",
    user="id2230",
    password="id2230",
)

# Ouvrir un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Définir le nom des colonnes que vous souhaitez ajouter
nouvelles_colonnes = [("nom", "text")]

# Boucle pour ajouter chaque nouvelle colonne
for colonne, type_colonne in nouvelles_colonnes:
    ajout_colonne_sql = sql.SQL("ALTER TABLE account ADD COLUMN {} {};").format(
        sql.Identifier(colonne), sql.SQL(type_colonne)
    )
    cur.execute(ajout_colonne_sql)

# Valider les modifications et fermer la connexion
conn.commit()
cur.close()
conn.close()

print("Colonnes ajoutées avec succès.")
