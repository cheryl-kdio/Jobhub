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
                    "Modifier son profil chercheur d'emploi",
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
            print("Votre Profil Chercheur d'Emploi est vide")
            print("Remplissons le ! :")
            questions = [
                {
                    "type": "input",
                    "name": "nom",
                    "message": "Nom de l'alerte",
                },
                {
                    "type": "input",
                    "name": "mots_cles",
                    "message": "Mots clés : ",
                },
                {
                    "type": "input",
                    "name": "lieu",
                    "message": "Ville où vous souhaitez travailler :",
                },
                {
                    "type": "input",
                    "name": "distance",
                    "message": "Distance autour de la ville",
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
                nom=answers[0],
                mots_cles=answers[1],
                lieu=answers[2],
                distance=answers[3],
                type_contrat=answers[4],
            )

            pced.ajouter_profil_chercheur_emploi(profil_chercheur_emploi, self.user)
            pce = pced.voir_profil_chercheur_emploi(self.user)[0]

        else:
            from business.client.profil_chercheur_emploi import ProfilChercheurEmploi

            questions = [
                {
                    "type": "list",
                    "name": "profil",
                    "message": "Choisissez le profil à consulter",
                    "choices": [
                        f"ID: {element.id_profil_chercheur_emploi}, Nom: {element.nom}, Lieu: {element.lieu}"
                        for element in pce
                        if isinstance(element, ProfilChercheurEmploi)
                    ],
                }
            ]

            profil_chercheur_emploi = prompt(questions)
            print(profil_chercheur_emploi)

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

        elif reponse["choix"] == "Modifier son profil chercheur d'emploi":
            from presentation.modif_profile_view import ModifProfileView

            return ModifProfileView(user=self.user, pce=profil_chercheur_emploi)

        elif reponse["choix"] == "Lancer une recherche":
            from presentation.recherche_view import RechercheView

            return RechercheView(self.user)

        elif reponse["choix"] == "Créer un compte":
            from presentation.creer_compte_view import CreateAccountView

            return CreateAccountView()
