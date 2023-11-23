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
    def __init__(self, pce, langue, user=None):
        self.pce = pce
        self.user = user
        self.langue = langue

    def make_choice(self):
        choix_profil = [
            "nom",
            "mots_cles",
            "lieu",
            "distance",
            "type_contrat",
        ]
        translated_choices = (
            [
                "Name",
                "Keywords",
                "Location",
                "Distance",
                "Contract Type",
            ]
            if self.langue == "anglais"
            else [
                "Nom",
                "Mots-clés",
                "Lieu",
                "Distance",
                "Type de contrat",
            ]
        )

        question = {
            "type": "list",
            "message": (
                "Choose an element to modify:"
                if self.langue == "anglais"
                else "Choisissez un élément à modifier :"
            ),
            "choices": translated_choices,
        }
        answers = prompt([question])

        if answers[0] == "retour":
            from presentation.start_view import StartView

            return StartView()

        else:
            real_choice = choix_profil[translated_choices.index(answers[0])]
            question = {
                "type": "input",
                "name": "nouv",
                "message": (
                    f"New {answers[0]}:"
                    if self.langue == "anglais"
                    else f"Nouveau {answers[0]} :"
                ),
            }
            from business.dao.profil_chercheur_emploi_dao import (
                ProfilChercheurEmploiDao,
            )

            pced = ProfilChercheurEmploiDao()
            pced.maj(
                self.pce.profil_chercheur_emploi["profil"].id_profil_chercheur_emploi,
                real_choice,
                prompt(question)["nouv"],
            )

            utils = pced.voir_profil_chercheur_emploi(self.user)

            for i, profil in enumerate(utils, 1):
                print(f"Profile {i}:")
                print(f"ID: {profil.id_profil_chercheur_emploi}")
                print(
                    f"Name: {profil.nom}"
                    if self.langue == "anglais"
                    else f"Nom: {profil.nom}"
                )
                print(
                    f"Keywords: {profil.mots_cles}"
                    if self.langue == "anglais"
                    else f"Mots-clés: {profil.mots_cles}"
                )
                print(
                    f"Location: {profil.lieu}"
                    if self.langue == "anglais"
                    else f"Lieu: {profil.lieu}"
                )
                print(
                    f"Distance: {profil.distance}"
                    if self.langue == "anglais"
                    else f"Distance: {profil.distance}"
                )
                print(
                    f"Contract Type: {profil.type_contrat}"
                    if self.langue == "anglais"
                    else f"Type de contrat: {profil.type_contrat}"
                )
                print("\n")

            input(
                "Press Enter to continue"
                if self.langue == "anglais"
                else "Appuyez sur entrée pour continuer"
            )
            questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": (
                        "Choose an option:"
                        if self.langue == "anglais"
                        else "Choisissez une option:"
                    ),
                    "choices": [
                        "Modify another parameter",
                        "Log out",
                        "Return",
                        "Quit",
                    ]
                    if self.langue == "anglais"
                    else [
                        "Modifier un autre paramètre",
                        "Se déconnecter",
                        "Retour",
                        "Quitter",
                    ],
                }
            ]
            answ = prompt(questions)
            if (
                answ["choix"] == "Modify another parameter"
                if self.langue == "anglais"
                else "Modifier un autre paramètre"
            ):
                return ModifProfileView(self.pce, user=self.user, langue=self.langue)

            elif (
                answ["choix"] == "Log out"
                if self.langue == "anglais"
                else "Se déconnecter"
            ):
                self.user._connexion = False
                from presentation.start_view import StartView

                return StartView(langue=self.langue)
            elif answ["choix"] == "Return" if self.langue == "anglais" else "Retour":
                from presentation.profile_view import ProfileView

                return ProfileView(user=self.user, langue=self.langue)
            else:
                pass

    def display_info(self):
        print(
            "Enter the following information:"
            if self.langue == "anglais"
            else "Veuillez entrer les informations suivantes :"
        )
