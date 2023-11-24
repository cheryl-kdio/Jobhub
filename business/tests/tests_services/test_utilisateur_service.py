from unittest import TestCase, TextTestRunner, TestLoader
from business.services.utilisateur_service import (
    Utilisateur,
)
from business.dao.utilisateur_dao import UtilisateurDao
from business.business_object.compte_utilisateur import CompteUtilisateur


class TestUtilisateurService(TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur()

    def test_01_create_account(self):
        self.utilisateur.create_account(
            "Antoine", "antoinejarry19@gmail.com", "Antoine53", "Antoine53"
        )
        result2 = UtilisateurDao().check_email_unique("antoinejarry19@gmail.com")
        self.assertFalse(
            result2
        )  # Doit retourner False si unique et déjà dans la base de données

    def test_02_se_connecter(self):
        result = self.utilisateur.se_connecter("antoinejarry19@gmail.com", "Antoine53")
        self.assertTrue(
            result
        )  # Doit être True car correspond bien à notre utilisateur crée avant

    def test_03_invalid_se_connecter(self):
        result = self.utilisateur.se_connecter("antoinejarry19@gmail.com", "Antoine")
        self.assertFalse(result)  # Doit retourner False car pas le bon password


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestUtilisateurService)
    )
