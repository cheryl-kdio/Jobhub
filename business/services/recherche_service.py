import requests
from tabulate import tabulate
import os
import dotenv
from business.client.offre import Offre
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.recherche_dao import RechercheDao


class RechercheService:
    def sauvegarder_recherche(
        self, nom_recherche: str, recherche, utilisateur: CompteUtilisateur
    ):
        RechercheDao().sauvegarder_recherche(nom_recherche, recherche, utilisateur)

    def supprimer_recherche(self, recherche: Recherche):
        RechercheDao().supprimer_recherche(recherche, utilisateur)

    def obtenir_resultats(self, recherche: Recherche):
        offres = []
        if recherche.response.status_code == 200:
            jobs = recherche.response.json()["results"]
            for job in jobs:
                offre = Offre(
                    titre=job.get("title", ""),
                    domaine=job.get("category", {}).get("label", ""),
                    lieu=job.get("location", {}).get("display_name", ""),
                    type_contrat=job.get("contract_type", ""),
                    lien_offre=job.get("redirect_url", ""),
                    salaire_minimum=job.get("salary_min", ""),
                    entreprise=job.get("company", {}).get("display_name}", ""),
                    description=job.get("description", ""),
                )
                if offre:
                    offres.append(offre)

            return offres

        else:
            print("Votre recherche ne peut pas être effectuée.")
            return None
