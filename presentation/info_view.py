from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class InfoView(AbstractView):
    def __init__(self, user, langue):
        self.langue = langue
        self.user = user
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
                    (
                        "Update personal information"
                        if self.langue == "anglais"
                        else "Modifier ses informations personnelles"
                    ),
                    ("Return" if self.langue == "anglais" else "Retour"),
                    ("Disconnect" if self.langue == "anglais" else "Se déconnecter"),
                    ("Quit" if self.langue == "anglais" else "Quitter"),
                ],
            }
        ]

    def display_info(self):
        from business.dao.utilisateur_dao import UtilisateurDao

        utilisateurdao = UtilisateurDao
        utils = utilisateurdao.recuperer_utilisateur(self, self.user.id)
        excluded_fields = ["id_compte_utilisateur", "mdp", "sel"]

        for record in utils:
            for i, (key, value) in enumerate(record.items()):
                if key not in excluded_fields:
                    print(f"{i + 1}: {key}: {value}")

        input(
            "Appuyez sur Entrée pour continuer"
            if self.langue == "français"
            else "Press enter to continue"
        )
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        choix_quit = "Quit" if self.langue == "anglais" else "Quitter"
        choix_update_info = (
            "Update personal information"
            if self.langue == "anglais"
            else "Modifier ses informations personnelles"
        )
        choix_return = "Return" if self.langue == "anglais" else "Retour"
        choix_disconnect = (
            "Disconnect" if self.langue == "anglais" else "Se déconnecter"
        )

        if reponse["choix"] == choix_quit:
            pass
        elif reponse["choix"] == choix_update_info:
            from presentation.modif_info_view import ModifInfoView

            return ModifInfoView(user=self.user, langue=self.langue)
        elif reponse["choix"] == choix_return:
            from presentation.user_view import UserView

            return UserView(user=self.user, langue=self.langue)
        elif reponse["choix"] == choix_disconnect:
            self.user._connexion = False
            from presentation.start_view import StartView

            return StartView(langue=self.langue)
