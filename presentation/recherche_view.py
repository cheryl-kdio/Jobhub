from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.services.utilisateur_service import (
    Utilisateur,
)  # Importation de la classe Utilisateur depuis le module utilisateur_service
from business.dao.utilisateur_dao import UtilisateurDao
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService
from tabulate import tabulate
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from business.client.profil_chercheur_emploi import ProfilChercheurEmploi
from business.dao.recherche_dao import RechercheDao

from business.dao.candidature_dao import CandidatureDao

class RechercheView(AbstractView):
    def __init__(self, user=None):
        self.user = user
        self.results_per_page = 20
        self.__questions = [
            {
                "type": "input",
                "name": "mot_cle",
                "message": "Entrez l'intitulé du poste ou des mots-clés : ",
            },
        ]

    def make_choice(self):
        answers = prompt(self.__questions)
        query_params = {
            "results_per_page": self.results_per_page,
            "what": answers["mot_cle"],
        }
        recherche = Recherche(query_params=query_params)
        r = RechercheService()
        print("Resultats obtenus :")
        choix_offres = [
            {"name": offre.titre, "value": offre}
            for offre in r.obtenir_resultats(recherche)
        ] + [{"name": "Retour", "value": None}]

        question = {
            "type": "list",
            "message": "Choisissez une offre à détailler :",
            "choices": choix_offres,
        }
        answers = prompt([question])

        if answers[0] == "retour":
            from presentation.start_view import StartView

            return StartView()
        else:
            print(answers[0])
            candidater = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "oui",
                        "message": "Envoyer sa candidature",
                        "default": False,
                    }
                ]
            )
            if candidater["oui"]:
                if self.user:
                    CandidatureDao().candidater(offre=answers[0],utilisateur=self.user)
                    print("Candidature effectuée")
                else:
                    print(
                        "Vous devez être connecté pour accéder à cette fonctionnalité"
                    )
                    from presentation.start_view import StartView
                    return StartView()


            sauvegarder_recherche = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "sauv",
                        "message": "Sauvergarder la recherche ?",
                        "default": False,
                    }
                ]
            )
            if sauvegarder_recherche["sauv"]:
                if self.user:
                    RechercheDao().sauvegarder_recherche(recherche, self.user)
                    print("Search saved successfully.")
                else:
                    print(
                        "Vous devez être connecté pour accéder à cette fonctionnalité"
                    )
                    from presentation.start_view import StartView

                    return StartView()
            autre_recherche = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "continue",
                        "message": "Faire une autre recherche ?",
                        "default": True,
                    }
                ]
            )
            if autre_recherche["continue"]:
                return RechercheView(self.user)

            else:
                if not self.user:
                    from presentation.start_view import StartView

                    return StartView()
                else:
                    from presentation.user_view import UserView

                    return UserView(self.user)

    def display_info(self):
        print("Veuillez entrer les informations suivantes :")
