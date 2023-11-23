from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class StartView(AbstractView):
    def __init__(self, langue="français"):
        self.langue = langue
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": (
                    f"Bonjour {Session().user_name}"
                    if self.langue == "français"
                    else f"Hello {Session().user_name}"
                ),
                "choices": [
                    [
                        "Se connecter",
                        "Créer un compte",
                        "Lancer une recherche",
                        "Change the tongue",
                        "Quitter",
                    ],
                    [
                        "Log in",
                        "Create an account",
                        "Start a search",
                        "Changer la langue",
                        "Quit",
                    ],
                ][self.langue == "anglais"],
            }
        ]

    def display_info(self):
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter" or reponse["choix"] == "Quit":
            pass

        elif reponse["choix"] == "Se connecter":
            from presentation.connection_view import ConnexionView

            return ConnexionView(langue=self.langue)

        elif (
            reponse["choix"] == "Lancer une recherche"
            or reponse["choix"] == "Start a research"
        ):
            from presentation.recherche_view import RechercheView

            return RechercheView(langue=self.langue)

        elif (
            reponse["choix"] == "Créer un compte"
            or reponse["choix"] == "Create an account"
        ):
            from presentation.creer_compte_view import CreateAccountView

            return CreateAccountView(langue=self.langue)

        elif reponse["choix"] == "Change the tongue":
            question = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "Choose the tongue",
                    "choices": [
                        "Français",
                        "English",
                    ],
                }
            ]
            answer = prompt(question)["choix"]
            if answer == "Français":
                from presentation.start_view import StartView

                return StartView("français")

            elif answer == "English":
                from presentation.start_view import StartView

                return StartView(langue="anglais")

        elif reponse["choix"] == "Changer la langue":
            question = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "Choisissez la langue",
                    "choices": [
                        "Français",
                        "English",
                    ],
                }
            ]
            answer = prompt(question)["choix"]
            if answer == "Français":
                from presentation.start_view import StartView

                return StartView("français")

            elif answer == "English":
                from presentation.start_view import StartView

                return StartView(langue="anglais")
