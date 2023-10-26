import unittest
from unittest.mock import MagicMock, patch
from business.services.recherche_service import (
    RechercheService,
)  # Remplacez "your_module" par le nom de votre module
from business.client.offre import Offre
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.recherche_dao import RechercheDao


class TestRechercheService(unittest.TestCase):
    def setUp(self):
        self.recherche_service = RechercheService()

    def test_sauvegarder_recherche(self):
        recherche_dao = MagicMock()
        RechercheDao.sauvegarder_recherche = recherche_dao
        recherche = Recherche(response=MagicMock())
        utilisateur = CompteUtilisateur()
        nom_recherche = "Ma Recherche"

        self.recherche_service.sauvegarder_recherche(
            nom_recherche, recherche, utilisateur
        )
        recherche_dao.assert_called_with(nom_recherche, recherche, utilisateur)

    def test_supprimer_recherche(self):
        recherche_dao = MagicMock()
        RechercheDao.supprimer_recherche = recherche_dao
        recherche = Recherche()

        self.recherche_service.supprimer_recherche(recherche)
        recherche_dao.assert_called_with(recherche)

    def test_obtenir_resultats(self):
        recherche = Recherche(response=MagicMock(status_code=200))
        job1 = {
            "title": "Job 1",
            "category": {"label": "Category 1"},
            "location": {"display_name": "Location 1"},
            "contract_type": "Contract Type 1",
            "redirect_url": "URL 1",
            "salary_min": "Salary Min 1",
        }
        job2 = {
            "title": "Job 2",
            "category": {"label": "Category 2"},
            "location": {"display_name": "Location 2"},
            "contract_type": "Contract Type 2",
            "redirect_url": "URL 2",
            "salary_min": "Salary Min 2",
        }
        recherche.response.json.return_value = {"results": [job1, job2]}

        offres = self.recherche_service.obtenir_resultats(recherche)
        self.assertEqual(len(offres), 2)
        self.assertTrue(all(isinstance(offre, Offre) for offre in offres))

    def test_obtenir_resultats_invalid_response(self):
        recherche = Recherche(response=MagicMock(status_code=404))
        offres = self.recherche_service.obtenir_resultats(recherche)
        self.assertEqual(offres, [])

    def test_afficher_offres(self):
        recherche = Recherche(response=MagicMock(status_code=200))
        job1 = {
            "title": "Job 1",
            "category": {"label": "Category 1"},
            "location": {"display_name": "Location 1"},
            "contract_type": "Contract Type 1",
            "redirect_url": "URL 1",
            "salary_min": "Salary Min 1",
        }
        job2 = {
            "title": "Job 2",
            "category": {"label": "Category 2"},
            "location": {"display_name": "Location 2"},
            "contract_type": "Contract Type 2",
            "redirect_url": "URL 2",
            "salary_min": "Salary Min 2",
        }
        recherche.response.json.return_value = {"results": [job1, job2]}

        with patch("builtins.print") as mock_print, patch(
            "tabulate.tabulate"
        ) as mock_tabulate:
            self.recherche_service.afficher_offres(recherche)
            mock_tabulate.assert_called_with(
                mock_print, headers="keys", tablefmt="pretty"
            )

    def test_afficher_offres_no_results(self):
        recherche = Recherche(response=MagicMock(status_code=404))
        with patch("builtins.print") as mock_print, patch(
            "tabulate.tabulate"
        ) as mock_tabulate:
            self.recherche_service.afficher_offres(recherche)
            mock_tabulate.assert_not_called()


if __name__ == "__main__":
    unittest.main()
