from InquirerPy import prompt
from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.dao.recherche_dao import (
    RechercheDao,
)  # Importing the module at the beginning


class RechercheView(AbstractView):
    def __init__(self, user):
        self.user = user
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour {Session().user_name}",
                "choices": [
                    "Supprimer des recherches sauvegardées",
                    "Retour",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        pced = RechercheDao()
        pce = pced.voir_favoris(self.user)
        if not pce:  # Use if not pce instead of pce == []
            print("Vous n'avez pas enregistré de recherche")
            print("Remplissons le ! :")
        else:
            recherche = pce

        for item in recherche:
            what = item.get("what", "N/A")
            where = item.get("where", "N/A")
            print("Intitulé:", what)  # Use what instead of item.get("what", "N/A")
            print("Lieu:", where)  # Use where instead of item.get("where", "N/A")
            print("===")

        input("Appuyez sur Entrée pour continuer")
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

        return recherche

    def make_choice(self):
        re = self.display_info()
        reponse = prompt(self.__questions)

        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Supprimer des recherches sauvegardées":
            question = prompt(
                [
                    {
                        "type": "list",
                        "message": "Choisissez une recherche sauvegardée à supprimer :",
                        "choices": [
                            item["what"] for item in re
                        ],  # Use a list comprehension
                    }
                ]
            )
            if question[0] == "Retour":  # Change "retour" to "Retour"
                from presentation.user_view import UserView

                return UserView(self.user)
            else:
                RechercheDao().supprimer_recherche(question[0], self.user)

        elif reponse["choix"] == "Retour":
            from presentation.user_view import UserView

            return UserView(self.user)

            return CreateAccountView()

        else:
            print(answers[0])
            utiliser_recherche = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "oui",
                        "message": "Lancer une recherche",
                        "default": False,
                    }
                ]
            )
            if q["oui"]:  # Change q["Oui"] to q["oui"]
                from presentation.recherche_view import RechercheView

                return RechercheView(self.user)
            else:
                from presentation.user_view import UserView

                return UserView(self.user)
