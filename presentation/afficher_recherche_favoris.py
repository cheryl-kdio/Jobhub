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
                "message": f"Bonjour {Session().user_name}"
                if self.langue == "français"
                else f"Hello {Session().user_name}",
                "choices": [
                    "Supprimer des recherches sauvegardées"
                    if self.langue == "français"
                    else "Delete searches",
                    "Choisir une recherche"
                    if self.langue == "français"
                    else "Choice search",
                    "Retour" if self.langue == "français" else "Return",
                    "Quitter" if self.langue == "français" else "Quit",
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
                        "Retour" if self.langue == "français" else " Return",
                        "Lancer une recherche"
                        if self.langue == "français"
                        else "Launch search",
                    ],
                }
            ]

            response = prompt(questions)

            if response["choix"] == (
                "Retour" if self.langue == "français" else "Return"
            ):
                from presentation.the_profil_view import TheProfileView

                return TheProfileView(user=self.user, langue=self.langue)

            elif response["choix"] == (
                "Lancer une recherche"
                if self.langue == "français"
                else "Launch a search"
            ):
                from presentation.recherche_view import RechercheView

                return RechercheView(user=self.user, langue=self.langue)

        else:
            recherche = pce

            for item in recherche:
                what = item.get("what", "N/A")
                where = item.get("where", "N/A")
                print(
                    "Intitulé:" if self.langue == "français" else "Title", what
                )  # Use what instead of item.get("what", "N/A")
                print(
                    "Lieu:" if self.langue == "français" else "Where", where
                )  # Use where instead of item.get("where", "N/A")
                print("===")
        reponse = prompt(self.__questions)

        if reponse["choix"] == ("Quitter" if self.langue == "français" else "Quit"):
            pass

        elif reponse["choix"] == (
            "Supprimer des recherches sauvegardées"
            if self.langue == "français"
            else "Delete searches"
        ):
            question = prompt(
                [
                    {
                        "type": "list",
                        "message": "Choisissez une recherche sauvegardée à supprimer :"
                        if self.langue == "français"
                        else "Choice a search saved to delete",
                        "name": "recherche",
                        "choices": [
                            f"what: {item.get('what', 'N/A')}, where: {item.get('where', 'N/A')}"
                            for item in recherche
                        ],
                    }
                ]
            )
            selected_choice_str = question["recherche"]

            selected_choice_dict = {"results_per_page": 20}
            for pair in selected_choice_str.split(", "):
                key, value = pair.split(": ")
                selected_choice_dict[key] = value

            from business.business_object.recherche import Recherche

            t = Recherche(selected_choice_dict)

            if RechercheDao().supprimer_recherche(t, self.user):
                print(
                    "La recherche à bien été supprimé"
                    if self.langue == "français"
                    else "Search was well deleted"
                )
                from presentation.afficher_recherche_favoris import ARechercheView

                return ARechercheView(self.user, self.langue)

        elif reponse["choix"] == (
            "Choisir une recherche" if self.langue == "français" else "Choice search"
        ):
            from presentation.recherche_view import RechercheView

            question = prompt(
                [
                    {
                        "type": "list",
                        "message": "Choisissez une recherche sauvegardée à supprimer :"
                        if self.langue == "français"
                        else "Choice a search saved to delete",
                        "name": "recherche",
                        "choices": [
                            f"what: {item.get('what', 'N/A')}, where: {item.get('where', 'N/A')}"
                            for item in recherche
                        ],
                    }
                ]
            )

            selected_choice_str = question["recherche"]

            selected_choice_dict = {"results_per_page": 20}
            for pair in selected_choice_str.split(", "):
                key, value = pair.split(": ")
                selected_choice_dict[key] = value

            # Remplacez les valeurs manquantes par "N/A"
            selected_choice_dict.setdefault("where", "N/A")
            selected_choice_dict.setdefault("what", "N/A")

            from business.business_object.recherche import Recherche

            t = Recherche(selected_choice_dict)

            return RechercheView(
                langue=self.langue,
                user=self.user,
                query_params=t.query_params,
            )

        elif reponse["choix"] == ("Retour" if self.langue == "français" else "Return"):
            from presentation.user_view import UserView

            return UserView(user=self.user, langue=self.langue)
