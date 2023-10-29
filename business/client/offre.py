class Offre:
    def __init__(self, titre, domaine, lieu, type_contrat, lien_offre, salaire_minimum, id_offre=None):
        self.id_offre = id_offre
        self.titre = titre
        self.domaine = domaine
        self.lieu = lieu
        self.type_contrat = type_contrat
        self.lien_offre = lien_offre
        self.salaire_minimum = salaire_minimum

    def __str__(self):
        return (f"Offre: {self.titre}\n"
                f"Domaine: {self.domaine}\n"
                f"Lieu: {self.lieu}\n"
                f"Type de contrat: {self.type_contrat}\n"
                f"Salaire minimum: {self.salaire_minimum}\n"
                f"Lien: {self.lien_offre}")
