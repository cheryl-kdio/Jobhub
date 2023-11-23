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
from business.dao.offre_dao import OffreDao

class CandidatureView(AbstractView):
    def __init__(self, user, langue):
        self.user = user
        self.langue = langue


    def display_info(self):
        pass

    def make_choice(self):
        c = OffreDao()
        choix_offres = [
            {"name": str(i+1)+"."+offre.titre + "-" + offre.entreprise, "value": offre}
            for i,offre in enumerate(c.voir_candidatures(self.user))
        ] + [{"name": "Retour", "value": None}]

        if len(choix_offres) == 1:
            print("Vous n'avez pas encore de candidatures \n")
            self.__questions=[
                    {
                        "type": "confirm",
                        "name": "oui",
                        "message": "Souhaiter vous lancer une recherche ?"
                        if self.langue == "français"
                        else "Do you want to start a reasearch ? ",
                        "default": True,
                    }
                ]
            answers=prompt(self.__questions)
            if answers['oui']:
                from presentation.recherche_view import RechercheView
                return RechercheView(langue=self.langue, user=self.user)
            else:
                from presentation.user_view import UserView
                return UserView(user=self.user, langue=self.langue) 
        else:
            self.__questions = {
                "type": "list",
                "message": "Choisissez une candidature à détailler : \n - - - - - - - - - - - - - - - - - - - -"
                if self.langue == "français"
                else "Choose a job application to view in detail.",
                "choices": choix_offres,
            }

            answers = prompt(self.__questions)
            if answers[0] == "Retour":
                from presentation.user_view import UserView
                return UserView(user=self.user, langue=self.langue)
            else:
                print(answers[0])
                self.__questions=[
                        {
                            "type": "confirm",
                            "name": "oui",
                            "message": "Retourner à la page d'acceuil"
                            if self.langue == "français"
                            else "Return to homepage",
                            "default": True,
                        }
                    ]
                answers=prompt(self.__questions)
                if answers['oui']:
                    from presentation.user_view import UserView
                    return UserView(user=self.user,langue=self.langue)
                else:
                    from presentation.suivi_candidature_view import CandidatureView
                    return CandidatureView(user=self.user,langue=self.langue)