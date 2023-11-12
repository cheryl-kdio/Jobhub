import os
import time

from unittest import TestCase, TextTestRunner, TestLoader
from business.dao.offre_dao import OffreDao
from business.client.compte_utilisateur import CompteUtilisateur
from business.client.offre import Offre
from business.services.utilisateur_service import Utilisateur


class TestOffreDao(TestCase):
    def test_supprimer_offre(self):
        # GIVEN

        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        offre = Offre(
            titre="test",
            domaine="dev",
            lieu="spdn",
            type_contrat="CDI",
            entreprise="nike",
            id_offre=1,
        )
        dao = OffreDao()

        # WHEN

        result = dao.supprimer_offre(offre)

        # THEN

        self.assertTrue(
            result
        )  # Assurez-vous que la méthode retourne True ce qui signifie qu'elle s'est bien supprimé

    def test_sauvegarder_offre(self):
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        offre = Offre(
            titre="test",
            domaine="dev",
            lieu="spdn",
            type_contrat="CDI",
            entreprise="nike",
            id_offre=1,
        )
        dao = OffreDao()

        # WHEN

        result = dao.ajouter_offre(offre, pierre)

        # THEN

        self.assertTrue(result)  # Assurez-vous que la méthode retourne TRUE

    def test_deja_favoris(self):
        # GIVEN
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        offre = Offre(
            titre="test",
            domaine="dev",
            lieu="spdn",
            type_contrat="CDI",
            entreprise="nike",
            id_offre=1,
        )
        dao = OffreDao()

        # WHEN

        result = dao.deja_favoris(offre, pierre)

        # THEN

        self.assertIsNotNone(result)  # Assurez-vous que la méthode retourne True

    def test_voir_favoris(self):
        # GIVEN
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        dao = OffreDao()
        # WHEN

        result = dao.voir_favoris(pierre)

        # THEN
        self.assertEqual(
            len(result), 1
        )  # Assurez-vous que la méthode retourne une liste avec une recherche

    def test_si_sauvegarde_en_plus(self):
        # GIVEN
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        offre = Offre(
            titre="test",
            domaine="dev",
            lieu="spdn",
            type_contrat="CDI",
            entreprise="nike",
            id_offre=1,
        )
        dao = OffreDao()

        # WHEN

        result = dao.ajouter_offre(offre, pierre)

        # THEN

        self.assertFalse(result)  # Assurez-vous que la méthode retourne False


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestOffreDao)
    )
