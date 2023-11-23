import unittest
from unittest.mock import patch
from business.business_object.compte_utilisateur import CompteUtilisateur
from business.services.utilisateur_service import Utilisateur


class TestCompteUtilisateur(unittest.TestCase):
    def setUp(self):
        # Créer une instance de CompteUtilisateur
        self.compte_utilisateur = CompteUtilisateur(
            id=1,
            mdp="mot_de_passe",
            nom="John Doe",
            age=30,
            mail="john@example.com",
            tel=1234567890,
            ville="Ville",
            code_postal=12345,
        )

    def test_initial_attributes(self):
        # vérification attributs
        self.assertEqual(self.compte_utilisateur.id, 1)
        self.assertEqual(self.compte_utilisateur.mdp, "mot_de_passe")
        self.assertEqual(self.compte_utilisateur.nom, "John Doe")
        self.assertEqual(self.compte_utilisateur.age, 30)
        self.assertEqual(self.compte_utilisateur.mail, "john@example.com")
        self.assertEqual(self.compte_utilisateur.tel, 1234567890)
        self.assertEqual(self.compte_utilisateur.ville, "Ville")
        self.assertEqual(self.compte_utilisateur.code_postal, 12345)
        self.assertEqual(self.compte_utilisateur._connexion, False)

    def test_deconnexion(self):
        self.compte_utilisateur._connexion = True

        compte_utilisateur_service = Utilisateur()

        # Utilisez patch pour simuler la sortie utilisateur
        with patch("builtins.print") as mock_print:
            # Appelez la méthode de déconnexion
            compte_utilisateur_service.deconnexion(self.compte_utilisateur)

            # Vérifiez que le message de déconnexion est imprimé
            mock_print.assert_called_with(f"A bientôt {self.compte_utilisateur.nom}")
            # Vérifiez que l'attribut _connexion est modifié
            self.assertEqual(self.compte_utilisateur._connexion, False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
