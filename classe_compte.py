from datetime import datetime
from abc import ABC, abstractmethod


class Utilisateur(ABC):
    def __init__(self, id, mdp=None):
        self.id = id
        self.mdp = mdp

    @abstractmethod
    def alerte_candidature(self):
        pass


class CompteUtilisateur(Utilisateur):
    def __init__(
        self,
        id,
        mdp,
        nom,
        date_naissance,
        mail=None,
        tel=None,
        ville=None,
        code_postal=None,
    ):
        super().__init__(id, mdp)
        self.nom = nom  # str
        self.date_naissance = date_naissance  # Date de naissance au format "YYYY-MM-DD"
        self.age = (
            self.__calculer_age()
        )  # Appel de la méthode privée pour calculer l'âge
        self.mail = mail  # str
        self.tel = tel  # int
        self.ville = ville  # str
        self.code_postal = code_postal  # int
        self._connexion = True  # bool

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


# Exemple d'utilisation :
