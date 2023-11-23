from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class UserView(AbstractView):
    def __init__(self, user):
        self.user = user
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour {Session().user_name}",
                "choices": [
                    "🔍 Consulter ses alertes",
                    "📄 Vérifier ses informations personnelles",
                    "🚀 Suivre ses candidatures",
                    "💖 Offres favoris",
                    "📚 Recherches sauvegardées",
                    "🔎 Lancer une recherche",
                    "🚪 Quitter",
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
        if reponse["choix"] == "🚪 Quitter":
            pass

        elif reponse["choix"] == "🔍 Consulter ses alertes":
            from presentation.profile_view import ProfileView

            return ProfileView(self.user)

        elif reponse["choix"] == "💖 Offres favoris":
            from presentation.offre_fav_view import OffreView

            return OffreView(self.user)

        elif reponse["choix"] == "📚 Recherches sauvegardés":
            from presentation.afficher_recherche_favoris import RechercheView

            return RechercheView(self.user)

        elif reponse["choix"] == "🔎 Lancer une recherche":
            from presentation.recherche_view import RechercheView

            return RechercheView(self.user)

        elif reponse["choix"] == "📄 Vérifier ses informations personnelles":
            from presentation.info_view import InfoView

            return InfoView(self.user)
        
        elif reponse["choix"]== "🚀 Suivre ses candidatures":
            from presentation.suivi_candidature_view import CandidatureView
            return CandidatureView(self.user)