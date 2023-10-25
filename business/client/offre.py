class Offre:
    def __init__(self, titre, domaine, lieu, type_contrat, lien_offre, salaire_minimum):
        self.id = None
        self.titre = titre
        self.domaine = domaine
        self.lieu = lieu
        self.type_contrat = type_contrat
        self.lien_offre = lien_offre
        self.salaire_minimum = salaire_minimum
        self._etre_en_favoris = False

    def mettre_en_favoris(self):
        self._etre_en_favoris = True
