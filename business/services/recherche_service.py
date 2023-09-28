import requests
from tabulate import tabulate
import os
import dotenv
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from dao.recherche_dao import RechercheDao


class RechercheService:
    def afficher_resultats(self, recherche: Recherche) -> str:
        if recherche.response.status_code == 200:
            data = recherche.response.json()
            jobs = data.get("results", [])

        else:
            print("Votre recherche ne peut pas être effectuée.")

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

    def sauvegarder_recherche(
        self, nom_recherche: str, recherche: Recherche, utilisateur: CompteUtilisateur
    ):
        RechercheDao().sauvegarder_recherche(nom_recherche, recherche, utilisateur)

    def supprimer_recherche(self, recherche: Recherche):
        RechercheDao().supprimer_recherche(recherche, utilisateur)
