from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class UserView(AbstractView):
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
                    (
                        "View alerts"
                        if self.langue == "anglais"
                        else "Consulter ses alertes"
                    ),
                    (
                        "Check personal information"
                        if self.langue == "anglais"
                        else "Vérifier ses informations personnelles"
                    ),
                    (
                        "Follow applications"
                        if self.langue == "anglais"
                        else "Suivre ses candidatures"
                    ),
                    (
                        "Saved offers"
                        if self.langue == "anglais"
                        else "Offres sauvegardés"
                    ),
                    (
                        "Saved searches"
                        if self.langue == "anglais"
                        else "Recherches sauvegardés"
                    ),
                    (
                        "Start a search"
                        if self.langue == "anglais"
                        else "Lancer une recherche"
                    ),
                    ("Quit" if self.langue == "anglais" else "Quitter"),
                ],
            }
        ]

    def display_info(self):
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if (
            reponse["choix"] == "Quitter"
            if self.langue == "français"
            else reponse["choix"] == "Quit"
        ):
            pass

        elif reponse["choix"] == (
            "Consulter ses alertes" if self.langue == "français" else "View alerts"
        ):
            from presentation.profile_view import ProfileView

            return ProfileView(user=self.user, langue=self.langue)

        elif reponse["choix"] == (
            "Offres sauvegardés" if self.langue == "français" else "Saved offers"
        ):
            from presentation.afficher_offre_favoris import OffreView

            return OffreView(user=self.user, langue=self.langue)

        elif reponse["choix"] == (
            "Recherches sauvegardés" if self.langue == "français" else "Saved searches"
        ):
            from presentation.afficher_recherche_favoris import RechercheView

            return RechercheView(user=self.user, langue=self.langue)

        elif reponse["choix"] == (
            "Lancer une recherche" if self.langue == "français" else "Start a search"
        ):
            from presentation.recherche_view import RechercheView

            return RechercheView(user=self.user, langue=self.langue)

        elif reponse["choix"] == (
            "Vérifier ses informations personnelles"
            if self.langue == "français"
            else "Check personal information"
        ):
            from presentation.info_view import InfoView

            return InfoView(user=self.user, langue=self.langue)

        elif reponse["choix"] == (
            "Suivre ses candidatures"
            if self.langue == "français"
            else "Follow applications"
        ):
            from presentation.suivi_candidature_view import CandidatureView

            return CandidatureView(user=self.user, langue=self.langue)
