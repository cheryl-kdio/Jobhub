from unittest import TestCase, TextTestRunner, TestLoader
from business.services.recherche_service import (
    RechercheService,
)
from business.client.offre import Offre
from business.client.recherche import Recherche
from business.services.utilisateur_service import Utilisateur
from business.dao.recherche_dao import RechercheDao


class TestRechercheService(TestCase):
    def setUp(self):
        self.recherche_service = RechercheService()

    def test_01_sauvegarder_recherche(self):
        query_params = {
            "results_per_page": 20,
            "what": "python dev",
        }
        utilisateur = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        recherche = Recherche(query_params)

        result = self.recherche_service.sauvegarder_recherche(recherche, utilisateur)

        self.assertFalse(result)

    def test_02_supprimer_recherche(self):
        query_params = {
            "results_per_page": 20,
            "what": "python dev",
        }
        utilisateur = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        recherche = Recherche(query_params)

        result = self.recherche_service.supprimer_recherche(recherche, utilisateur)

        self.assertTrue(result)

    def test_03_obtenir_resultats(self):
        query_params = {
            "results_per_page": 20,
            "what": "python dev",
        }
        recherche = Recherche(query_params)

        result = self.recherche_service.obtenir_resultats(recherche)

        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestRechercheService)
    )
