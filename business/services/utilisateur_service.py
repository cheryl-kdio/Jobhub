from business.dao.utilisateur_dao import UtilisateurDao


from getpass import getpass
from argon2 import PasswordHasher

ph = PasswordHasher()


class Utilisateur(UtilisateurDao):  # Création classe Utilisateur
    def create_account(self):  # Création de la fonction créer un compte
        name_user = input("nom utilisateur :")
        mail = input("Adresse e_mail")
        passw = getpass("Mot de passe : ")
        password = ph.hash(passw)

        password_to_check = getpass("Vérification du mot de passe : ")
        try:
            ph.verify(password, password_to_check)
            print("Le mot de passe est valide.")
        except:
            print("Le mot de passe est invalide.")

        UtilisateurDao().add_db(
            id, name_user, mail, password
        )  # Ajout de l'utilisateur à notre stockage

    def se_connecter(self):  # Voir comment l'ajuster avec notre
        try:
            # Demander à l'utilisateur de saisir son identifiant et son mot de passe
            mail = input("Adresse e-mail : ")

            utilisateur = UtilisateurDao().verif_connexion(mail=mail)

            # Vérifier si l'utilisateur a été trouvé dans la base de données
            if utilisateur is not None:
                print(
                    "Connexion réussie ! Bienvenue,", utilisateur[1]
                )  # Supposons que le nom de l'utilisateur est dans la deuxième colonne
            else:
                print("Identifiant ou mot de passe incorrect. Veuillez réessayer.")

        except Exception as e:
            print("Erreur lors de la connexion à la base de données :", e)


# Appeler la fonction se_connecter
if __name__ == "__main__":
    u1 = Utilisateur()
    u1.create_account()

    UtilisateurDao().afficher_db()
