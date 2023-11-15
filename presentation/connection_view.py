from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.services.utilisateur_service import (
    Utilisateur,
)  # Importation de la classe Utilisateur depuis le module utilisateur_service
from business.dao.utilisateur_dao import UtilisateurDao
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService
from tabulate import tabulate
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from business.client.profil_chercheur_emploi import ProfilChercheurEmploi
from business.dao.recherche_dao import RechercheDao
from business.client.compte_utilisateur import CompteUtilisateur

from InquirerPy import prompt


class ConnexionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "mail",
                "message": "Votre adresse mail :",
            },
            {
                "type": "password",
                "name": "mdp",
                "message": "Votre mot de passe : ",
            },
        ]

    def make_choice(self):
        answers = prompt(self.__questions)
        u = Utilisateur()
        compte_utilisateur = u.se_connecter(
            answers["mail"],
            answers["mdp"],
        )

        if compte_utilisateur:
            print("Connexion réussie, bienvenue ", compte_utilisateur.nom)
            from presentation.user_view import UserView

            return UserView(compte_utilisateur)
        else:
            print("email ou mot de passe incorrect.")

    def display_info(self):
        print("Veuillez entrer les informations suivantes :")
