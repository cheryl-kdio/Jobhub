from InquirerPy import prompt
from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.dao.recherche_dao import (
    RechercheDao,
)  # Importing the module at the beginning


class ARechercheView(AbstractView):
    def __init__(self, user, langue):
        self.user = user
        self.langue = langue
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
        redao = RechercheDao()
        pce = redao.voir_favoris(self.user)

        if not pce:
            print(
                "Vous n'avez pas de recherches sauvegardées"
                if self.langue == "français"
                else "You don't have any saved searches."
            )
            print("Remplissons-le ensemble!")

            questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": (
                        "What is your choice?"
                        if self.langue == "anglais"
                        else "Que voulez-vous faire ? :"
                    ),
                    "choices": [
                        "Retour",
                        "Quitter",
                        "Lancer une recherche",
                    ],
                }
            ]

            response = prompt(
                questions[0]
            )  # Use indexing to access the first item in the list
            if response["choix"] == "Retour":
                from presentation.user_view import UserView

                return UserView(self.user)

            elif response["choix"] == (
                "Quitter" if self.langue == "français" else "Quit"
            ):
                pass

            else:
                from presentation.afficher_recherche_favoris import ARechercheView

                return ARechercheView(self.user, self.langue)

        for item in pce:
            what = item.get("what", "N/A")
            where = item.get("where", "N/A")
            print("Intitulé:", what)
            print("Lieu:", where)
            print("===")

        return pce

    def make_choice(self):
        recherche, pce = self.display_info()
        reponse = prompt(self.__questions)

        if reponse == ("Quitter" if self.langue == "français" else "Quit"):
            pass

        elif reponse == (
            "Supprimer des recherches sauvegardées"
            if self.langue == "français"
            else "Delete an offer"
        ):
            from business.dao.recherche_dao import RechercheDao

            redao = RechercheDao()
            from business.client.recherche import Recherche

            question = [
                {
                    "type": "list",
                    "name": "recherche",
                    "message": (
                        "Choisissez la recherche à supprimer"
                        if self.langue == "français"
                        else "Choose the search to delete:"
                    ),
                    "choices": [
                        {
                            "name": f"{item['what']} - {item['where']}",
                            "value": item,
                        }
                        for item in pce
                        if isinstance(item, dict)
                    ],
                }
            ]

            recherche = prompt(question)[
                0
            ]  # Use [0] to get the first (and only) element
            selected_recherche_str = recherche["recherche"]

            selected_recherche = None
            for element in pce:
                if (
                    isinstance(element, Recherche)
                    and f"{element['what']} - {element['where']}"
                    == selected_recherche_str
                ):
                    selected_recherche = element
                    break

            with open(
                "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
            ) as asset:
                print(asset.read())

            redao.supprimer_recherche(selected_recherche)
            print(
                "L'offre a bien été supprimée"
                if self.langue == "français"
                else "The offer has been deleted"
            )
            return ARechercheView(user=self.user, langue=self.langue)

        elif reponse == "Retour":
            from presentation.user_view import UserView

            return UserView(self.user)
