import os
import time

from unittest import TestCase, TextTestRunner, TestLoader, mock
from business.dao.offre_dao import OffreDao

import unittest
from unittest.mock import MagicMock, patch
from business.dao.offre_dao import (
    OffreDao,
)  # Remplacez "your_module" par le nom de votre module
from business.client.compte_utilisateur import CompteUtilisateur
from business.client.offre import Offre


class TestOffreDao(TestCase):
    def setUp(self):
        self.offre_dao = OffreDao()
        Pierre = Utilisateur().create_account("cheryl", "ck@gmail.com", "Patate12", "Patate12") 
pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")

    def test_supprimer_offre(self):
        # Mock de la connexion et du curseur
        with patch("business.dao.offre_dao.DBConnection") as mock_connection:
            mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value.execute.return_value = (
                None
            )

            offre = Offre(id_offre=1)  # Créez une instance d'Offre avec un ID factice
            result = self.offre_dao.supprimer_offre(offre)
            self.assertTrue(result)  # Assurez-vous que la méthode retourne True

    def test_deja_favoris(self):
        # Mock de la connexion et du curseur
        with patch("business.dao.offre_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.fetchone.return_value = None

            offre = Offre(
                titre="Titre",
                domaine="Domaine",
                lieu="Lieu",
                type_contrat="CDI",
                lien_offre="Lien",
                salaire_minimum=50000,
                etre_en_favoris=True,
            )
            id_utilisateur = 1  # ID factice de l'utilisateur
            result = self.offre_dao.deja_favoris(offre, id_utilisateur)
            self.assertFalse(result)  # Assurez-vous que la méthode retourne False

    def test_ajouter_offre(self):
        # Mock de la connexion et du curseur
        with patch("business.dao.offre_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.execute.return_value = None
            mock_cursor.fetchone.return_value = {
                "id_offre": 1
            }  # ID factice de l'offre ajoutée

            offre = Offre(
                titre="Titre",
                domaine="Domaine",
                lieu="Lieu",
                type_contrat="CDI",
                lien_offre="Lien",
                salaire_minimum=50000,
                etre_en_favoris=True,
            )
            id_utilisateur = 1  # ID factice de l'utilisateur
            result = self.offre_dao.ajouter_offre(offre, id_utilisateur)
            self.assertTrue(result)  # Assurez-vous que la méthode retourne True

    def test_voir_favoris(self):
        # Mock de la connexion et du curseur
        with patch("business.dao.offre_dao.DBConnection") as mock_connection:
            mock_cursor = (
                mock_connection.return_value.connection.__enter__.return_value.cursor().__enter__.return_value
            )
            mock_cursor.execute.return_value = (
                None  # Ici, vous pouvez simuler les données que vous attendez
            )
            mock_cursor.fetchall.return_value = [
                {
                    "titre": "Titre",
                    "domaine": "Domaine",
                    "lieu": "Lieu",
                    "type_contrat": "CDI",
                    "lien_offre": "Lien",
                    "salaire_minimum": 50000,
                }
            ]

            utilisateur = CompteUtilisateur(
                mail="test@example.com"
            )  # Créez un utilisateur factice
            result = self.offre_dao.voir_favoris(utilisateur)
            self.assertEqual(
                len(result), 1
            )  # Assurez-vous que la méthode retourne une liste avec une offre


if __name__ == "__main__":
    unittest.main()
