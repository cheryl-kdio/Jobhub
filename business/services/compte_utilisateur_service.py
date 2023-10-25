from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.utilisateur_dao import UtilisateurDao


class CompteUtilisateurService:
    def supprimerCompte(self, compte_utilisateur: CompteUtilisateur) -> bool:
        "Supprimer le compte d'un CompteUtilisateur"
        return UtilisateurDao().supprimer(compte_utilisateur)

    def deconnexion(self, compte_utilisateur: CompteUtilisateur) -> bool:
        "Déconnecter un CompteUtilisateur"
        name = compte_utilisateur.nom
        print(f"A bientôt {name}")
        compte_utilisateur._connexion = False

    def modifierInfo(
        self,
        compte_utilisateur: CompteUtilisateur,
        nom=None,
        age=None,
        mail=None,
        tel=None,
        ville=None,
        code_postal=None,
    ) -> bool:
        "Modifier le nom d'un CompteUtilisateur"
        id = compte_utilisateur.id

        UtilisateurDao().update(
            id,
            nom=nom,
            age=age,
            mail=mail,
            tel=tel,
            ville=ville,
            code_postal=code_postal,
        )
