from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.utilisateur_dao import UtilisateurDao
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService
from business.dao.recherche_dao import RechercheDao
from business.services.utilisateur_service import Utilisateur
from business.dao.offre_dao import OffreDao
from business.dao.candidature_dao import CandidatureDao
from tabulate import tabulate

#Utilisateur().create_account("cheryl","ck@gmail.com","Patate12","Patate12")

print("Test de connexion")
pers = Utilisateur().se_connecter("ck@gmail.com", "Patate12")

#print("Test de modification info")
#Utilisateur().update(pers.id,nom="Cheryl",age="20",tel=330626340800, ville="Paris", code_postal=35170)
print("Test de recherche")

query_params = {
    "results_per_page": 20,
    "what": "python dev",
}

r = RechercheService()

print("Affichage des resultats")

offres = r.obtenir_resultats(Recherche(query_params=query_params))

data = {
    "n":[i + 1 for i, offre in enumerate(offres)],
    "Titre": [offre.titre for offre in offres],
    "Domaine": [offre.domaine for offre in offres],
    "Lieu": [offre.lieu for offre in offres],
    "Type de Contrat": [offre.type_contrat for offre in offres],
    "Entreprise " : [offre.entreprise for offre in offres]
}
print(tabulate(data, headers="keys", tablefmt="pretty"))
print("#####\n Candidater \n #####")

o = CandidatureDao()

num = int(input("Selectionner une offre à laquelle candidater [1-20]: "))

print("ajout favoris")
if o.candidater(offres[num-1], pers):
    print("candidature envoyée")
else:
    print("dejà candidat")

offres = o.voir_candidatures(pers)

data = {
    "n":[offre.id_offre for offre in offres],
    "Titre": [offre.titre for offre in offres],
    "Domaine": [offre.domaine for offre in offres],
    "Lieu": [offre.lieu for offre in offres],
    "Type de Contrat": [offre.type_contrat for offre in offres],
    "Entreprise " : [offre.entreprise for offre in offres]
}
print(tabulate(data, headers="keys", tablefmt="pretty"))

