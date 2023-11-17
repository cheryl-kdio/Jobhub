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
        choix_profil = [
            "nom",
            "mots_cles",
            "lieu",
            "distance",
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

            return StartView()

        else:
            question = {
                "type": "input",
                "name": "nouv",
                "message": f"Nouveau {answers[0]}:",
            }
            from business.dao.profil_chercheur_emploi_dao import (
                ProfilChercheurEmploiDao,
            )

            pced = ProfilChercheurEmploiDao()
            pced.maj(
                int(self.pce["profil"].split("ID: ")[1].split(",")[0]),
                answers[0],
                prompt(question)["nouv"],
            )

            utils = pced.voir_profil_chercheur_emploi(self.user)

            for i, profil in enumerate(utils, 1):
                print(f"Profil {i}:")
                print(f"ID: {profil.id_profil_chercheur_emploi}")
                print(f"Nom: {profil.nom}")
                print(f"Mots-clés: {profil.mots_cles}")
                print(f"Lieu: {profil.lieu}")
                print(f"Distance: {profil.distance}")
                print(f"Type de contrat: {profil.type_contrat}")
                print("\n")

            input("Appuyez sur entrée pour continuer")

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

                return ProfileView(self.user)
            else:
                pass

    def display_info(self):
        print("Veuillez entrer les informations suivantes :")
