class Offre:
    def __init__(self, titre, domaine, lieu, type_contrat, lien_offre, salaire_minimum, id_offre=None):
        self.id_offre = id_offre
        self.titre = titre
        self.domaine = domaine
        self.lieu = lieu
        self.type_contrat = type_contrat
        self.lien_offre = lien_offre
        self.salaire_minimum = salaire_minimum

    def mettre_en_favoris(self):
        self._etre_en_favoris = True
