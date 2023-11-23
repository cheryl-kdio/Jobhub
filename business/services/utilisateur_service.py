from business.dao.utilisateur_dao import UtilisateurDao
from business.client.compte_utilisateur import CompteUtilisateur

from getpass import getpass
from argon2 import PasswordHasher

ph = PasswordHasher()
import random
import string
import re


class Utilisateur(UtilisateurDao):
    def create_account(self, nom, mail, mdp, mdp_verif):
        """
        Création d'un compte et ajout d'un utilisateur à la base de données

        Parameters:
        -----------

        Returns :
        ----------

        """
        name_user = nom
        sel = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(16)
        )

        mot_de_passe_concatene = sel + mdp

        password = ph.hash(mot_de_passe_concatene)

        UtilisateurDao().add_db(name_user, mail, password, sel)

    def se_connecter(self, mail, passw):
        """Permet à un utilisateur de se connecter en saisissant son adresse e-mail et son mot de passe.

        Returns:
            CompteUtilisateur: Un objet CompteUtilisateur contenant les informations de l'utilisateur
                              connecté si la connexion réussit. None sinon.
        """

        utilisateur = UtilisateurDao().verif_connexion(mail=mail, passw=passw)

        if utilisateur:
            name = UtilisateurDao.get_value_from_mail(self, mail=mail, value="nom")
            CompteUtilisateur._connexion = True
            CompteUtilisateur.id = UtilisateurDao.get_value_from_mail(
                self, mail=mail, value="id_compte_utilisateur"
            )
            CompteUtilisateur.nom = UtilisateurDao.get_value_from_mail(
                self, mail=mail, value="nom"
            )
            CompteUtilisateur.age = UtilisateurDao.get_value_from_mail(
                self, mail=mail, value="age"
            )
            CompteUtilisateur.code_postal = UtilisateurDao.get_value_from_mail(
                self, mail=mail, value="code_postal"
            )
            CompteUtilisateur.tel = UtilisateurDao.get_value_from_mail(
                self, mail=mail, value="tel"
            )
            CompteUtilisateur.ville = UtilisateurDao.get_value_from_mail(
                self, mail=mail, value="ville"
            )
            CompteUtilisateur.mail = mail
            return CompteUtilisateur
        else:
            return None


# Appeler la fonction se_connecter
if __name__ == "__main__":
    # u1 = Utilisateur()
    # u3 = u1.create_account(
    #    nom="tom",
    #    mail="tom.t@gmail.com",
    #    mdp="Tom0001",
    #    mdp_verif="Tom0001",
    # )
    # CompteUtilisateurService().deconnexion(u3)

    # CompteUtilisateurService().modifierInfo(u3, mail="pascal@gmail")
    # UtilisateurDao().afficher_db()
    Utilisateur().update_user_info(2, "nom", "Benoit")
    UtilisateurDao().afficher_db()
    # print(UtilisateurDao().recuperer_utilisateur(3))
