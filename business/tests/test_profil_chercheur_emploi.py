from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.utilisateur_dao import UtilisateurDao
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService
from business.dao.recherche_dao import RechercheDao
from business.services.utilisateur_service import Utilisateur
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from business.client.profil_chercheur_emploi import ProfilChercheurEmploi
from tabulate import tabulate

print("Test de connexion")
pers = Utilisateur().se_connecter("ck@gmail.com", "Patate12")

print("Création profil chercheur emploi")
p=ProfilChercheurEmploiDao()
if p.ajouter_profil_chercheur_emploi(ProfilChercheurEmploi(lieu="Paris",), pers):
    print(True)


if p.ajouter_profil_chercheur_emploi(ProfilChercheurEmploi(lieu="Paris", domaine="Informatique", salaire_minimum=300,type_contrat="contract"), pers):
    print(True)
else:
    print(False)

if p.ajouter_profil_chercheur_emploi(ProfilChercheurEmploi(lieu="Paris", domaine="Informatique", salaire_minimum=300,type_contrat="contract"), pers):
    print(True)
else:
    print(False)

liste=p.voir_profil_chercheur_emploi(pers)
print(liste)

print("recherche")
offres=p.match_criteres(liste[0])
data = {
    "n":[i + 1 for i, offre in enumerate(offres)],
    "Domaine": [offre.domaine for offre in offres],
    "Lieu": [offre.lieu for offre in offres],
    "Type de Contrat": [offre.type_contrat for offre in offres],
}

print(tabulate(data, headers="keys", tablefmt="pretty"))

for i in range(len(liste)):
    p.supprimer_profil_chercheur_emploi(liste[i])

liste=p.voir_profil_chercheur_emploi(pers)
print(liste)

