class CompteUtilisateur:
    """
    Classe représentant un compte utilisateur

    Attributes
    ----------

    mdp : str
        Le mot de passe du compte utilisateur.
    nom : str
        Le nom du compte utilisateur.
    age : int
        L'âge du compte utilisateur calculé à partir de la date de naissance.
    mail : str, optional
        L'adresse e-mail du compte utilisateur (par défaut None).
    tel : int, optional
        Le numéro de téléphone du compte utilisateur (par défaut None).
    ville : str, optional
        La ville de résidence du compte utilisateur (par défaut None).
    code_postal : int, optional
        Le code postal de la ville de résidence du compte utilisateur (par défaut None).
    _connexion : bool
        Indique si le compte utilisateur est connecté (True) ou déconnecté (False).
    """

    def __init__(
        self,
        mdp: str,
        nom: str,
        id=None,
        age: int = None,
        mail: str = None,
        tel: int = None,
        ville: str = None,
        code_postal: int = None,
    ):
        self.id = id
        self.mdp = mdp
        self.nom = nom
        self.age = age
        self.mail = mail
        self.tel = tel
        self.ville = ville
        self.code_postal = code_postal
        self._connexion = False
