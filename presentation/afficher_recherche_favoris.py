from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class RechercheView(AbstractView):
    def __init__(self, user):
        self.user = user
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour {Session().user_name}",
                "choices": [
                    "Modifier ses recherches sauvegardés",
                    "Retour",
                    "Se déconnecter",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        from business.dao.recherche_dao import RechercheDao

        pced = RechercheDao()
        pce = pced.voir_favoris(self.user)
        if pce == []:
            print("Vous n'avez pas enregistré de recherche")
            print("Remplissons le ! :")
            # l'emmener faire une recherche

        else:
            recherche = pce

        what = []
        where = []

        for item in recherche:
            what = item.get("what", "N/A")
            where = item.get("where", "N/A")
            print("Intitulé:", item.get("what", "N/A"))
            print("Lieu", item.get("where","N/A"))
            print("===") 
        
        input("Appuyez sur Entrée pour continuer")
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

        return recherche

    def make_choice(self):
        profil_chercheur_emploi = self.display_info()
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Modifier ses recherches":
            from presentation.modif_profile_view import ModifProfileView

            return ModifProfileView(profil_chercheur_emploi, self.user)

        elif reponse["choix"] == "Lancer une recherche":
            from presentation.recherche_view import RechercheView

            return RechercheView(self.user)

        elif reponse["choix"] == "Créer un compte":
            from presentation.creer_compte_view import CreateAccountView

            return CreateAccountView()
        
        else:
            print(answers[0])
            utiliser_recherche = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "use",
                        "message": "Utiliser la recherche ?",
                        "default": False,
                    }
                ]
            )
            if utiliser_recherche["use"]:
                if self.user: ## Quoi ajouter pour relancer la recherche initiale ? 

                    return StartView()