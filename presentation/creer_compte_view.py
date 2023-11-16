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

from InquirerPy import prompt


class CreateAccountView(AbstractView):
    def __init__(self):
        utilisateurdao = UtilisateurDao()
        self.__questions = [
            {
                "type": "input",
                "name": "nom",
                "message": "Votre nom : ",
            },
            {
                "type": "input",
                "name": "mail",
                "message": "Votre adresse mail :",
                "validate": lambda email: utilisateurdao.check_email_valide(email)
                and utilisateurdao.check_email_unique(email),
                "invalid_message": "Adresse e-mail invalide ou déjà existante.",
            },
            {
                "type": "password",
                "name": "mdp",
                "message": "Votre mot de passe : ",
                "validate": lambda mdp: utilisateurdao.check_mdp_valide(mdp),
                "invalid_message": "Le mot de passe ne remplit pas les conditions.",
            },
            {
                "type": "password",
                "name": "mdp_check",
                "message": "Vérifier votre mot de passe : ",
                "validate": lambda mdp_check: utilisateurdao.check_mdp_valide(mdp_check),
                "invalid_message": "Le mot de passe ne remplit pas les conditions.",
            },
            {
                "type": "password",
                "name": "mdp_confirmation",
                "message": "Confirmez votre mot de passe : ",
            },
        ]

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            if answers["mdp"] == answers["mdp_confirmation"]:
                break
            else:
                print("Les mots de passe ne correspondent pas. Veuillez réessayer.")

        u = Utilisateur()
        u.create_account(
            answers["nom"], answers["mail"], answers["mdp"], answers["mdp_confirmation"]
        )
        print("Compte créé avec succès !")
        Session().user_name = answers["nom"]
        from presentation.start_view import StartView

        return StartView()

    def display_info(self):
        print("Veuillez entrer les informations suivantes :")
