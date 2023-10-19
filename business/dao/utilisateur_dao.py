import psycopg2
from business.dao.db_connection import DBConnection
from business.singleton import Singleton

from argon2 import PasswordHasher

ph = PasswordHasher()

from getpass import getpass


class UtilisateurDao(metaclass=Singleton):
    def add_db(self, id, name_user, mail, password):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                insert_sql = "insert into projet2A.compte_utilisateur (nom,mail, mdp) values(%s, %s, %s)"
                values = (name_user, mail, password)
                cur.execute(insert_sql, values)

    def drop_id(self, id):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                delete_line = f"DELETE FROM projet2A.compte_utilisateur WHERE id_compte_utilisateur = %s;"
                cur.execute(delete_line, (id,))

    def iterer_donnees(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                get_id = (
                    f"SELECT id_compte_utilisateur FROM projet2A.compte_utilisateur;"
                )
                cur.execute(get_id)
                id_liste = cur.fetchall()
        return [id_liste[0] for id in id_liste]

    def recuperer_utilisateur(self, id):
        # Récupère les données d'un utilisateur depuis la base de données partagée
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                get_user = f"SELECT * FROM projet2A.compte_utilisateur WHERE id_compte_utilisateur= %s;"
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
                get_id = (
                    f"SELECT id_compte_utilisateur FROM projet2A.compte_utilisateur;"
                )
                cur.execute(get_id)
                id_liste = cur.fetchall()
        return [id_liste[0] for id in id_liste]

    def verif_connexion(self, mail):  # Voir comment l'ajuster avec notre DAO
        passw = getpass("Mot de passe : ")
        password = ph.hash(passw)
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                requete = "SELECT mdp FROM projet2A.compte_utilisateur WHERE mail =%s"
                cur.execute(requete, (mail))
                mdp_to_check = cur.fetchone()

        try:
            ph.verify(password, mdp_to_check)
            print("Le mot de passe est valide.")
        except:
            print("Le mot de passe est invalide.")

    def modifier_perso(  # A discuter
        self,
        id,
        nom=None,
        age=None,
        mail=None,
        tel=None,
        ville=None,
        code_postal=None,
    ):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                update = """UPDATE projet2A.compte_utilisateur
                SET nom=COALESCE(%s,nom),
                    age = COALESCE(%s,age), mail = COALESCE(%s,mail),
                    tel = COALESCE(%s,tel), ville = COALESCE(%s,ville), code_postal=COALESCE(%s,code_postal)
                WHERE id = %s """
                cur.execute(
                    update,
                    (nom, age, mail, tel, ville, code_postal, id),
                )
