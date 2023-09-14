from datetime import datetime
from Business_layer.Service_layer.utilisateur import Utilisateur


class CompteUtilisateur:
    """
    Classe représentant un compte utilisateur

    Attributes
    ----------
    id : int
        L'identifiant unique du compte utilisateur.
    mdp : str
        Le mot de passe du compte utilisateur.
    nom : str
        Le nom du compte utilisateur.
    date_naissance : str
        La date de naissance du compte utilisateur au format "YYYY-MM-DD".
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
        id: int,
        mdp: str,
        nom: str,
        date_naissance,
        mail: str = None,
        tel: int = None,
        ville: str = None,
        code_postal: int = None,
    ):
        self.id = id
        self.mdp = mdp
        self.nom = nom
        self.date_naissance = date_naissance  # Date de naissance au format "YYYY-MM-DD"
        self.age = (
            self.__calculer_age()
        )  # Appel de la méthode privée pour calculer l'âge
        self.mail = mail
        self.tel = tel
        self.ville = ville
        self.code_postal = code_postal
        self._connexion = True

    def alerte_candidature(self):
        pass

    def se_deconnecter(self):
        self._connexion = False

    def __calculer_age(self):  # Méthode privée pour calculer l'âge
        # Convertir la date de naissance en objet datetime
        date_naissance = datetime.strptime(self.date_naissance, "%Y-%m-%d")

        # Obtenir la date actuelle
        date_actuelle = datetime.now()

        # Calculer la différence entre la date actuelle et la date de naissance
        difference = date_actuelle - date_naissance

        # Extraire l'âge en années
        age = difference.days // 365

        return age
