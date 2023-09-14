import requests
from tabulate import tabulate
import os
import dotenv


class Recherche:
    def __init__(
        self, country: str
    ):  # Certains attributs sont potentiellement à mettre en privé/protection
        dotenv.load_dotenv(override=True)
        self.api_key = os.environ["API_KEY"]
        self.api_id = os.environ["API_ID"]
        self.country = country
        self.page_number = 1
        self.base_url = os.environ["HOST_WEBSERVICE"]
        self.endpoint = f"jobs/{self.country}/search/{self.page_number}"
        self.liste_recherches = {}

    def requeter_via_api(self, query_params: dict) -> dict:
        params = {"app_id": self.api_id, "app_key": self.api_key, **query_params}

        response = requests.get(f"{self.base_url}{self.endpoint}", params=params)

        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
        else:
            print(f"Echec de la requête - code {response.status_code}: {response.text}")
            return []

    def afficher_resultats(self, query_params: dict) -> str:
        jobs = self.requeter_via_api(query_params)

        output = [
            {
                "id": i + 1,
                "Titre": job.get("title", ""),
                "Entreprise": job.get("company", {}).get("display_name", ""),
                "Lieu": job.get("location", {}).get("display_name", ""),
                "Salaire min": job.get("salary_min", ""),
                "Salaire max": job.get("salary_max", ""),
                "Categorie": job.get("category", {}).get("label", ""),
                # "redirect_url": job.get("redirect_url", ""),
            }
            for i, job in enumerate(jobs)
        ]

        print(tabulate(output, headers="keys", tablefmt="pretty"))

    def sauvegarder_recherche(self, nom_recherche: str, query_params: dict):
        self.liste_recherches[nom_recherche] = query_params

    def supprimer_recherche(self, nom_recherche: str):
        if nom_recherche in self.liste_recherches:
            del self.liste_recherches[nom_recherche]


# Example usage:
if __name__ == "__main__":
    country = "fr"
    job_search = Recherche(country)

    query_params = {
        "results_per_page": 20,
        "what": "python dev",
        # Add additional parameters as needed
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

    job_search.afficher_resultats(query_params)
