import os
import time

from unittest import TestCase, TextTestRunner, TestLoader
from business.dao.candidature_dao import Candidature_Dao
from business.client.compte_utilisateur import CompteUtilisateur
from business.client.offre import Offre
from business.services.utilisateur_service import Utilisateur


class TestCandidatureDao(TestCase):
    def test_01__supprimer_candidature(self):
        # GIVEN
        offre = Offre(
            titre="test",
            domaine="dev",
            lieu="spdn",
            type_contrat="CDI",
            entreprise="nike",
            id_offre=1,
        )
        dao = Candidature_Dao()

        # WHEN

        result = dao.supprimer_candidature(offre)

        # THEN

        self.assertTrue(
            result
        )  # Assurez-vous que la méthode retourne True ce qui signifie qu'elle s'est bien supprimé

    def test_02_sauvegarder_Candidature(self):
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        offre = Offre(
            titre="test",
            domaine="dev",
            lieu="spdn",
            type_contrat="CDI",
            entreprise="nike",
            id_offre=1,
        )
        dao = Candidature_Dao()

        # WHEN

        result = dao.ajouter_candidature(offre, pierre)

        # THEN

        self.assertTrue(result)  # Assurez-vous que la méthode retourne TRUE

    def test_03_deja_favoris(self):
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
        dao = Candidature_Dao()

        # WHEN

        result = dao.deja_favoris(offre, pierre)

        # THEN

        self.assertIsNotNone(result)  # Assurez-vous que la méthode retourne True

    def test_04_voir_candidature(self):
        # GIVEN
        pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        dao = Candidature_Dao()
        # WHEN

        result = dao.voir_candidature(pierre)

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
        dao = Candidature_Dao()

        # WHEN

        result = dao.ajouter_candidature(offre, pierre)

        # THEN

        self.assertFalse(result)  # Assurez-vous que la méthode retourne False


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestCandidatureDao)
    )
