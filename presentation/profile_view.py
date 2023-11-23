from InquirerPy import prompt, inquirer

from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from business.business_object.profil_chercheur_emploi import ProfilChercheurEmploi
from business.dao.recherche_dao import RechercheDao
from business.services.recherche_service import RechercheService
from business.business_object.recherche import Recherche


class ProfileView(AbstractView):
    def __init__(self, user, langue):
        self.user = user
        self.langue = langue

    def display_info(self):
        pass

    def make_choice(self):
        pced = ProfilChercheurEmploiDao()
        choix_alertes = [
            {
                "name": str(i + 1) + ". " + alerte.nom + "-" + alerte.lieu,
                "value": alerte,
            }
            for i, alerte in enumerate(pced.voir_profil_chercheur_emploi(self.user))
        ] + [
            {"name": "Creer une alerte", "value": "create_alert"},
            {"name": "Retour", "value": "retour"},
        ]

        self.__questions = {
            "type": "list",
            "message": "Voir le détail d'une alerte : \n - - - - - - - - - - - - - - - - - - - -\n"
            if self.langue == "français"
            else "Detail an alert : \n - - - - - - - - - - - - - - - - - - - -\n",
            "choices": choix_alertes,
        }

        answers = prompt(self.__questions)

        if answers[0] == "retour":
            from presentation.start_view import StartView

            return StartView(self.langue)

        elif answers[0] == "create_alert":
            self.__questions = [
                {
                    "type": "input",
                    "name": "nom",
                    "message": "Alert name : "
                    if self.langue == "anglais"
                    else "Nom de l'alerte :",
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
                    "type": "list",
                    "name": "type_contrat",
                    "message": "Type de contrat : CDD/CDI/Temps plein/Temps partiel"
                    if self.langue == "français"
                    else "Contract type: Fixed-term/Permanent/Full-time/Part-time",
                    "choices": [
                        {
                            "name": "CDD"
                            if self.langue == "français"
                            else "Fixed-term",
                            "value": "CDD",
                        },
                        {
                            "name": "CDI" if self.langue == "français" else "Permanent",
                            "value": "CDI",
                        },
                        {
                            "name": "Temps plein"
                            if self.langue == "français"
                            else "Full-time",
                            "value": "TEMPS PLEIN",
                        },
                        {
                            "name": "Temps partiel"
                            if self.langue == "français"
                            else "Part-time",
                            "value": "TEMPS PARTIEL",
                        },
                    ],
                },
            ]

            reponse_alerte = prompt(self.__questions)
            from business.business_object.profil_chercheur_emploi import (
                ProfilChercheurEmploi,
            )

            pce = ProfilChercheurEmploi(
                nom=reponse_alerte["nom"],
                mots_cles=reponse_alerte["mots_cles"],
                lieu=reponse_alerte["lieu"],
                distance=reponse_alerte["distance"],
                type_contrat=reponse_alerte["type_contrat"],
            )
            if pced.ajouter_profil_chercheur_emploi(pce, self.user):
                print("Votre alerte a bien été créée")
                return ProfileView(self.user, self.langue)
        else:
            print(answers[0])
            self.__questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "",
                    "choices": [
                        "Supprimer cette alerte",
                        "Modifier cette alerte",
                        "Voir les résultats",
                        "Retour",
                    ],
                }
            ]
            answers2 = prompt(self.__questions)
            if answers2["choix"] == "Supprimer cette alerte":
                if pced.supprimer_profil_chercheur_emploi(answers[0]):
                    print("Cette alerte a bien été supprimée")
                    return ProfileView(self.user, self.langue)
            elif answers2["choix"] == "Modifier cette alerte":
                from presentation.modif_profile_view import ModifProfileView

                return ModifProfileView(
                    pce=answers[0], user=self.user, langue=self.langue
                )
            elif answers2["choix"] == "Voir les résultats":
                from presentation.recherche_view import RechercheView

                return RechercheView(
                    langue=self.langue,
                    user=self.user,
                    query_params=answers[0].query_params,
                )
            else:
                return ProfileView(user=self.user, langue=self.langue)
