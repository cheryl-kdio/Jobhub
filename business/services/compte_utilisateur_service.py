from business.client.compte_utilisateur import CompteUtilisateur
from dao.CompteUtilisateur_dao import CompteUtilisateurDao


class CompteUtilisateurService:
    def supprimerCompte(self, CompteUtilisateur) -> bool:
        "Supprimer le compte d'un CompteUtilisateur"
        return CompteUtilisateurDao().supprimer(CompteUtilisateur)

    def deconnexion(self) -> bool:
        "Déconnecter un CompteUtilisateur"
        CompteUtilisateur()._connexion = False

    # def modifier_nom(self, nom) -> bool:
    #     "Modifier le nom d'un CompteUtilisateur"
    #     CompteUtilisateurDao().update(nom)

    # def modifier_prenom(self, prenom) -> bool:
    #     "Modifier le prénom d'un CompteUtilisateur"
    #     CompteUtilisateurDao().update(prenom)

    # def modifier_age(self, age) -> bool:
    #     "Modifier l'âge d'un CompteUtilisateur"
    #     CompteUtilisateurDao().update(age)

    # def modifier_mail(self, mail) -> bool:
    #     "Modifier le mail d'un CompteUtilisateur"
    #     CompteUtilisateurDao().update(mail)

    # def modifier_tel(self, tel) -> bool:
    #     "Modifier le téléphone d'un CompteUtilisateur"
    #     CompteUtilisateurDao().update(tel)

    # def changer_mdp(self, mdp) -> bool:
    #     "Modifier le mot de passe d'un CompteUtilisateur"
    #     CompteUtilisateurDao().update(mdp)

    # def modifier_ville(self, ville) -> bool:
    #     "Modifier la ville d'un CompteUtilisateur"
    #     CompteUtilisateurDao().update(ville)

    # def modifier_code_postal(self, code_postal) -> bool:
    #     "Modifier le code postal d'un CompteUtilisateur"
    #     CompteUtilisateurDao().update(code_postal)
