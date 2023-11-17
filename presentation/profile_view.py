from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class ProfileView(AbstractView):
    def __init__(self, user):
        self.user = user
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Bonjour {Session().user_name}",
                "choices": [
                    "Modifier ses alertes",
                    "Retour",
                    "Se déconnecter",
                    "Quitter",
                ],
            }
        ]

    def display_info(self):
        from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao

        pced = ProfilChercheurEmploiDao()
        pce = pced.voir_profil_chercheur_emploi(self.user)
        if pce == []:
            print("Vous n'avez pas d'alerte")
            print("Remplissons le ! :")
            questions = [
                {
                    "type": "input",
                    "name": "lieu",
                    "message": "Ville où vous souhaitez travailler :",
                },
                {
                    "type": "input",
                    "name": "domaine",
                    "message": "Domaine : ",
                },
                {
                    "type": "input",
                    "name": "salaire_min",
                    "message": "Salaire minimum",
                },
                {
                    "type": "input",
                    "name": "salaire_max",
                    "message": "Salaire maximum",
                },
                {
                    "type": "input",
                    "name": "type_contrat",
                    "message": "CDD/CDI",
                },
            ]
            answers = [prompt([q])[q["name"]] for q in questions]
            print(answers)
            from business.client.profil_chercheur_emploi import ProfilChercheurEmploi

            profil_chercheur_emploi = ProfilChercheurEmploi(
                lieu=answers[0],
                domaine=answers[1],
                salaire_minimum=answers[2],
                salaire_maximum=answers[3],
                type_contrat=answers[4],
            )

            pced.ajouter_profil_chercheur_emploi(profil_chercheur_emploi, self.user)
            pce = pced.voir_profil_chercheur_emploi(self.user)[0]

        else:
            profil_chercheur_emploi = pce[0]
        for i in [
            "lieu",
            "domaine",
            "salaire_minimum",
            "salaire_maximum",
            "type_contrat",
        ]:
            print(getattr(profil_chercheur_emploi, i))

        input("Appuyez sur Entrée pour continuer")
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

        return profil_chercheur_emploi

    def make_choice(self):
        profil_chercheur_emploi = self.display_info()
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass

        elif reponse["choix"] == "Modifier ses alertes":
            from presentation.modif_profile_view import ModifProfileView

            return ModifProfileView(profil_chercheur_emploi, self.user)

        elif reponse["choix"] == "Lancer une recherche":
            from presentation.recherche_view import RechercheView

            return RechercheView(self.user)

        elif reponse["choix"] == "Créer un compte":
            from presentation.creer_compte_view import CreateAccountView

            return CreateAccountView()
