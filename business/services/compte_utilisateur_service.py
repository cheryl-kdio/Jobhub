from business.client.compte_utilisateur import CompteUtilisateur
from dao.Utilisateur_dao import UtilisateurDao


class CompteUtilisateurService:
    def supprimerCompte(self, compte_utilisateur: CompteUtilisateur) -> bool:
        "Supprimer le compte d'un CompteUtilisateur"
        return UtilisateurDao().supprimer(compte_utilisateur)

    def deconnexion(self, compte_utilisateur: CompteUtilisateur) -> bool:
        "Déconnecter un CompteUtilisateur"
        compte_utilisateur()._connexion = False

    # def modifierInfo(
    #    self, compte_utilisateur: CompteUtilisateur, type_info, nouvelle_valeur
    # ) -> bool:
    #    "Modifier le nom d'un CompteUtilisateur"
    #    UtilisateurDao().update(type_info, nouvelle_valeur, compte_utilisateur)

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
        id = compte_utilisateur.id_compte_utilisateur

        UtilisateurDao().update(
            id,
            nom=nom,
            age=age,
            mail=mail,
            tel=tel,
            ville=ville,
            code_postal=code_postal,
        )
