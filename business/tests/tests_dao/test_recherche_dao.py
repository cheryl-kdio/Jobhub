import time
from unittest import TestCase, TextTestRunner, TestLoader
from business.client.recherche import Recherche
from business.dao.db_connection import DBConnection

from business.services.recherche_service import RechercheService
from business.dao.recherche_dao import RechercheDao
from business.services.utilisateur_service import Utilisateur


class TestRechercheDao(TestCase):
    def test_01__supprimer_recherche(self):
        # GIVEN
        query_params = {
            "results_per_page": 20,
            "what": "python dev",
        }
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        recherche = Recherche(query_params)
        dao = RechercheDao()

        # WHEN

        result = dao.supprimer_recherche(recherche, pierre)

        # THEN

        self.assertTrue(
            result
        )  # Assurez-vous que la méthode retourne True ce qui signifie qu'elle s'est bien supprimé

    def test_02__sauvegarder_recherche(self):
        # GIVEN
        query_params = {
            "results_per_page": 20,
            "what": "python dev",
        }
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        recherche = Recherche(query_params)
        dao = RechercheDao()
        # WHEN

        result = dao.sauvegarder_recherche(recherche, pierre)

        # THEN

        self.assertTrue(result)  # Assurez-vous que la méthode retourne True

    def test_03_deja_favoris(self):
        # GIVEN
        query_params = {
            "results_per_page": 20,
            "what": "python dev",
        }
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        recherche = Recherche(query_params)
        dao = RechercheDao()

        # WHEN

        result = dao.deja_favoris(recherche, pierre.id)

        # THEN

        self.assertIsNotNone(result)  # Assurez-vous que la méthode retourne True

    def test_04_voir_favoris(self):
        # GIVEN
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        dao = RechercheDao()
        # WHEN

        result = dao.voir_favoris(pierre)

        # THEN
        self.assertEqual(
            len(result), 2
        )  # Assurez-vous que la méthode retourne une liste avec une recherche

    def test_05_si_sauvegarde_en_plus(self):
        # GIVEN
        query_params = {
            "results_per_page": 20,
            "what": "python dev",
        }
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        recherche = Recherche(query_params)
        dao = RechercheDao()

        # WHEN

        result = dao.sauvegarder_recherche(recherche, pierre)

        # THEN

        self.assertFalse(result)  # Assurez-vous que la méthode retourne False


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestRechercheDao)
    )
