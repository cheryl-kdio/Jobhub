from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class UserView(AbstractView):
    def __init__(self, user):
        self.user = user
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour {Session().user_name}",
                "choices": [
                    "Consulter son profil",
                    "Créer un compte",
                    "Lancer une recherche",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Consulter son profil":
            from presentation.profile_view import ProfileView

            return ProfileView()

        elif reponse["choix"] == "Lancer une recherche":
            from presentation.recherche_view import RechercheView

            return RechercheView(self.user)

        elif reponse["choix"] == "Créer un compte":
            from presentation.creer_compte_view import CreateAccountView

            return CreateAccountView()
