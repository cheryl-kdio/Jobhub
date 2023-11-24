from unittest import TestCase, TextTestRunner, TestLoader
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from business.business_object.profil_chercheur_emploi import ProfilChercheurEmploi
from business.services.utilisateur_service import Utilisateur


class TestProfilDao(TestCase):
    def test_01__supprimer_profil(self):
        # GIVEN
        profil = ProfilChercheurEmploi()
        dao = ProfilChercheurEmploiDao()

        # WHEN

        result = dao.supprimer_profil_chercheur_emploi(profil)

        # THEN

        self.assertTrue(
            result
        )  # Assurez-vous que la méthode retourne True ce qui signifie qu'elle s'est bien supprimé

    def test_02_ajouter_profil(self):
        # GIVEN
        profil = ProfilChercheurEmploi()
        utilisateur = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        dao = ProfilChercheurEmploiDao()

        # WHEN

        result = dao.ajouter_profil_chercheur_emploi(profil, utilisateur)

        # THEN

        self.assertTrue(result)  # Assurez-vous que la méthode retourne TRUE

    def test_03_deja_enregistré(self):
        # GIVEN
        profil = ProfilChercheurEmploi()
        utilisateur = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        dao = ProfilChercheurEmploiDao()

        # WHEN

        result = dao.deja_favoris(profil, utilisateur)

        # THEN

        self.assertIsNotNone(result)  # Assurez-vous que la méthode retourne True

    def test_04_voir_profil(self):
        # GIVEN
        utilisateur = Utilisateur().se_connecter("ck@gmail.com", "Patate12")
        dao = ProfilChercheurEmploiDao()

        # WHEN

        result = dao.voir_candidature(utilisateur)

        # THEN
        self.assertEqual(
            len(result), 1
        )  # Assurez-vous que la méthode retourne une liste avec une recherche

    def test_05_match_critere(self):
        profil = ProfilChercheurEmploi()
        dao = ProfilChercheurEmploiDao()

        # WHEN

        result = dao.match_criteres(profil)

        # THEN
        self.assertEqual(len(result), 1)

    def test_06_modifier_profil(self):
        profil = ProfilChercheurEmploi()
        dao = ProfilChercheurEmploiDao()

        # WHEN

        result = dao.modifier_profil_chercheur_emploi(profil)

        # THEN
        self.assertTrue(result)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestProfilDao)
    )
