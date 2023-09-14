class GestionCompte:  # relation de composition avec classe compte utilisateur
    def __init__(self, compte_utilisateur):
        self.compte_utilisateur = compte_utilisateur

    @property
    def modifier_nom(self, nouveau_nom):
        self.compte_utilisateur.nom = nouveau_nom

    @property
    def modifier_prenom(self, nouveau_prenom):
        self.compte_utilisateur.prenom = nouveau_prenom

    @property
    def modifier_age(self, nouvel_age):
        self.compte_utilisateur.age = nouvel_age

    @property
    def modifier_mail(self, nouveau_mail):
        self.compte_utilisateur.mail = nouveau_mail

    @property
    def modifier_tel(self, nouveau_tel):
        self.compte_utilisateur.tel = nouveau_tel

    @property
    def voir_mdp(self):
        return self.compte_utilisateur.__mdp

    def changer_mdp(self, nouveau_mdp):
        self.compte_utilisateur.__mdp = nouveau_mdp

    def modifier_ville(self, nouvelle_ville):
        self.compte_utilisateur.ville = nouvelle_ville

    def modifier_code_postal(self, nouveau_code_postal):
        self.compte_utilisateur.code_postal = nouveau_code_postal
