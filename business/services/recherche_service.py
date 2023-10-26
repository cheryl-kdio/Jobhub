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
                )
                if offre:
                    offres.append(offre)

            return offres

        else:
            print("Votre recherche ne peut pas être effectuée.")

    def afficher_offres(self, recherche: Recherche):
        offres = self.obtenir_resultats(recherche)
        if offres:
            # Créez un DataFrame à partir de la liste des offres
            data = {
                "Titre": [offre.titre for offre in offres],
                "Domaine": [offre.domaine for offre in offres],
                "Lieu": [offre.lieu for offre in offres],
                "Type de Contrat": [offre.type_contrat for offre in offres],
                "Lien Offre": [offre.lien_offre for offre in offres],
                "Salaire Minimum": [offre.salaire_minimum for offre in offres],
                "Favoris": [offre._etre_en_favoris for offre in offres],
            }
            print(tabulate(data, headers="keys", tablefmt="pretty"))
        else:
            print("Aucune offre trouvée.")


query_params = {
    "results_per_page": 20,
    "what": "python dev",
    # "where": "london",
    # "sort_direction": "up",
    # "sort_by": "relevance",
    # "category": "IT Jobs",
    # "distance": 10,
    # "salary_min": 50000,
    # "salary_max": 100000,
    # "permanent": "1",
    # "part_time": "0",
    # "full_time": "1",
    # "contract": "0",
}

a = Recherche(query_params=query_params)
b = RechercheService().obtenir_resultats(a)
print(b)
