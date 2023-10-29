class ProfilChercheurEmploi:
    def __init__(
        self,
        lieu=None,
        domaine=None,
        salaire_minimum=None,
        salaire_maximum=None,
        type_contrat=None,
        id_profil_chercheur_emploi=None,
    ):
        self.id_profil_chercheur_emploi = id_profil_chercheur_emploi
        self.lieu = lieu
        self.domaine = domaine
        self.salaire_minimum = salaire_minimum
        self.salaire_maximum = salaire_maximum
        self.type_contrat = type_contrat
