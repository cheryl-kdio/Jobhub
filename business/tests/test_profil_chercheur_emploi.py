from business.business_object.compte_utilisateur import CompteUtilisateur
from business.dao.utilisateur_dao import UtilisateurDao
from business.business_object.recherche import Recherche
from business.services.recherche_service import RechercheService
from business.dao.recherche_dao import RechercheDao
from business.services.utilisateur_service import Utilisateur
from business.dao.offre_dao import OffreDao
from business.dao.candidature_dao import CandidatureDao
from business.business_object.profil_chercheur_emploi import ProfilChercheurEmploi
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from tabulate import tabulate

# Utilisateur().create_account("cheryl","ck@gmail.com","Patate12","Patate12")

print("Test de connexion")
pers = Utilisateur().se_connecter("ck@gmail.com", "Patate12")

# print("Test de modification info")
# Utilisateur().update(pers.id,nom="Cheryl",age="20",tel=330626340800, ville="Paris", code_postal=35170)
print("Test de création profil emploi")

profil = ProfilChercheurEmploi(
    nom="test31",
    mots_cles="developpeur python",
    lieu="paris",
    distance=10,
    type_contrat="CDD",
)
p = ProfilChercheurEmploiDao()

print("ajout profil")
if p.ajouter_profil_chercheur_emploi(profil, pers):
    print("ajoutée")
else:
    print("non rajoutée")


print("match critères")

offres = p.match_criteres(profil)

data = {
    "n": [i + 1 for i, offre in enumerate(offres)],
    "Titre": [offre.titre for offre in offres],
    "Domaine": [offre.domaine for offre in offres],
    "Lieu": [offre.lieu for offre in offres],
    "Type de Contrat": [offre.type_contrat for offre in offres],
    "Entreprise ": [offre.entreprise for offre in offres],
}
print(tabulate(data, headers="keys", tablefmt="pretty"))
print("#####\n Voir profil \n #####")
print(profil.id_profil_chercheur_emploi)

offres = p.voir_profil_chercheur_emploi(pers)

data = {
    "n": [offre.id_profil_chercheur_emploi for offre in offres],
    "Titre": [offre.nom for offre in offres],
    "Lieu": [offre.lieu for offre in offres],
    "Type de Contrat": [offre.type_contrat for offre in offres],
}
print(tabulate(data, headers="keys", tablefmt="pretty"))
### Changer la maj et vérifier la suppression
# p.maj(offres[0])
