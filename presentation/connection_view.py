from InquirerPy import prompt
from utils.countdown_timer import countdown_timer
from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.services.utilisateur_service import Utilisateur
from business.dao.utilisateur_dao import UtilisateurDao
from business.business_object.compte_utilisateur import CompteUtilisateur

from InquirerPy import prompt


class ConnexionView(AbstractView):
    def __init__(self, langue):
        self.langue = langue
        self.__questions = [
            {
                "type": "input",
                "name": "mail",
                "message": (
                    "Your email address:"
                    if self.langue == "anglais"
                    else "Votre adresse mail :"
                ),
            },
            {
                "type": "password",
                "name": "mdp",
                "message": (
                    "Your password:"
                    if self.langue == "anglais"
                    else "Votre mot de passe :"
                ),
            },
        ]

    def make_choice(self):
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            answers = prompt(self.__questions)
            u = Utilisateur()
            compte_utilisateur = u.se_connecter(
                answers["mail"],
                answers["mdp"],
            )

            if compte_utilisateur:
                from presentation.user_view import UserView

                return UserView(user=compte_utilisateur, langue=self.langue)
            else:
                if self.langue == "français":
                    print(
                        "Identifiant ou mot de passe incorrect. Vous avez encore",
                        max_attempts - attempts - 1,
                        "tentatives.\n",
                    )
                elif self.langue == "anglais":
                    print(
                        "Incorrect username or password. You have",
                        max_attempts - attempts - 1,
                        "attempts remaining.\n",
                    )
                attempts += 1

        if self.langue == "français":
            print(
                "\n Trop de tentatives infructueuses. La connexion est bloquée. \n Veuillez attendre 5 secondes avant de tenter de vous reconnecter!\n"
            )
        elif self.langue == "anglais":
            print(
                "Too many unsuccessful attempts. Connection blocked. Wait 5 seconds to reconnect !\n"
            )

        countdown_timer(5)
        from presentation.start_view import StartView

        return StartView(self.langue)

    def display_info(self):
        if self.langue == "français":
            print("Veuillez entrer les informations suivantes :")
        elif self.langue == "anglais":
            print("Please enter the following information: :")
