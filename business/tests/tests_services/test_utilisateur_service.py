import unittest
from unittest.mock import MagicMock, patch
from business.services.utilisateur_service import (
    Utilisateur,
)  # Remplacez "your_module" par le nom de votre module
from business.dao.utilisateur_dao import UtilisateurDao
from business.client.compte_utilisateur import CompteUtilisateur


class TestUtilisateur(unittest.TestCase):
    def setUp(self):
        self.utilisateur = Utilisateur()

    def test_create_account(self):
        UtilisateurDao().check_mail = MagicMock(return_value=True)
        UtilisateurDao().add_db = MagicMock()
        getpass = MagicMock(return_value="test_password")
        random = MagicMock()
        random.choice = MagicMock(return_value="a")
        self.utilisateur.create_account()
        UtilisateurDao().add_db.assert_called()
        UtilisateurDao().check_mail.assert_called_with(MagicMock())
        random.choice.assert_called_with("abcdefghijklmnopqrstuvwxyz0123456789", k=16)
        getpass.assert_called_with("Mot de passe : ")

    def test_se_connecter(self):
        UtilisateurDao().verif_connexion = MagicMock(return_value=True)
        UtilisateurDao.get_value_from_mail = MagicMock(return_value="TestName")
        input = MagicMock(return_value="test@mail.com")
        getpass = MagicMock(return_value="test_password")
        CompteUtilisateur._connexion = False
        compte_utilisateur = self.utilisateur.se_connecter()
        self.assertTrue(CompteUtilisateur._connexion)
        self.assertEqual(compte_utilisateur.nom, "TestName")
        self.assertEqual(compte_utilisateur.id, "id_compte_utilisateur")
        self.assertEqual(compte_utilisateur.age, "age")
        self.assertEqual(compte_utilisateur.code_postal, "code_postal")
        self.assertEqual(compte_utilisateur.tel, "tel")
        self.assertEqual(compte_utilisateur.ville, "ville")

    def test_se_connecter_invalid(self):
        UtilisateurDao().verif_connexion = MagicMock(return_value=False)
        input = MagicMock(return_value="test@mail.com")
        getpass = MagicMock(return_value="test_password")
        CompteUtilisateur._connexion = False
        compte_utilisateur = self.utilisateur.se_connecter()
        self.assertFalse(CompteUtilisateur._connexion)
        self.assertIsNone(compte_utilisateur)


if __name__ == "__main__":
    unittest.main()
