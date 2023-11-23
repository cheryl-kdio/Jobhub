from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class OffreView(AbstractView):
    def __init__(self, user, langue):
        self.user = user
        self.langue = langue
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": (
                    f"Hello {Session().user_name}"
                    if self.langue == "anglais"
                    else f"Bonjour {Session().user_name}"
                ),
                "choices": [
                    ("Return" if self.langue == "anglais" else "Retour"),
                    ("Log out" if self.langue == "anglais" else "Se déconnecter"),
                    ("Quit" if self.langue == "anglais" else "Quitter"),
                    (
                        "Delete an offer"
                        if self.langue == "anglais"
                        else "Supprimer une offre"
                    ),
                ],
            }
        ]

    def display_info(self):
        from business.dao.offre_dao import OffreDao

        offredao = OffreDao()
        pce = offredao.voir_favoris(self.user)
        if pce == []:
            print(
                "Vous n'avez pas d'offres sauvegardés"
                if self.langue == "anglais"
                else "You don't have any saved offers."
            )

        else:
            from business.client.offre import Offre

            questions = [
                {
                    "type": "list",
                    "name": "offre",
                    "message": (
                        "Choose the offer to view:"
                        if self.langue == "anglais"
                        else "Choisissez l'offre à consulter :"
                    ),
                    "choices": [
                        f" Title: {element.titre}, Location: {element.lieu}"
                        if self.langue == "anglais"
                        else f" Titre: {element.titre}, Lieu: {element.lieu}"
                        for element in pce
                        if isinstance(element, Offre)
                    ],
                }
            ]

            offre = prompt(questions)

        return offre, pce

    def make_choice(self):
        offre, pce = self.display_info()
        reponse = prompt(self.__questions)
        if reponse["choix"] == ("Quitter" if self.langue == "français" else "Quit"):
            pass

        elif (
            reponse["choix"] == "Supprimer une offre"
            if self.langue == "français"
            else "Delete an offer"
        ):
            from business.dao.offre_dao import OffreDao

            offredao = OffreDao()
            from business.client.offre import Offre

            question = [
                {
                    "type": "list",
                    "name": "offre",
                    "message": (
                        "Choisissez l'offre à consulter"
                        if self.langue == "français"
                        else "Choose the offer to delete:"
                    ),
                    "choices": [
                        f"ID:{element.id_offre}, Title: {element.titre}, Location: {element.lieu}"
                        if self.langue == "anglais"
                        else f" Id:{element.id_offre}, Titre: {element.titre}, Lieu: {element.lieu}"
                        for element in pce
                        if isinstance(element, Offre)
                    ],
                }
            ]
            offre = prompt(question)
            selected_offre_str = offre["offre"]

            selected_offre = None
            for element in pce:
                if (
                    isinstance(element, Offre)
                    and f"ID: {element.id_offre}" in selected_offre_str
                ):
                    selected_offre = element
                    break
            with open(
                "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
            ) as asset:
                print(asset.read())

            offredao.supprimer_offre(selected_offre)
            print(
                "L'offre a bien été supprimée"
                if self.langue == "français"
                else "The offer has been deleted"
            )
            return OffreView(user=self.user, langue=self.langue)

        elif reponse["choix"] == ("Retour" if self.langue == "français" else "Return"):
            from presentation.user_view import UserView

            return UserView(user=self.user, langue=self.langue)

        elif reponse["choix"] == (
            "Se déconnecter" if self.langue == "français" else "Disconnect"
        ):
            self.user._connexion = False
            from presentation.start_view import StartView

            return StartView(langue=self.langue)
