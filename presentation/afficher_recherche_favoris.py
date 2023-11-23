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
        pass

    def make_choice(self):
        pced = RechercheDao()
        pce = pced.voir_favoris(self.user)
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
                        "Lancer une recherche",
                    ],
                }
            ]

            response = prompt(questions)
            return response

        else:
            recherche = pce

            for item in recherche:
                what = item.get("what", "N/A")
                where = item.get("where", "N/A")
                print("Intitulé:", what)  # Use what instead of item.get("what", "N/A")
                print("Lieu:", where)  # Use where instead of item.get("where", "N/A")
                print("===")
        reponse = prompt(self.__questions)

        if reponse["choix"] == ("Quitter" if self.langue == "français" else "Quit"):
            pass

        elif reponse["choix"] == "Supprimer des recherches sauvegardées":
            question = prompt(
                [
                    {
                        "type": "list",
                        "message": "Choisissez une recherche sauvegardée à supprimer :",
                        "name": "recherche",
                        "choices": [
                            f"{item.get('what','N/A')} - {item.get('where', 'N/A')}"
                            for item in recherche
                        ],
                    }
                ]
            )
            selected_choice_str = question["recherche"]
            selected_item = next(
                (
                    item
                    for item in recherche
                    if f"{item.get('what','N/A')} - {item.get('where', 'N/A')}"
                    == selected_choice_str
                ),
                None,
            )
            from business.client.recherche import Recherche

            t = Recherche(selected_item)
            if RechercheDao().supprimer_recherche(t, self.user):
                print("La recherche à bien été supprimé")
                from presentation.afficher_recherche_favoris import ARechercheView

                return ARechercheView(self.user, self.langue)

        elif reponse["choix"] == ("Retour" if self.langue == "français" else "Return"):
            from presentation.user_view import UserView

            return UserView(user=self.user, langue=self.langue)

        elif recherche["choix"] == (
            "Retour" if self.langue == "français" else "Return"
        ):
            from presentation.user_view import UserView

            return UserView(user=self.user, langue=self.langue)

        elif recherche["choix"] == (
            "Lancer une recherche" if self.langue == "français" else "Launch a search"
        ):
            from presentation.recherche_view import RechercheView

            return RechercheView(user=self.user, langue=self.langue)
