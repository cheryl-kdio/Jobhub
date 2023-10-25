class Offre:
    def __init__(
        self,
        titre,
        domaine,
        lieu,
        type_contrat,
        lien_offre,
        salaire_minimum,
        etre_en_favoris=False,
    ):
        self.titre = titre
        self.domaine = domaine
        self.lieu = lieu
        self.type_contrat = type_contrat
        self.lien_offre = lien_offre
        self.salaire_minimum = salaire_minimum
        self.etre_en_favoris = etre_en_favoris

    def __str__(self):
        return f"Offre: {self.titre} - {self.domaine} - {self.lieu} - {self.type_contrat} - {self.lien_offre} - {self.salaire_minimum} - {self.etre_en_favoris}"

    def mettre_en_favoris(self):
        self.etre_en_favoris = True
