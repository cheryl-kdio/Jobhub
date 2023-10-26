import unittest
from unittest.mock import MagicMock, patch
from business.dao.utilisateur_dao import (
    UtilisateurDao,
)  # Remplacez "your_module" par le nom de votre module


class TestUtilisateurDao(unittest.TestCase):
    def setUp(self):
        self.utilisateur_dao = UtilisateurDao()

    def test_add_db(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )

            name_user = "TestUser"
            mail = "testuser@example.com"
            password = "hashed_password"
            sel = "salt"

            result = self.utilisateur_dao.add_db(name_user, mail, password, sel)
            self.assertTrue(result)

    def test_get_mail(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchall.return_value = [
                {"mail": "test1@example.com"},
                {"mail": "test2@example.com"},
            ]

            result = self.utilisateur_dao.get_mail()
            self.assertEqual(result, ["test1@example.com", "test2@example.com"])

    def test_get_salt_mdp(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchone.return_value = {
                "mdp": "hashed_password",
                "sel": "salt",
            }

            result = self.utilisateur_dao.get_salt_mdp("testuser@example.com")
            self.assertEqual(result, {"mdp": "hashed_password", "sel": "salt"})

    def test_get_value_from_mail(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchone.return_value = {"value": "some_value"}

            result = self.utilisateur_dao.get_value_from_mail(
                "testuser@example.com", "value"
            )
            self.assertEqual(result, "some_value")

    def test_drop_id(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )

            result = self.utilisateur_dao.drop_id(123)
            self.assertTrue(result)

    def test_iterer_donnees(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchall.return_value = [
                {"id_compte_utilisateur": 1},
                {"id_compte_utilisateur": 2},
            ]

            result = self.utilisateur_dao.iterer_donnees()
            self.assertEqual(result, [1, 2])

    def test_recuperer_utilisateur(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchall.return_value = [
                {"col1": "value1", "col2": "value2"},
                {"col1": "value3", "col2": "value4"},
            ]

            result = self.utilisateur_dao.recuperer_utilisateur(1)
            self.assertEqual(
                result,
                [
                    {"col1": "value1", "col2": "value2"},
                    {"col1": "value3", "col2": "value4"},
                ],
            )

    def test_verif_connexion(self):
        with patch("business.dao.utilisateur_dao.getpass") as mock_getpass, patch(
            "your_module.PasswordHasher"
        ) as mock_password_hasher:
            mock_getpass.return_value = "user_password"
            mock_connection = mock_password_hasher.return_value
            mock_connection.verify.return_value = True

            result = self.utilisateur_dao.verif_connexion("testuser@example.com")
            self.assertTrue(result)

    def test_update(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )

            result = self.utilisateur_dao.update(
                1, nom="NewName", age=30, mail="newmail@example.com"
            )
            self.assertTrue(result)

    def test_supprimer(self):
        with patch("business.dao.utilisateur_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.rowcount = 1

            result = self.utilisateur_dao.supprimer(MagicMock())
            self.assertTrue(result)

    def test_check_mail(self):
        with patch(
            "business.dao.utilisateur_dao.UtilisateurDao.get_mail"
        ) as mock_get_mail:
            mock_get_mail.return_value = ["existing@example.com"]

            result = self.utilisateur_dao.check_mail("new@example.com")
            self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
