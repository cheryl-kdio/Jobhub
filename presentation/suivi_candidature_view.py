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


class CandidatureView(AbstractView):
    def __init__(self, user, langue):
        self.user = user
        self.langue = langue
        print(
            "Voici la liste des candidatures effectuées: \n"
            if self.langue == "français"
            else "Here is the list of job applications made: \n"
        )
        c = CandidatureDao()
        choix_offres = [
            {"name": offre.titre + "-" + offre.entreprise, "value": offre}
            for offre in c.voir_candidatures(self.user)
        ] + [{"name": "Retour", "value": None}]

        self.__questions = {
            "type": "list",
            "message": "Choisissez une candidature à détailler :"
            if self.langue == "français"
            else "Choose a job application to view in detail.",
            "choices": choix_offres,
        }

    def display_info(self):
        print(
            "Voici le détail de l'offre à laquelle vous avez candidaté :"
            if self.langue == "français"
            else "Here are the details of the job offer to which you have applied:"
        )

    def make_choice(self):
        answers = prompt(self.__questions)
        if answers[0] == "retour":
            from presentation.user_view import UserView

            return UserView(user=self.user, langue=self.langue)
        else:
            print(answers[0])
