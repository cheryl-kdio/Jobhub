from InquirerPy import prompt

from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.services.utilisateur_service import (
    Utilisateur,
)  # Importation de la classe Utilisateur depuis le module utilisateur_service
from business.dao.utilisateur_dao import UtilisateurDao
from business.business_object.recherche import Recherche
from business.services.recherche_service import RechercheService
from tabulate import tabulate
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from business.business_object.profil_chercheur_emploi import ProfilChercheurEmploi
from business.dao.recherche_dao import RechercheDao

from business.dao.candidature_dao import CandidatureDao


class RechercheView(AbstractView):
    def __init__(self, langue, query_params=None, user=None):
        self.langue = langue
        self.user = user
        self.query_params = {} if query_params is None else query_params
        self.query_params["results_per_page"] = 20
        self.__questions = [
            {
                "type": "input",
                "name": "mot_cle",
                "message": (
                    "Enter the job title or keywords:"
                    if self.langue == "anglais"
                    else "Entrez l'intitulé du poste ou des mots-clés (séparés par des espaces) : "
                ),
            },
        ]

    def make_choice(self):
        if len(self.query_params) == 1:
            answers = prompt(self.__questions)
            self.query_params["what"] = answers["mot_cle"]

        recherche = Recherche(query_params=self.query_params)
        r = RechercheService()
        print(
            "Resultats obtenus :" if self.langue == "français" else "Results obtained"
        )

        choix_offres = (
            [
                {
                    "name": str(i + 1) + ". " + offre.titre + "-" + offre.entreprise,
                    "value": offre,
                }
                for i, offre in enumerate(r.obtenir_resultats(recherche))
            ]
            + [
                {
                    "name": "Retour" if self.langue == "français" else "Return",
                    "value": None,
                }
            ]
            + [
                {
                    "name": "Sauvegarder la recherche ?"
                    if self.langue == "français"
                    else "Save the search",
                    "value": "sauv",
                }
            ]
        )

        question = {
            "type": "list",
            "message": (
                "Choose a job offer to view in detail:"
                if self.langue == "anglais"
                else "Choisissez une offre à détailler :"
            ),
            "choices": choix_offres,
        }
        answers = prompt([question])

        if answers[0] == "sauv":
            if self.user:
                a = RechercheDao().sauvegarder_recherche(recherche, self.user)
                if a:
                    print(
                        "Search saved successfully."
                        if self.langue == "anglais"
                        else "La recherche a bien été sauvegardée"
                    )
                    print(
                        "Resultats obtenus :"
                        if self.langue == "français"
                        else "Results obtained"
                    )

                    choix_offres = [
                        {
                            "name": str(i + 1)
                            + ". "
                            + offre.titre
                            + "-"
                            + offre.entreprise,
                            "value": offre,
                        }
                        for i, offre in enumerate(r.obtenir_resultats(recherche))
                    ] + [
                        {
                            "name": "Retour" if self.langue == "français" else "Return",
                            "value": None,
                        }
                    ]
                    question = {
                        "type": "list",
                        "message": (
                            "Choose a job offer to view in detail:"
                            if self.langue == "anglais"
                            else "Choisissez une offre à détailler :"
                        ),
                        "choices": choix_offres,
                    }
                    answers = prompt([question])

                else:
                    print(
                        "La recherche est déjà sauvegardé"
                        if self.langue == "français"
                        else "Search is already saved"
                    )
                    print(
                        "Resultats obtenus :"
                        if self.langue == "français"
                        else "Results obtained"
                    )

                    choix_offres = [
                        {
                            "name": str(i + 1)
                            + ". "
                            + offre.titre
                            + "-"
                            + offre.entreprise,
                            "value": offre,
                        }
                        for i, offre in enumerate(r.obtenir_resultats(recherche))
                    ] + [
                        {
                            "name": "Retour" if self.langue == "français" else "Return",
                            "value": None,
                        }
                    ]
                    question = {
                        "type": "list",
                        "message": (
                            "Choose a job offer to view in detail:"
                            if self.langue == "anglais"
                            else "Choisissez une offre à détailler :"
                        ),
                        "choices": choix_offres,
                    }
                    answers = prompt([question])

            else:
                print(
                    "You must be logged in to access this feature."
                    if self.langue == "anglais"
                    else "Vous devez être connecté pour accéder à cette fonctionnalité"
                )
                from presentation.start_view import StartView

                return StartView()

        if not answers[0]:
            if not self.user:
                from presentation.start_view import StartView

                return StartView(self.langue)
            else:
                from presentation.user_view import UserView

                return UserView(user=self.user, langue=self.langue)

        else:
            print(answers[0])

            favoris = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "oui",
                        "message": "Mettre en favoris"
                        if self.langue == "français"
                        else "Add to favorites",
                        "default": False,
                    }
                ]
            )
            if favoris["oui"]:
                if self.user:
                    from business.dao.offre_dao import OffreDao

                    OffreDao().ajouter_offre(offre=answers[0], utilisateur=self.user)
                    print(
                        "L'offre a bien été mis en favoris !"
                        if self.langue == "français"
                        else "The offer has been successfully added to favorites!"
                    )
                else:
                    print(
                        "Vous devez être connecté pour accéder à cette fonctionnalité"
                        if self.langue == "français"
                        else "You must be logged in to access this feature."
                    )
                    from presentation.start_view import StartView

                    return StartView(langue=self.langue)
            candidater = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "oui",
                        "message": "Envoyer sa candidature"
                        if self.langue == "français"
                        else "Send your application",
                        "default": False,
                    }
                ]
            )
            if candidater["oui"]:
                if self.user:
                    CandidatureDao().candidater(offre=answers[0], utilisateur=self.user)
                    print(
                        "Candidature effectuée"
                        if self.langue == "français"
                        else "Application submitted"
                    )
                else:
                    print(
                        "You must be logged in to access this feature."
                        if self.langue == "anglais"
                        else "Vous devez être connecté pour accéder à cette fonctionnalité"
                    )
                    from presentation.start_view import StartView

                    return StartView()

            autre_recherche = prompt(
                [
                    {
                        "type": "confirm",
                        "name": "continue",
                        "message": "Faire une autre recherche ?"
                        if self.langue == "français"
                        else "Start another research",
                        "default": True,
                    }
                ]
            )
            if autre_recherche["continue"]:
                return RechercheView(self.user)

            else:
                if not self.user:
                    from presentation.start_view import StartView

                    return StartView(langue=self.langue)
                else:
                    from presentation.user_view import UserView

                    return UserView(user=self.user, langue=self.langue)

    def display_info(self):
        pass
