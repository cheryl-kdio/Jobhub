from business.dao.db_connection import DBConnection
from utils.singleton import Singleton

from argon2 import PasswordHasher

ph = PasswordHasher()

import getpass
import re
import string


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

    def recuperer_utilisateur(self, id):
        """
        Récupère les données d'un utilisateur depuis la base de données en utilisant son ID.

        Parameters:
            id (int): L'ID de l'utilisateur à récupérer.

        Returns:
            List[Dict[str, Any]]: Liste contenant les données de l'utilisateur.
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                get_user = f"SELECT * FROM projet2A.compte_utilisateur WHERE id_compte_utilisateur= %s;"
                cur.execute(get_user, (id,))
                user = cur.fetchall()
        return user

    def verif_connexion(self, mail, passw):
        """
        Vérifie la connexion de l'utilisateur en vérifiant son mot de passe.

        Parameters:
            mail (str): L'adresse e-mail de l'utilisateur.

        Returns:
            bool: True si la connexion est réussie, False sinon.
        """
        mail_exist = UtilisateurDao().check_mail(mail)
        if not mail_exist:
            mdp_db_salt = UtilisateurDao().get_salt_mdp(mail)
            salt_db = mdp_db_salt["sel"]
            mdp_db = mdp_db_salt["mdp"]

            try:
                ph.verify(mdp_db, salt_db + passw)
                print("Le mot de passe est valide.")
                return True
            except:
                print("Le mot de passe est invalide.")
                return False
        else:
            print("L'adresse mail est invalide")
            return False

    def update_user_info(self, id, field, new_value):
        """
        Met à jour les informations de l'utilisateur dans la base de données.

        Parameters:
            id (int): L'ID de l'utilisateur à mettre à jour.
            field (str): Le champ à mettre à jour.
            new_value: La nouvelle valeur du champ.
        """
        allowed_fields = ["nom", "age", "mail", "tel", "ville", "code_postal"]

        if field not in allowed_fields:
            print("Champ non autorisé.")
            return

        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                update_query = f"""
                    UPDATE projet2A.compte_utilisateur
                    SET {field} = %s
                    WHERE id_compte_utilisateur = %s
                """

                cur.execute(update_query, (new_value, id))

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

    def check_email_valide(self, mail):
        if not mail or not re.match(
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", mail
        ):
            return False
        else:
            return True

    def check_email_unique(self, mail):
        if not UtilisateurDao.check_mail(self, mail=mail):
            return False
        else:
            return True

    def check_mdp_valide(self, mdp):
        if (
            not len(mdp) >= 6
            or not any(c.isupper() for c in mdp)
            or not any(c.isdigit() for c in mdp)
        ):
            return False
        else:
            return True

    def check_mdp_egal(self, mdp, mdp_to_check):
        try:
            ph.verify(mdp, mdp_to_check)
            return True
        except:
            return False
