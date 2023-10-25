from business.dao.utilisateur_dao import UtilisateurDao
from business.client.compte_utilisateur import CompteUtilisateur

# from services.compte_utilisateur_service import CompteUtilisateurService


from getpass import getpass
from argon2 import PasswordHasher

ph = PasswordHasher()
import random
import string


class Utilisateur(UtilisateurDao):  # Création classe Utilisateur
    def create_account(self):  # Création de la fonction créer un compte
        name_user = input("nom utilisateur :")
        mail = input("Adresse e_mail")
        passw = getpass("Mot de passe : ")
        password_to_check = getpass("Vérification du mot de passe : ")

        sel = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(16)
        )

        mot_de_passe_concatene = sel + passw

        password = ph.hash(mot_de_passe_concatene)
        print(password)
        print(ph.hash(sel + password_to_check))

        try:
            mot_de_passe_concatene_to_check = sel + password_to_check
            ph.verify(password, mot_de_passe_concatene_to_check)
            print("Le mot de passe est valide.")
        except:
            print("Le mot de passe est invalide.")

        UtilisateurDao().add_db(
            name_user, mail, password, sel
        )  # Ajout de l'utilisateur à notre stockage

    def se_connecter(self):  # Voir comment l'ajuster avec notre
        try:
            # Demander à l'utilisateur de saisir son identifiant et son mot de passe
            mail = input("Adresse e-mail : ")

            utilisateur = UtilisateurDao().verif_connexion(mail=mail)

            # Vérifier si l'utilisateur a été trouvé dans la base de données
            if utilisateur:
                print(
                    "Connexion réussie ! Bienvenue,"
                )  # Supposons que le nom de l'utilisateur est dans la deuxième colonne
            else:
                print("Identifiant ou mot de passe incorrect. Veuillez réessayer.")

        except Exception as e:
            print("Erreur lors de la connexion à la base de données :", e)


# Appeler la fonction se_connecter
if __name__ == "__main__":
    u1 = Utilisateur()
    UtilisateurDao().drop_id(17)
    u1.se_connecter()
