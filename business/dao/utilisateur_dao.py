import psycopg2
from Persistance_layer.db_connection import DBConnection
from persistance import Singleton


class UtilisateurDao(metaclass=Singleton):
    def add_db(self, id, name_user, password):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                insert_sql = "insert into projet2A.compte_utilisateur (ID, name_user, password) values(%s, %s, %s)"
                values = (id, name_user, password)
                cur.execute(insert_sql, values)

    def drop_id(self, id):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                delete_line = f"DELETE FROM projet2A.compte_utilisateur WHERE ID = %s;"
                cur.execute(delete_line, (id,))

    def iterer_donnees(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                get_id = f"SELECT ID FROM projet2A.compte_utilisateur;"
                cur.execute(get_id)
                id_liste = cur.fetchall()
        return [id_liste[0] for id in id_liste]

    def recuperer_utilisateur(self, id):
        # Récupère les données d'un utilisateur depuis la base de données partagée
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                get_user = f"SELECT * FROM projet2A.compte_utilisateur WHERE ID= %s;"
                cur.execute(get_user, (id,))
                user = cur.fetchall()
        return user

    def afficher_db(self):  # Affiche l'ensemble de la base de données
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                display_all = f"SELECT * FROM projet2A.compte_utilisateur;"
                cur.execute(display_all)
                rows = cur.fetchall()
                for row in rows:
                    print(row)

        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                get_id = f"SELECT ID FROM projet2A.compte_utilisateur;"
                cur.execute(get_id)
                id_liste = cur.fetchall()
        return [id_liste[0] for id in id_liste]

    def verif_connexion(
        self, identifiant, mdp
    ):  # Voir comment l'ajuster avec notre DAO
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                requete = "SELECT * FROM utilisateurs WHERE identifiant=%s AND mot_de_passe=%s"
                curseur.execute(requete, (identifiant, mot_de_passe))

                # Récupérer le résultat de la requête
                utilisateur = curseur.fetchone()

                # Fermer le curseur et la connexion à la base de données
                curseur.close()
                connexion.close()

        return utilisateur

    def add_perso(  # A discuter
        self,
        id,
        nom=None,
        date_naissance=None,
        age=None,
        mail=None,
        tel=None,
        ville=None,
        code_postal=None,
    ):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                update = """UPDATE projet2A.compte_utilisateur
                SET nom=COALESCE(%s,nom), date_naissance =COALESCE(%s,date_naissance),
                    age = COALESCE(%s,age), mail = COALESCE(%s,mail),
                    tel = COALESCE(%s,tel), ville = COALESCE(%s,ville), code_postal=COALESCE(%s,code_postal)
                WHERE id = %s """
                cur.execute(
                    update,
                    (nom, date_naissance, age, mail, tel, ville, code_postal, id),
                )
