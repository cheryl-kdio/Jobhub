import requests
from tabulate import tabulate
import os
import dotenv
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.recherche_dao import RechercheDao


class RechercheService:
    def afficher_resultats(self, recherche) -> str:
        if recherche.response.status_code == 200:
            data = recherche.response.json()
            jobs = data.get("results", [])

            output = [
                {
                    "id": i + 1,
                    "Titre": job.get("title", ""),
                    "Entreprise": job.get("company", {}).get("display_name", ""),
                    "Lieu": job.get("location", {}).get("display_name", ""),
                    "Salaire min": job.get("salary_min", ""),
                    "Categorie": job.get("category", {}).get("label", ""),
                    # "redirect_url": job.get("redirect_url", ""),
                }
                for i, job in enumerate(jobs)
            ]

            print(tabulate(output, headers="keys", tablefmt="pretty"))

        else:
            print("Votre recherche ne peut pas être effectuée.")

    def sauvegarder_recherche(
        self, nom_recherche: str, recherche, utilisateur: CompteUtilisateur
    ):
        RechercheDao().sauvegarder_recherche(nom_recherche, recherche, utilisateur)

    def supprimer_recherche(self, recherche: Recherche):
        RechercheDao().supprimer_recherche(recherche, utilisateur)


query_params = {
    "results_per_page": 20,
    "what": "python dev",
    "where": "london",
    "sort_direction": "up",
    "sort_by": "relevance",
    "category": "IT Jobs",
    "distance": 10,
    "salary_min": 50000,
    "salary_max": 100000,
    "permanent": "1",
    "part_time": "0",
    "full_time": "1",
    "contract": "0",
}

a = Recherche(country="gb", query_params=query_params)
RechercheService().afficher_resultats(recherche=a)
