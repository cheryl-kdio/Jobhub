import requests
from tabulate import tabulate
import os
import dotenv


class Recherche:
    def __init__(
        self, country: str, query_params: dict, id_recherche: int
    ):  # Certains attributs sont potentiellement à mettre en privé/protection
        dotenv.load_dotenv(override=True)
        self.recherche = recherche
        self.country = country
        self.page_number = 1
        self.base_url = os.environ["HOST_WEBSERVICE"]
        self.endpoint = f"jobs/{self.country}/search/{self.page_number}"
        self.query_params = query_params
        self.params = {
            "app_id": os.environ["API_KEY"],
            "app_key": os.environ["API_ID"],
            **self.query_params,
        }
        self.response = requests.get(
            f"{self.base_url}{self.endpoint}", params=self.params
        )
