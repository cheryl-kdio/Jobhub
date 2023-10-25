from business.dao.db_connection import DBConnection
from business.singleton import Singleton

from argon2 import PasswordHasher

ph = PasswordHasher()

from getpass import getpass


class UtilisateurDao(metaclass=Singleton):

    def add_db(self, name_user, mail, password, sel):
        """
        Ajoute un nouvel utilisateur à la base de données.

        Parameters:
            name_user (str): Le nom de l'utilisateur.
            mail (str): L'adresse e-mail de l'utilisateur.
            password (str): Le mot de passe haché de l'utilisateur.
            sel (str): Le sel utilisé pour le hachage du mot de passe.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                insert_sql = "insert into projet2A.compte_utilisateur (nom,mail, mdp, sel) values(%s, %s, %s, %s)"
                values = (name_user, mail, password, sel)
                cur.execute(insert_sql, values)

    def get_mail(self):
        """
        Récupère la liste des adresses e-mail depuis la base de données.

        Returns:
            List[str]: Liste des adresses e-mail.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                requete = f"SELECT mail FROM projet2A.compte_utilisateur;"
                cur.execute(
                    requete,
                )
                results = cur.fetchall()
                print(results)
                mails = [result["mail"] for result in results]
        return mails

    def get_salt_mdp(self, mail):
        """
        Récupère le mot de passe haché et le sel associé à une adresse e-mail donnée.

        Parameters:
            mail (str): L'adresse e-mail de l'utilisateur.

        Returns:
            Dict[str, str]: Un dictionnaire contenant le mot de passe haché et le sel.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                requete = (
                    "SELECT mdp, sel FROM projet2A.compte_utilisateur WHERE mail= %s;"
                )
                cur.execute(requete, (mail,))
                mdp_salt = cur.fetchone()
        return mdp_salt

    def get_value_from_mail(self, mail, value):
        """
        Récupère une valeur spécifique associée à une adresse e-mail donnée depuis la base de données.

        Parameters:
            mail (str): L'adresse e-mail de l'utilisateur.
            value (str): Le nom de la colonne à récupérer.

        Returns:
            Any: La valeur associée à la colonne spécifiée.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                requete = (
                    f"SELECT {value} FROM projet2A.compte_utilisateur WHERE mail = %s;"
                )
                cur.execute(requete, (mail,))
                result = cur.fetchone()
                if result:
                    return result[value]
                else:
                    return None

    def drop_id(self, id):
        """
        Supprime un utilisateur de la base de données en utilisant son ID.

        Parameters:
            id (int): L'ID de l'utilisateur à supprimer.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                delete_line = f"DELETE FROM projet2A.compte_utilisateur WHERE id_compte_utilisateur = %s;"
                cur.execute(delete_line, (id,))

    def iterer_donnees(self):
        """
        Itère à travers les ID des utilisateurs dans la base de données.

        Returns:
            List[int]: Liste des ID des utilisateurs.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                get_id = (
                    f"SELECT id_compte_utilisateur FROM projet2A.compte_utilisateur;"
                )
                cur.execute(get_id)
                id_liste = cur.fetchall()
        return [id_liste[0] for id in id_liste]

    def recuperer_utilisateur(self, id):
        """
        Récupère les données d'un utilisateur depuis la base de données en utilisant son ID.

        Parameters:
            id (int): L'ID de l'utilisateur à récupérer.

        Returns:
            List[Dict[str, Any]]: Liste contenant les données de l'utilisateur.
        """        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                get_user = f"SELECT * FROM projet2A.compte_utilisateur WHERE id_compte_utilisateur= %s;"
                cur.execute(get_user, (id,))
                user = cur.fetchall()
        return user

    def afficher_db(self):  # Affiche l'ensemble de la base de données
        """
        Affiche l'ensemble de la base de données.
        """
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
        """
        Vérifie la connexion de l'utilisateur en vérifiant son mot de passe.

        Parameters:
            mail (str): L'adresse e-mail de l'utilisateur.

        Returns:
            bool: True si la connexion est réussie, False sinon.
        """
        passw = getpass("Mot de passe : ")
        mdp_db_salt = UtilisateurDao().get_salt_mdp(mail)
        salt_db = mdp_db_salt["sel"]
        print(salt_db)
        mdp_db = mdp_db_salt["mdp"]

        try:
            ph.verify(mdp_db, salt_db + passw)
            print("Le mot de passe est valide.")
            return True
        except:
            print("Le mot de passe est invalide.")
            return False

    def update(
        self, id, nom=None, age=None, mail=None, tel=None, ville=None, code_postal=None
    ):
        """
        Met à jour les informations de l'utilisateur dans la base de données.

        Parameters:
            id (int): L'ID de l'utilisateur à mettre à jour.
            nom (str, optional): Le nouveau nom de l'utilisateur.
            age (int, optional): Le nouvel âge de l'utilisateur.
            mail (str, optional): La nouvelle adresse e-mail de l'utilisateur.
            tel (int, optional): Le nouveau numéro de téléphone de l'utilisateur.
            ville (str, optional): La nouvelle ville de résidence de l'utilisateur.
            code_postal (int, optional): Le nouveau code postal de la ville de résidence de l'utilisateur.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                update = """UPDATE projet2A.compte_utilisateur
                SET nom=COALESCE(%s,nom),
                    age = COALESCE(%s,age), mail = COALESCE(%s,mail),
                    tel = COALESCE(%s,tel), ville = COALESCE(%s,ville), code_postal=COALESCE(%s,code_postal)
                WHERE id_compte_utilisateur = %s """

                cur.execute(
                    update,
                    (nom, age, mail, tel, ville, code_postal, id),
                )

        def supprimer(self, user) -> bool:
            """Suppression d'un utilisateur dans la base de données

            Parameters
            ----------
            user : CompteUtilisateur
                utilisateur à supprimer de la base de données

            Returns
            -------
                True si l'utilisateur a bien été supprimé
            """
            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        # Supprimer le compte d'un utilisateur
                        cursor.execute(
                            "DELETE FROM projet2A.compte_utilisateur           "
                            " WHERE id_compte_utilisateur=%(id_compte_utilisateur)s      ",
                            {"id_compte_utilisateur": user.id_compte_utilisateur},
                        )
                        res = cursor.rowcount
            except Exception as e:
                print(e)
                raise

            return res > 0

    def check_mail(self, mail):
        """
        Vérifie si une adresse e-mail existe déjà dans la base de données.

        Parameters:
            mail (str): L'adresse e-mail à vérifier.

        Returns:
            bool: True si l'adresse e-mail est unique, False sinon.
        """
        try:
            if mail in self.get_mail():
                return False
            else:
                return True
        except Exception as e:
            print("Une erreur s'est produite :", str(e))
            return False
