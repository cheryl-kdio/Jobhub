class ProfilChercheurEmploi:
    def __init__(
        self,
        nom,
        mots_cles=None,
        lieu=None,
        salaire_minimum=None,
        distance=None,
        type_contrat=None,
        id_profil_chercheur_emploi=None,
    ):
        self.id_profil_chercheur_emploi = id_profil_chercheur_emploi
        self.nom = nom
        self.mots_cles = mots_cles
        self.lieu = lieu
        self.distance = distance
        self.type_contrat = type_contrat
        
        # Define the query_params dictionary with only truthy values
        self.query_params = {
            "what": self.mots_cles,
            "where": self.lieu,
            "distance": self.distance,
            "full_time":1 if self.type_contrat=="TEMPS PLEIN" else 0,
            "part_time":1 if self.type_contrat=="TEMPS PARTIEL" else 0,
            "contract":1 if self.type_contrat=="CDD" else 0,
            "permanent":1 if self.type_contrat=="CDI" else 0,
        }
        self.query_params = {k: v for k, v in self.query_params.items() if v}

