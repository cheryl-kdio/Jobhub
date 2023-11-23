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
        max_label_length = max(len("Domaine"), len("Lieu"), len("Type de contrat"),
                            len("Salaire minimum"), len("Entreprise"), len("Description"), len("Lien"))

        def format_line(label, value):
            return f"{label:<{max_label_length}}: {value}"

        border = "- - - - - - - - - - - - - - - - - - - -\n" 
        return (
            f"{border}"
            f"{format_line('Offre', self.titre)}\n"
            f"{border}"
            f"{format_line('Domaine', self.domaine)}\n"
            f"{border}"
            f"{format_line('Lieu', self.lieu)}\n"
            f"{border}"
            f"{format_line('Type de contrat', self.type_contrat)}\n"
            f"{border}"
            f"{format_line('Salaire minimum', self.salaire_minimum)}\n"
            f"{border}"
            f"{format_line('Entreprise', self.entreprise)}\n"
            f"{border}"
            f"{format_line('Description', self.description)}\n"
            f"{border}"
            f"{format_line('Plus de détails', self.lien_offre)} \n"
            f"{border}"

        )

