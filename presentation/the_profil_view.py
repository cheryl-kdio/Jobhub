from InquirerPy import prompt
from presentation.abstract_view import AbstractView
from presentation.session import Session
from presentation.profile_view import ProfileView
from presentation.offre_fav_view import OffreView
from presentation.afficher_recherche_favoris import ARechercheView
from presentation.recherche_view import RechercheView
from presentation.info_view import InfoView
from presentation.suivi_candidature_view import CandidatureView


class TheProfileView(AbstractView):
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
                    "Alertes" if self.langue == "français" else "Alerts",
                    "Vérifier ses informations personnelles"
                    if self.langue == "français"
                    else "Check personal information",
                    "Suivre ses candidatures"
                    if self.langue == "français"
                    else "Check applications",
                    "Offres sauvegardées"
                    if self.langue == "français"
                    else "Saved Offers",
                    "Recherches sauvegardées"
                    if self.langue == "français"
                    else "Saved searches",
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
        choix = reponse["choix"]

        if choix == ("Quitter" if self.langue == "français" else "Quit"):
            pass
        elif choix == ("Alertes" if self.langue == "français" else "Alerts"):
            return ProfileView(user=self.user, langue=self.langue)
        elif choix == (
            "Offres sauvegardées" if self.langue == "français" else "Saved Offers"
        ):
            return OffreView(user=self.user, langue=self.langue)
        elif choix == (
            "Recherches sauvegardées" if self.langue == "français" else "Saved searches"
        ):
            return ARechercheView(user=self.user, langue=self.langue)
        elif choix == (
            "Vérifier ses informations personnelles"
            if self.langue == "français"
            else "Check personal information"
        ):
            return InfoView(user=self.user, langue=self.langue)
        elif (
            choix == "Suivre ses candidatures"
            if self.langue == "français"
            else "Check applications"
        ):
            return CandidatureView(user=self.user, langue=self.langue)
