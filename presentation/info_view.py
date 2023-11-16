from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class InfoView(AbstractView):
    def __init__(self, user):
        self.user = user
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour {Session().user_name}",
                "choices": [
                    "Modifier ses informations personnelles",
                    "Retour",
                    "Se déconnecter",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        from business.dao.utilisateur_dao import UtilisateurDao

        utilisateurdao = UtilisateurDao
        utils = utilisateurdao.recuperer_utilisateur(self, self.user.id)
        for record in utils:
            for i, (key, value) in enumerate(record.items()):
                print(f"{i + 1}: {key}: {value}")

        input("Appuyez sur Entrée pour continuer")
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Modifier ses informations personnelles":
            from presentation.modif_info_view import ModifInfoView

            return ModifInfoView(self.user)

        elif reponse["choix"] == "Lancer une recherche":
            from presentation.recherche_view import RechercheView

            return RechercheView(self.user)

        elif reponse["choix"] == "Créer un compte":
            from presentation.creer_compte_view import CreateAccountView

            return CreateAccountView()
