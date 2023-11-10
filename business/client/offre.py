class Offre:
    def __init__(
        self,
        titre,
        domaine,
        lieu,
        type_contrat,
        entreprise,
        lien_offre=None,
        salaire_minimum=None,
        description=None,
        id_offre=None,
    ):
        self.id_offre = id_offre
        self.titre = titre
        self.domaine = domaine
        self.lieu = lieu
        self.type_contrat = type_contrat
        self.lien_offre = lien_offre
        self.salaire_minimum = salaire_minimum
        self.entreprise = entreprise
        self.description = description

    def __str__(self):
        return (
            f"Id_offre : {self.id_offre}\n"
            "+-----------------------------------+\n"
            f"Offre: {self.titre}\n"
            "+-----------------------------------+\n"
            f"Domaine: {self.domaine}\n"
            "+-----------------------------------+\n"
            f"Lieu: {self.lieu}\n"
            "+-----------------------------------+\n"
            f"Type de contrat: {self.type_contrat}\n"
            "+-----------------------------------+\n"
            f"Salaire minimum: {self.salaire_minimum}\n"
            "+-----------------------------------+\n"
            f"Entreprise : {self.entreprise}\n"
            "+-----------------------------------+\n"
            f"Description : {self.description}\n"
            "+-----------------------------------+\n"
            f"Lien: {self.lien_offre}"
        )
