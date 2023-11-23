import unittest
from unittest.mock import patch, Mock
from business.business_object.recherche import (
    Recherche,
)  # Assurez-vous d'importer correctement votre classe Recherche


class TestRecherche(unittest.TestCase):
    def setUp(self):
        # Créer une instance de Recherche
        self.query_params = {"param1": "value1", "param2": "value2"}
        self.recherche = Recherche(query_params=self.query_params, id_recherche=1)

    @patch("business.recherche.requests.get")
    def test_initial_attributes(self, mock_requests_get):
        # Configuration du mock pour simuler la réponse de la requête
        mock_response = Mock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response

        # Vérification des attributs initiaux
        self.assertEqual(self.recherche.id_recherche, 1)
        self.assertEqual(self.recherche.query_params, self.query_params)
        self.assertEqual(self.recherche.base_url, "votre_base_url_attendue")
        self.assertEqual(self.recherche.params["app_id"], "votre_api_id_attendu")
        self.assertEqual(self.recherche.params["app_key"], "votre_api_key_attendue")

        # Appel à la méthode qui effectue la requête
        self.recherche.response  # Cela devrait déclencher la requête

        # Vérification que la méthode requests.get a été appelée avec les paramètres attendus
        mock_requests_get.assert_called_once_with(
            "votre_base_url_attendue", params=self.recherche.params
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
