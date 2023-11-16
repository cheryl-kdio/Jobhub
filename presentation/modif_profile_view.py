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

from InquirerPy import prompt


class ModifProfileView(AbstractView):
    def __init__(self, pce, user=None):
        self.pce = pce
        self.user = user
        self.results_per_page = 20

    def make_choice(self):
        print(self.pce.domaine)
        choix_profil = [
            "Lieu",
            "Domaine",
            "Salaire minimum",
            "Salaire maximum",
            "type_contrat",
        ]

        question = {
            "type": "list",
            "message": "Choisissez un élément à modifier :",
            "choices": choix_profil,
        }
        answers = prompt([question])

        if answers[0] == "retour":
            from presentation.start_view import StartView
        elif answers[0] == "Lieu":
            question = {
                "type": "input",
                "name": "nouv_lieu",
                "message": "Nouveau Lieu",
            }

            from business.dao.profil_chercheur_emploi_dao import (
                ProfilChercheurEmploiDao,
            )

            pced = ProfilChercheurEmploiDao()
            self.pce.lieu = prompt(question)["nouv_lieu"]
            for i in [
                "lieu",
                "domaine",
                "salaire_minimum",
                "salaire_maximum",
                "type_contrat",
            ]:
                print(getattr(self.pce, i))
            pced.modifier_profil_chercheur_emploi(self.pce)
            print(self.pce)
            questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "",
                    "choices": [
                        "Modifier un autre paramètre",
                        "Lancer une recherche",
                        "Retour",
                        "Quitter",
                    ],
                }
            ]
            if prompt(questions) == "Modifier un autre paramètre":
                return ModifProfileView(self.pce, self.user)
            elif prompt(question) == "Lancer une recherche":
                from presentation.recherche_view import RechercheView

                return RechercheView(self.user)
            elif prompt(question) == "Retour":
                from presentation.profile_view import ProfileView

                return ProfileView(user)
            else:
                pass

        elif answers[0] == "Domaine":
            question = {
                "type": "input",
                "name": "nouv_domaine",
                "message": "Nouveau Domaine",
            }

            from business.dao.profil_chercheur_emploi_dao import (
                ProfilChercheurEmploiDao,
            )

            pced = ProfilChercheurEmploiDao()
            pce.domain = prompt(question)
            modifier_profil_chercheur_emploi(self, pce)
            print(pce)
            questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "",
                    "choices": [
                        "Modifier un autre paramètre",
                        "Lancer une recherche",
                        "Retour",
                        "Quitter",
                    ],
                }
            ]
            if prompt(questions) == "Modifier un autre paramètre":
                return ModifProfileView(pce, self.user)
            elif prompt(question) == "Lancer une recherche":
                from presentation.recherche_view import RechercheView

                return RechercheView(self.user)
            elif prompt(question) == "Retour":
                from presentation.profile_view import ProfileView

                return ProfileView(user)
            else:
                pass
        elif answers[0] == "Salaire minimum":
            question = {
                "type": "input",
                "name": "nouv_salaire_min",
                "message": "Nouveau Salaire Minimum",
            }

            from business.dao.profil_chercheur_emploi_dao import (
                ProfilChercheurEmploiDao,
            )

            pced = ProfilChercheurEmploiDao()
            pce.salaire_minimum = prompt(question)
            modifier_profil_chercheur_emploi(self, pce)
            print(pce)
            questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "",
                    "choices": [
                        "Modifier un autre paramètre",
                        "Lancer une recherche",
                        "Retour",
                        "Quitter",
                    ],
                }
            ]
            if prompt(questions) == "Modifier un autre paramètre":
                return ModifProfileView(pce, self.user)
            elif prompt(question) == "Lancer une recherche":
                from presentation.recherche_view import RechercheView

                return RechercheView(self.user)
            elif prompt(question) == "Retour":
                from presentation.profile_view import ProfileView

                return ProfileView(user)
            else:
                pass
        elif answers[0] == "Salaire maximum":
            question = {
                "type": "input",
                "name": "nouv_salaire_max",
                "message": "Nouveau Salaire Maximum",
            }

            from business.dao.profil_chercheur_emploi_dao import (
                ProfilChercheurEmploiDao,
            )

            pced = ProfilChercheurEmploiDao()
            pce.salaire_maximum = prompt(question)
            modifier_profil_chercheur_emploi(self, pce)
            print(pce)
            questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "",
                    "choices": [
                        "Modifier un autre paramètre",
                        "Lancer une recherche",
                        "Retour",
                        "Quitter",
                    ],
                }
            ]
            if prompt(questions) == "Modifier un autre paramètre":
                return ModifProfileView(pce, self.user)
            elif prompt(question) == "Lancer une recherche":
                from presentation.recherche_view import RechercheView

                return RechercheView(self.user)
            elif prompt(question) == "Retour":
                from presentation.profile_view import ProfileView

                return ProfileView(user)
            else:
                pass
        elif answers[0] == "type_contrat":
            question = {
                "type": "input",
                "name": "nouv_contrat",
                "message": "Nouveau Type de Contrat",
            }

            from business.dao.profil_chercheur_emploi_dao import (
                ProfilChercheurEmploiDao,
            )

            pced = ProfilChercheurEmploiDao()
            pce.type_contrat = prompt(question)
            modifier_profil_chercheur_emploi(self, pce)
            print(pce)
            questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": "",
                    "choices": [
                        "Modifier un autre paramètre",
                        "Lancer une recherche",
                        "Retour",
                        "Quitter",
                    ],
                }
            ]
            if prompt(questions) == "Modifier un autre paramètre":
                return ModifProfileView(pce, self.user)
            elif prompt(question) == "Lancer une recherche":
                from presentation.recherche_view import RechercheView

                return RechercheView(self.user)
            elif prompt(question) == "Retour":
                from presentation.profile_view import ProfileView

                return ProfileView(user)
            else:
                pass

    def display_info(self):
        print("Veuillez entrer les informations suivantes :")
