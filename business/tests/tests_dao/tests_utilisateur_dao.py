from business.dao.utilisateur_dao import UtilisateurDao
from unittest import TestCase, TextTestRunner, TestLoader
from business.client.compte_utilisateur import CompteUtilisateur
from business.services.utilisateur_service import Utilisateur


class TestUtilisateurDao(TestCase):
    def test_01__add_db(self):
        UtilisateurDao().add_db(
            name_user="cheryl",
            mail="ck@gmail.com",
            password="Patate12",
            sel="xbZb3OJ5InH9buJR",
        )

        result = UtilisateurDao().check_email_unique("ck@gmail.com")

        self.assertFalse(result)  # Doit retourner FALSE normalement

    def test_02_get_mail(self):
        result = UtilisateurDao().get_mail()

        self.assertEqual(result, "ck@gmail.com")

    def test_03_get_salt_mdp(self):
        result = UtilisateurDao().get_salt_mdp("ck@gmail.com")

        self.assertEqual(result, "xbZb3OJ5InH9buJR")

    def test_04_get_value_from_mail(self):
        value = "nom"

        result = UtilisateurDao().get_value_from_mail("ck@gmail.com", value)

        self.assertEqual(result, "cheryl")

    def test_05_drop_utilisateur(self):
        UtilisateurDao().drop_id(1)

        result = UtilisateurDao().check_mail("ck@gmail.com")

        self.assertFalse(result)

    def test_06_iterer_donnee(self):
        result = UtilisateurDao().iterer_donnees()

        self.assertNone(result)

    def test_07_recup_utilisateur(self):
        result = UtilisateurDao().recuperer_utilisateur(1)

        self.assertEqual(len(result), 1)

    def test_08_afficher_db(self):
        result = UtilisateurDao().afficher_db()

        self.assertEqual(len(result), 1)

    def test_09_verif_connexion(self):
        result = UtilisateurDao().verif_connexion("ck@gmail.com", "Patate12")

        self.assertTrue(result)

    def test_10_update(self):
        UtilisateurDao.update(1, nom="Cheryl_ENSAI")

        result = UtilisateurDao().get_value_from_mail("ck@gmail.com", "nom")

        self.assertEqual(result, "Cheryl_ENSAI")

    def test_11_supprimer(self):
        utilisateur = CompteUtilisateur(mdp="Patate12", nom="cheryl")

        result = UtilisateurDao().supprimer(utilisateur)

        self.assertTrue(result)

    def test_12_check_mail(self):
        result = UtilisateurDao().check_mail("ck@gmail.com")

        self.assertFalse(result)

    def test_13_check_mail_valide(self):
        result = UtilisateurDao().check_email_valide("ck@gmail.com")

        self.assertTrue(result)

    def test_14_check_mail_unique(self):
        result = UtilisateurDao().check_email_unique("ck@gmail.com")

        self.assertTrue(result)

    def test_15_check_mdp_valide(self):
        result = UtilisateurDao().check_mdp_valide("Patate12")

        self.assertTrue(result)

    def test_16_check_mdp_egal(self):
        utilisateur = CompteUtilisateur(mdp="Patate12", nom="cheryl")

        result = UtilisateurDao().check_mdp_egal("Patate12", utilisateur.mdp)

        self.assertTrue(result)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestUtilisateurDao)
    )
