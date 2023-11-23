from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session


class ProfileView(AbstractView):
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
                        "Modify alerts"
                        if self.langue == "anglais"
                        else "Modifier ses alertes"
                    ),
                    "Back" if self.langue == "anglais" else "Retour",
                    "Disconnect" if self.langue == "anglais" else "Se déconnecter",
                    "Quit" if self.langue == "anglais" else "Quitter",
                ],
            }
        ]

    def display_info(self):
        from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao

        pced = ProfilChercheurEmploiDao()
        pce = pced.voir_profil_chercheur_emploi(self.user)
        if pce == []:
            print(
                "You don't have any alerts"
                if self.langue == "anglais"
                else "Vous n'avez pas d'alerte"
            )
            print(
                "Let's create one! :"
                if self.langue == "anglais"
                else "Créons-en une ! :"
            )
            questions = [
                {
                    "type": "input",
                    "name": "nom",
                    "message": "Alert name"
                    if self.langue == "anglais"
                    else "Nom de l'alerte",
                },
                {
                    "type": "input",
                    "name": "mots_cles",
                    "message": "Keywords: "
                    if self.langue == "anglais"
                    else "Mots clés : ",
                },
                {
                    "type": "input",
                    "name": "lieu",
                    "message": "City where you want to work:"
                    if self.langue == "anglais"
                    else "Ville où vous souhaitez travailler :",
                },
                {
                    "type": "input",
                    "name": "distance",
                    "message": "Distance around the city"
                    if self.langue == "anglais"
                    else "Distance autour de la ville",
                },
                {
                    "type": "input",
                    "name": "type_contrat",
                    "message": "Fixed-term/Permanent"
                    if self.langue == "anglais"
                    else "CDD/CDI",
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

            choix_profil = [
                {
                    "name": f"{element.id_profil_chercheur_emploi}. {element.nom} - {element.lieu}",
                    "value": element,
                }
                for element in pce
                if isinstance(element, ProfilChercheurEmploi)
            ]

            if choix_profil:
                questions = [
                    {
                        "type": "list",
                        "name": "profil",
                        "message": (
                            "Choose the profile to consult"
                            if self.langue == "anglais"
                            else "Choisissez le profil à consulter"
                        ),
                        "choices": choix_profil + [{"name": "Retour", "value": None}],
                    }
                ]

            profil_chercheur_emploi = prompt(questions)["profil"]
            profil_dict = vars(profil_chercheur_emploi)
            for key, value in profil_dict.items():
                print(f"{key}: {value}")

        input(
            "Appuyez sur Entrée pour continuer"
            if self.langue == "français"
            else "Press Enter to continue"
        )
        with open(
            "presentation/graphical_assets/banner.txt", "r", encoding="utf-8"
        ) as asset:
            print(asset.read())

        return profil_chercheur_emploi

    def make_choice(self):
        profil_chercheur_emploi = self.display_info()
        reponse = prompt(self.__questions)

        choix_change_param = (
            "Modify alerts" if self.langue == "anglais" else "Modifier ses alertes"
        )
        choix_return = "Back" if self.langue == "anglais" else "Retour"
        choix_disconnect = (
            "Disconnect" if self.langue == "anglais" else "Se déconnecter"
        )

        if reponse["choix"] == choix_change_param:
            from presentation.modif_profile_view import ModifProfileView

            return ModifProfileView(
                user=self.user, pce=profil_chercheur_emploi, langue=self.langue
            )

        elif reponse["choix"] == choix_return:
            from presentation.user_view import UserView

            return UserView(user=self.user, langue=self.langue)

        elif reponse["choix"] == choix_disconnect:
            self.user._connexion = False
            from presentation.start_view import StartView

            return StartView(langue=self.langue)

        else:
            pass
