from business.client.compte_utilisateur import CompteUtilisateur
from dao.CompteUtilisateur_dao import CompteUtilisateurDao


from business.client.compte_utilisateur import CompteUtilisateur


class CompteUtilisateurService:
    def supprimerCompte(self, compte_utilisateur: CompteUtilisateur) -> bool:
        "Supprimer le compte d'un CompteUtilisateur"
        return CompteUtilisateurDao().supprimer(compte_utilisateur)

    def deconnexion(self) -> bool:
        "Déconnecter un CompteUtilisateur"
        CompteUtilisateur()._connexion = False

    def modifierInfo(
        self, compte_utilisateur: CompteUtilisateur, type_info, nouvelle_valeur
    ) -> bool:
        "Modifier le nom d'un CompteUtilisateur"
        CompteUtilisateurDao().update(type_info, nouvelle_valeur, compte_utilisateur)
