import unittest
from unittest.mock import MagicMock, patch
from business.dao.recherche_dao import (
    RechercheDao,
)  # Remplacez "your_module" par le nom de votre module
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur


class TestRechercheDao(unittest.TestCase):
    def setUp(self):
        self.recherche_dao = RechercheDao()

    def test_supprimer_recherche(self):
        recherche = Recherche(
            id_recherche=1
        )  # Créez une instance de Recherche avec un ID factice
        utilisateur = CompteUtilisateur(
            id=1
        )  # Créez une instance de CompteUtilisateur avec un ID factice

        # Mock de la connexion et du curseur
        with patch("business.dao.recherche_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.rowcount = 1  # Suppression réussie

            result = self.recherche_dao.supprimer_recherche(recherche, utilisateur)
            self.assertTrue(result)  # Assurez-vous que la méthode retourne True

    def test_sauvegarder_recherche(self):
        nom_recherche = "Ma Recherche"
        recherche = Recherche(
            params="Paramètres", response="Résultat"
        )  # Créez une instance de Recherche
        utilisateur = CompteUtilisateur(
            id=1
        )  # Créez une instance de CompteUtilisateur avec un ID factice

        # Mock de la connexion et du curseur
        with patch("business.dao.recherche_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchone.return_value = {
                "id_recherche": 1
            }  # ID factice de la recherche ajoutée

            result = self.recherche_dao.sauvegarder_recherche(
                nom_recherche, recherche, utilisateur
            )
            self.assertTrue(result)  # Assurez-vous que la méthode retourne True

    def test_deja_favoris(self):
        recherche = Recherche(
            query_params="Paramètres"
        )  # Créez une instance de Recherche
        id_utilisateur = 1  # ID factice de l'utilisateur

        # Mock de la connexion et du curseur
        with patch("business.dao.recherche_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchone.return_value = None

            result = self.recherche_dao.deja_favoris(recherche, id_utilisateur)
            self.assertFalse(result)  # Assurez-vous que la méthode retourne False

    def test_voir_favoris(self):
        utilisateur = CompteUtilisateur(
            mail="test@example.com"
        )  # Créez un utilisateur factice

        # Mock de la connexion et du curseur
        with patch("business.dao.recherche_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchall.return_value = [
                {"query_params": "Paramètres"}
            ]  # Ici, vous pouvez simuler les données que vous attendez

            result = self.recherche_dao.voir_favoris(utilisateur)
            self.assertEqual(
                len(result), 1
            )  # Assurez-vous que la méthode retourne une liste avec une recherche


if __name__ == "__main__":
    unittest.main()
