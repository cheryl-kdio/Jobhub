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
                    "Modifier ses offres sauvegardés",
                    "Retour",
                    "Se déconnecter",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        from business.dao.offre_dao import OffreDao

        pced = OffreDao()
        pce = pced.voir_profil_chercheur_emploi(self.user)
        if pce == []:
            print("Vous n'avez pas d'offres sauvegardés")
            print("Remplissons le ! :")
            ## l'emmener faire une recherche

        else:
            offre = pce[0]
        for i in [
            "titre",
            "domaine",
            "lieu",
            "type_contrat",
            "lien_offre",
            "salaire_minimum",
            "entreprise",
            "description",
        ]:
            print(getattr(offre, i))

        input("Appuyez sur Entrée pour continuer")
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

        return offre

    def make_choice(self):
        profil_chercheur_emploi = self.display_info()
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Modifier ses offres":
            from presentation.modif_profile_view import ModifProfileView

            return ModifProfileView(profil_chercheur_emploi, self.user)

        elif reponse["choix"] == "Lancer une recherche":
            from presentation.recherche_view import RechercheView

            return RechercheView(self.user)

        elif reponse["choix"] == "Créer un compte":
            from presentation.creer_compte_view import CreateAccountView

            return CreateAccountView()
