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
                    f"Hello {self.user.nom}"
                    if self.langue == "anglais"
                    else f"Bonjour {self.user.nom}\n"
                ),
                "choices": [
                    "Consulter ses alertes"
                    if self.langue == "français"
                    else "View alerts",
                    "Vérifier ses informations personnelles"
                    if self.langue == "français"
                    else "Check personal information",
                    "Suivre ses candidatures"
                    if self.langue == "français"
                    else "Track job applications",
                    "Offres sauvegardées"
                    if self.langue == "français"
                    else "Saved Offers",
                    "Recherches sauvegardées"
                    if self.langue == "français"
                    else "Saved searches",
                    "Lancer une recherche"
                    if self.langue == "français"
                    else "Start a new search",
                    "Quitter" if self.langue == "français" else "Quit",
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
        if reponse["choix"] == ("Quitter" if self.langue == "français" else "Quit"):
            pass

        elif reponse["choix"] == (
            "Consulter ses alertes" if self.langue == "français" else "View alerts"
        ):
            from presentation.profile_view import ProfileView

            return ProfileView(user=self.user, langue=self.langue)

        elif reponse["choix"] == (
            "Offres sauvegardées" if self.langue == "français" else "Saved Offers"
        ):
            from presentation.offre_fav_view import OffreView

            return OffreView(user=self.user, langue=self.langue)

        elif reponse["choix"] == "Recherches sauvegardés":
            from presentation.afficher_recherche_favoris import RechercheView

            return RechercheView(user=self.user)

        elif reponse["choix"] == (
            "Lancer une recherche"
            if self.langue == "français"
            else "Start a new search"
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

        elif reponse["choix"] == "Suivre ses candidatures":
            from presentation.suivi_candidature_view import CandidatureView

            return CandidatureView(user=self.user, langue=self.langue)
