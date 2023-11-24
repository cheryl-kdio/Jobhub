class ProfilChercheurEmploi:
    def __init__(
        self,
        nom,
        mots_cles=None,
        lieu=None,
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
    
    def __str__(self):
        labels = [
            "Nom de l'alerte", "Mots clés", "Ville", "Distance autour de la ville",
            "Type de contrat", "Query params"
        ]

        max_label_length = max(len(label) for label in labels)

        def format_line(label, value):
            return f"{label:<{max_label_length}}: {value}"

        border = "- - - - - - - - - - - - - - - - - - - -\n"

        return (
            border +
            format_line('Nom de l\'alerte', self.nom) + '\n' +
            border +
            format_line('Mots clés', self.mots_cles) + '\n' +
            border +
            format_line('Ville', self.lieu) + '\n' +
            border +
            format_line('Distance autour de la ville', self.distance) + '\n' +
            border +
            format_line('Type de contrat', self.type_contrat) + '\n' +
            border
        )


              

