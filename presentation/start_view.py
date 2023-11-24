from InquirerPy import prompt
from presentation.abstract_view import AbstractView
from presentation.session import Session
from presentation.connection_view import ConnexionView
from presentation.recherche_view import RechercheView
from presentation.creer_compte_view import CreateAccountView

class StartView(AbstractView):
    def __init__(self, langue="français", query_params=None):
        self.langue = langue
        self.query_params = query_params
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
                    "Se connecter" if self.langue == "français" else "Log in",
                    "Créer un compte" if self.langue == "français" else "Create an account",
                    "Lancer une recherche" if self.langue == "français" else "Start a search",
                    "Change the tongue" if self.langue == "français" else "Changer la langue",
                    "Quitter" if self.langue == "français" else "Quit",
                ],
            }
        ]

    def display_info(self):
        with open("presentation/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        choix = reponse["choix"]

        if choix in ["Quitter", "Quit"]:
            pass
        elif choix in ["Se connecter", "Log in"]:
            return ConnexionView(langue=self.langue)
        elif choix in ["Lancer une recherche", "Start a search"]:
            return RechercheView(langue=self.langue, query_params=self.query_params)
        elif choix in ["Créer un compte", "Create an account"]:
            return CreateAccountView(langue=self.langue)
        elif choix == "Change the tongue" or choix == "Changer la langue":
            question = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "Choose the tongue" if self.langue == "français" else "Choisissez la langue",
                    "choices": ["Français", "English"],
                }
            ]
            answer = prompt(question)["choix"]
            return StartView("français") if answer == "Français" else StartView(langue="anglais")
