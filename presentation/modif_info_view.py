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


class ModifInfoView(AbstractView):
    def __init__(self, user=None):
        self.user = user

    def make_choice(self):
        choix_info = [
            "nom",
            "age",
            "mail",
            "tel",
            "Ville",
            "code_postal",
        ]

        question = {
            "type": "list",
            "message": "Choisissez un élément à modifier :",
            "choices": choix_info,
        }
        answers = prompt([question])

        if answers[0] == "retour":
            from presentation.start_view import StartView

            return StartView

        else:
            print(answers[0])
            question = {
                "type": "input",
                "name": "nouv",
                "message": f"Nouveau {answers[0]}:",
            }
            from business.dao.utilisateur_dao import (
                UtilisateurDao,
            )

            utilisateurdao = UtilisateurDao()
            utilisateurdao.update_user_info(
                self.user.id, answers[0], prompt(question)["nouv"]
            )
            utils = utilisateurdao.recuperer_utilisateur(self.user.id)
            excluded_fields = ["id_compte_utilisateur", "mdp", "sel"]

            for record in utils:
                for i, (key, value) in enumerate(record.items()):
                    if key not in excluded_fields:
                        print(f"{i + 1}: {key}: {value}")
            input("Appuyez sur entrée pour continuer")

        quest = [
            {
                "type": "list",
                "name": "choix",
                "message": "",
                "choices": [
                    "Modifier une autre information",
                    "Retour",
                    "Se déconnecter",
                    "Quitter",
                ],
            }
        ]
        answ = prompt(quest)
        if answ["choix"] == "Modifier une autre information":
            return ModifInfoView(self.user)
        elif answ["choix"] == "Se déconnecter":
            self.user._connexion = False
            from presentation.start_view import StartView

            return StartView()
        elif answ["choix"] == "Retour":
            from presentation.info_view import InfoView

            return InfoView(self.user)
        else:
            pass

    def display_info(self):
        print("Veuillez entrer les informations suivantes :")
