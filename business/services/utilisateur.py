from abc import ABC, abstractmethod
from random import randint
from Persistance_layer.memory_id import Memory


class Utilisateur(Memory):  # Création classe Utilisateur
    def create_account(self):  # Création de la fonction créer un compte
        id = randint(0, 999999999999)  # Attribution ID interne
        while (
            id in Memory().iterer_donnees()
        ):  # Verif ID n'existe pas déjà dans notre stockage
            id = randint(0, 999999999999)

        name_user = input("nom utilisateur :")
        password = "a"
        password2 = "b"
        while password != password2:
            password = input("mot de passe :")
            password2 = input("confirmation du mot de passe :")

        Memory().add_db(
            id, [name_user, password]
        )  # Ajout de l'utilisateur à notre stockage


u1 = Utilisateur()
u2 = Utilisateur()
u1.create_account()
u2.create_account()

Memory().afficher_db()
