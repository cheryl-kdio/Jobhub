from InquirerPy import prompt
from presentation.abstract_view import AbstractView
from presentation.the_profil_view import TheProfileView
from presentation.recherche_view import RechercheView


class UserView(AbstractView):
    def __init__(self, user, langue):
        self.user = user
        self.langue = langue
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": (
                    f"Hello {self.user.nom}"
                    if self.langue == "anglais"
                    else f"Bonjour {self.user.nom}\n"
                ),
                "choices": [
                    "Voir son profil"
                    if self.langue == "français"
                    else "See your profile",
                    "Lancer une recherche"
                    if self.langue == "français"
                    else "Start a new search",
                    "Changer la langue"
                    if self.langue == "anglais"
                    else "Change the language",
                    "Quitter" if self.langue == "français" else "Quit",
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
        choix = reponse["choix"]

        if choix == ("Quitter" if self.langue == "français" else "Quit"):
            pass
        elif choix == (
            "Voir son profil" if self.langue == "français" else "See your profile"
        ):
            return TheProfileView(user=self.user, langue=self.langue)

        elif choix == (
            "Lancer une recherche"
            if self.langue == "français"
            else "Start a new search"
        ):
            return RechercheView(user=self.user, langue=self.langue)
        elif choix == (
            "Changer la langue" if self.langue == "anglais" else "Change the language"
        ):
            new_langue = "français" if self.langue == "anglais" else "anglais"
            return UserView(user=self.user, langue=new_langue)
