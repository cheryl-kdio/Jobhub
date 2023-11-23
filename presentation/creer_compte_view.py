from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.services.utilisateur_service import (
    Utilisateur,
)  # Importation de la classe Utilisateur depuis le module utilisateur_service
from business.dao.utilisateur_dao import UtilisateurDao
from business.business_object.recherche import Recherche
from business.services.recherche_service import RechercheService
from tabulate import tabulate
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from business.business_object.profil_chercheur_emploi import ProfilChercheurEmploi
from business.dao.recherche_dao import RechercheDao


class CreateAccountView(AbstractView):
    def __init__(self, langue):
        self.langue = langue
        utilisateurdao = UtilisateurDao()
        self.__questions = [
            {
                "type": "input",
                "name": "nom",
                "message": "Your name:" if self.langue == "anglais" else "Votre nom : ",
            },
            {
                "type": "input",
                "name": "mail",
                "message": (
                    "Your email address:"
                    if self.langue == "anglais"
                    else "Votre adresse mail :"
                ),
                "validate": lambda email: utilisateurdao.check_email_valide(email)
                and utilisateurdao.check_email_unique(email),
                "invalid_message": (
                    "Invalid email address or already exists."
                    if self.langue == "anglais"
                    else "Adresse e-mail invalide ou déjà existante."
                ),
            },
            {
                "type": "password",
                "name": "mdp",
                "message": (
                    "Your password:"
                    if self.langue == "anglais"
                    else "Votre mot de passe : "
                ),
                "validate": lambda mdp: utilisateurdao.check_mdp_valide(mdp),
                "invalid_message": (
                    "Password does not meet the requirements."
                    if self.langue == "anglais"
                    else "Le mot de passe ne remplit pas les conditions."
                ),
            },
            {
                "type": "password",
                "name": "mdp_check",
                "message": (
                    "Verify your password:"
                    if self.langue == "anglais"
                    else "Vérifier votre mot de passe : "
                ),
                "validate": lambda mdp_check: utilisateurdao.check_mdp_valide(
                    mdp_check
                ),
                "invalid_message": (
                    "Password does not meet the requirements."
                    if self.langue == "anglais"
                    else "Le mot de passe ne remplit pas les conditions."
                ),
            },
        ]

    def make_choice(self):
        while True:
            answers = prompt(self.__questions)
            if answers["mdp"] == answers["mdp_check"]:
                break
            else:
                print(
                    "Passwords do not match. Please try again."
                    if self.langue == "anglais"
                    else "Les mots de passe ne correspondent pas. Veuillez réessayer."
                )

        u = Utilisateur()
        u.create_account(
            answers["nom"], answers["mail"], answers["mdp"], answers["mdp_check"]
        )
        print(
            "Compte créé avec succès !"
            if self.langue == "français"
            else "Account succesfully created"
        )
        Session().user_name = answers["nom"]
        from presentation.start_view import StartView

        return StartView()

    def display_info(self):
        print(
            "Veuillez entrer les informations suivantes :"
            if self.langue == "français"
            else "Please enter the following information:"
        )
