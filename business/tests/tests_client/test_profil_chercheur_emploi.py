import unittest
from business.business_object.profil_chercheur_emploi import (
    ProfilChercheurEmploi,
)  # Assurez-vous d'importer correctement votre classe ProfilChercheurEmploi


class TestProfilChercheurEmploi(unittest.TestCase):
    def setUp(self):
        # Créer une instance de ProfilChercheurEmploi
        self.profil_chercheur = ProfilChercheurEmploi(
            id_profil_chercheur_emploi=1,
            lieu="Ville",
            domaine="Informatique",
            salaire_minimum=40000,
            salaire_maximum=60000,
            type_contrat="CDI",
        )

    def test_initial_attributes(self):
        # Vérification des attributs initiaux
        self.assertEqual(self.profil_chercheur.id_profil_chercheur_emploi, 1)
        self.assertEqual(self.profil_chercheur.lieu, "Ville")
        self.assertEqual(self.profil_chercheur.domaine, "Informatique")
        self.assertEqual(self.profil_chercheur.salaire_minimum, 40000)
        self.assertEqual(self.profil_chercheur.salaire_maximum, 60000)
        self.assertEqual(self.profil_chercheur.type_contrat, "CDI")


if __name__ == "__main__":
    unittest.main(verbosity=2)
