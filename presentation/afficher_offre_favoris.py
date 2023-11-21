from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class OffreView(AbstractView):
    def __init__(self, user):
        self.user = user
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour {Session().user_name}",
                "choices": [
                    "Supprimer une offre",
                    "Retour",
                    "Se déconnecter",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        from business.dao.offre_dao import OffreDao

        offredao = OffreDao()
        pce = offredao.voir_favoris(self.user)
        if pce == []:
            print("Vous n'avez pas d'offres sauvegardés")

        else:
            from business.client.offre import Offre

            questions = [
                {
                    "type": "list",
                    "name": "offre",
                    "message": "Choisissez l'offre' à consulter",
                    "choices": [
                        f" Titre: {element.titre}, Lieu: {element.lieu}"
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
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Supprimer une offre":
            from business.dao.offre_dao import OffreDao

            offredao = OffreDao()
            from business.client.offre import Offre

            question = [
                {
                    "type": "list",
                    "name": "offre",
                    "message": "Choisissez l'offre à consulter",
                    "choices": [
                        f"ID: {element.id_offre}, Titre: {element.titre}, Lieu: {element.lieu}"
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
            print("L'offre a bien été supprimée")
            return OffreView(self.user)

        elif reponse["choix"] == "Retour":
            from presentation.user_view import UserView

            return UserView(self.user)

        elif reponse["choix"] == "Se déconnecter":
            self.user._connexion = False
            from presentation.start_view import StartView

            return StartView()
