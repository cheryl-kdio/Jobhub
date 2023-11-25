from InquirerPy import prompt

from presentation.abstract_view import AbstractView


from InquirerPy import prompt


class ModifInfoView(AbstractView):
    def __init__(self, langue, user=None):
        self.user = user
        self.langue = langue

    def make_choice(self):
        choix_info = [
            "nom",
            "age",
            "mail",
            "tel",
            "ville",
            "code_postal",
        ]
        translated_choices = (
            [
                "Name",
                "Age",
                "Email",
                "Phone",
                "City",
                "Postal Code",
                "Return",
            ]
            if self.langue == "anglais"
            else [
                "Nom",
                "Âge",
                "Courriel",
                "Téléphone",
                "Ville",
                "Code postal",
                "Retour",
            ]
        )

        question = {
            "type": "list",
            "message": (
                "Choose an element to modify:"
                if self.langue == "anglais"
                else "Choisissez un élément à modifier :"
            ),
            "choices": translated_choices,
        }
        answers = prompt([question])

        if answers[0] == ("Retour" if self.langue == "français" else "Return"):
            from presentation.info_view import InfoView

            return InfoView(user=self.user, langue=self.langue)

        real_choice = choix_info[translated_choices.index(answers[0])]
        question = {
            "type": "input",
            "name": "nouv",
            "message": (
                f"New {answers[0]}:"
                if self.langue == "anglais"
                else f"Nouveau {answers[0]} :"
            ),
        }
        from business.dao.utilisateur_dao import (
            UtilisateurDao,
        )

        utilisateurdao = UtilisateurDao()
        utilisateurdao.update_user_info(
            self.user.id, real_choice, prompt(question)["nouv"]
        )
        utils = utilisateurdao.recuperer_utilisateur(self.user.id)
        excluded_fields = ["id_compte_utilisateur", "mdp", "sel"]
        for record in utils:
            for i, (key, value) in enumerate(record.items()):
                if key not in excluded_fields:
                    print(f"{i + 1}: {key}: {value}")
        input(
            "Press Enter to continue"
            if self.langue == "anglais"
            else "Appuyez sur entrée pour continuer"
        )

        quest = [
            {
                "type": "list",
                "name": "choix",
                "message": (
                    "Choose an option:"
                    if self.langue == "anglais"
                    else "Choisissez une option:"
                ),
                "choices": [
                    "Modify another information",
                    "Return",
                    "Disconnect",
                    "Quit",
                ]
                if self.langue == "anglais"
                else [
                    "Modifier une autre information",
                    "Retour",
                    "Se déconnecter",
                    "Quitter",
                ],
            }
        ]
        answ = prompt(quest)

        choix_update_info = (
            "Modify another information"
            if self.langue == "anglais"
            else "Modifier une autre information"
        )
        choix_return = "Return" if self.langue == "anglais" else "Retour"
        choix_disconnect = (
            "Disconnect" if self.langue == "anglais" else "Se déconnecter"
        )

        if answ["choix"] == choix_update_info:
            return ModifInfoView(user=self.user, langue=self.langue)

        elif answ["choix"] == choix_disconnect:
            self.user._connexion = False
            from presentation.start_view import StartView

            return StartView(langue=self.langue)

        elif answ["choix"] == choix_return:
            from presentation.info_view import InfoView

            return InfoView(user=self.user, langue=self.langue)
        else:
            pass

    def display_info(self):
        print(
            "Enter the following information:"
            if self.langue == "anglais"
            else "Veuillez entrer les informations suivantes :"
        )
