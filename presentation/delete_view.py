from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class DeleteView(AbstractView):
    def __init__(self, user, langue):
        self.langue = langue
        self.user = user
        self.__questions = [
            {
                "type": "confirm",
                "name": "oui",
                "message": (
                    "Are you sure you want to permanently leave our application? All your data will be lost."
                    if self.langue == "anglais"
                    else "Etes vous certain de vouloir quitter definitivement notre application ? Toutes vos données seront perdues"
                ),
                "default": False,
            }
        ]

    def make_choice(self):
        answer = prompt(self.__questions)
        if answer["oui"]:
            from business.dao.utilisateur_dao import UtilisateurDao

            udao = UtilisateurDao()
            suppr = udao.supprimer(user=self.user)
            if suppr:
                print(
                    "Your account has been successfully deleted."
                    if self.langue == "anglais"
                    else "Votre compte a bien été supprimé."
                )
                print(
                    "You can always register again on our application."
                    if self.langue == "anglais"
                    else "Vous pouvez toujours vous réinscrire sur notre application."
                )
                input(
                    "appuyez sur entrée pour continuer"
                    if self.langue == "français"
                    else "Press Enter to continue"
                )

                from presentation.start_view import StartView

                return StartView(langue=self.langue)
            else:
                print(
                    "Your account could not be deleted."
                    if self.langue == "anglais"
                    else "Votre compte n'a pas pu être supprimé."
                )

        else:
            print(
                "Nous sommes ravis de continuer l'aventure avec vous !"
                if self.langue == "français"
                else "We are delighted to continue the adventure with you!"
            )
            from presentation.info_view import InfoView

            return InfoView(user=self.user, langue=self.langue)

    def display_info(self):
        pass
