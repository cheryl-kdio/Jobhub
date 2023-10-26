import requests
from tabulate import tabulate
import os
import dotenv


class Recherche:
    def __init__(
        self,
        query_params: dict,
    ):  # Certains attributs sont potentiellement à mettre en privé/protection
        dotenv.load_dotenv(override=True)
        self.base_url = os.environ["HOST_WEBSERVICE"]
        self.query_params = query_params
        self.params = {
            "app_id": os.environ["API_ID"],
            "app_key": os.environ["API_KEY"],
            **self.query_params,
        }
        self.response = requests.get(f"{self.base_url}", params=self.params)
