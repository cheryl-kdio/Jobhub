class ProfilChercheurEmploi:
    def __init__(
        self,
        lieu,
        domaine,
        salaire_minimum,
        salaire_maximum,
        type_contrat,
        id_profil_chercheur_emploi=None,
    ):
        self.id_profil_chercheur_emploi = id_profil_chercheur_emploi
        self.lieu = lieu
        self.domaine = domaine
        self.salaire_minimum = salaire_minimum
        self.salaire_maximum = salaire_maximum
        self.type_contrat = type_contrat
