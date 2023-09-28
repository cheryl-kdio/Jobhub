from abc import ABC, abstractmethod
from random import randint
from Persistance_layer.memory_id import Memory

from getpass import getpass
from argon2 import PasswordHasher

ph = PasswordHasher()


class Utilisateur(Memory):  # Création classe Utilisateur
    def create_account(self):  # Création de la fonction créer un compte
        id = randint(0, 9999999)  # Attribution ID interne
        while (
            id in Memory().iterer_donnees()
        ):  # Verif ID n'existe pas déjà dans notre stockage
            id = randint(0, 9999999)

        name_user = input("nom utilisateur :")
        passw = getpass("Mot de passe : ")
        password = ph.hash(passw)

        password_to_check = getpass("Vérification du mot de passe : ")
        try:
            ph.verify(password, password_to_check)
            print("Le mot de passe est valide.")
        except:
            print("Le mot de passe est invalide.")

        Memory().add_db(
            id, name_user, password
        )  # Ajout de l'utilisateur à notre stockage

    def se_connecter(self):
        try:
            # Connexion à la base de données PostgreSQL
            connexion = psycopg2.connect(
                database="votre_base_de_donnees",
                user="votre_utilisateur",
                password="votre_mot_de_passe",
                host="votre_hôte",
                port="votre_port",
            )

            # Création d'un curseur pour exécuter des requêtes SQL
            curseur = connexion.cursor()

            # Demander à l'utilisateur de saisir son identifiant et son mot de passe
            identifiant = input("Identifiant : ")
            mot_de_passe = input("Mot de passe : ")

            # Requête SQL pour vérifier les informations de connexion
            requete = (
                "SELECT * FROM utilisateurs WHERE identifiant=%s AND mot_de_passe=%s"
            )
            curseur.execute(requete, (identifiant, mot_de_passe))

            # Récupérer le résultat de la requête
            utilisateur = curseur.fetchone()

            # Fermer le curseur et la connexion à la base de données
            curseur.close()
            connexion.close()

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
    se_connecter()


u1 = Utilisateur()
u1.create_account()

Memory().drop_id(8786055)

Memory().afficher_db()
