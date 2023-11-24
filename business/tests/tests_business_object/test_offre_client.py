import unittest
from business.business_object.offre import (
    Offre,
)  # Assurez-vous d'importer correctement votre classe Offre


class TestOffre(unittest.TestCase):
    def setUp(self):
        # Créer une instance de Offre
        self.offre = Offre(
            id_offre=1,
            titre="Titre de l'offre",
            domaine="Informatique",
            lieu="Ville",
            type_contrat="CDI",
            entreprise="Nom de l'entreprise",
            lien_offre="http://exemple.com/offre",
            salaire_minimum=50000,
            description="Description de l'offre",
        )

    def test_initial_attributes(self):
        # Vérification des attributs initiaux
        self.assertEqual(self.offre.id_offre, 1)
        self.assertEqual(self.offre.titre, "Titre de l'offre")
        self.assertEqual(self.offre.domaine, "Informatique")
        self.assertEqual(self.offre.lieu, "Ville")
        self.assertEqual(self.offre.type_contrat, "CDI")
        self.assertEqual(self.offre.entreprise, "Nom de l'entreprise")
        self.assertEqual(self.offre.lien_offre, "http://exemple.com/offre")
        self.assertEqual(self.offre.salaire_minimum, 50000)
        self.assertEqual(self.offre.description, "Description de l'offre")

    def test_str_method(self):
        # Vérification de la méthode __str__
        expected_output = (
            "Id_offre : 1\n"
            "+-----------------------------------+\n"
            "Offre: Titre de l'offre\n"
            "+-----------------------------------+\n"
            "Domaine: Informatique\n"
            "+-----------------------------------+\n"
            "Lieu: Ville\n"
            "+-----------------------------------+\n"
            "Type de contrat: CDI\n"
            "+-----------------------------------+\n"
            "Salaire minimum: 50000\n"
            "+-----------------------------------+\n"
            "Entreprise : Nom de l'entreprise\n"
            "+-----------------------------------+\n"
            "Description : Description de l'offre\n"
            "+-----------------------------------+\n"
            "Lien: http://exemple.com/offre"
        )
        self.assertEqual(str(self.offre), expected_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
