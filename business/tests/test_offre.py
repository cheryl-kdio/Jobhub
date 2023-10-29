from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.utilisateur_dao import UtilisateurDao
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService
from business.dao.recherche_dao import RechercheDao
from business.services.utilisateur_service import Utilisateur
from business.dao.offre_dao import OffreDao
from tabulate import tabulate

# Utilisateur().create_account("cheryl","ck@gmail.com","Patate12","Patate12")

print("Test de connexion")
pers = Utilisateur().se_connecter("ck@gmail.com", "Patate12")

print("Test de recherche")

query_params = {"results_per_page": 20, "what": "python dev", "where": "london"}

r = RechercheService()

print("Affichage des resultats")

offres = r.obtenir_resultats(Recherche(query_params=query_params))

print(offres)

print("#####\n Mettre en favoris \n #####")

o = OffreDao()

print("ajout favoris")
if o.ajouter_offre(offres[0], pers):
    print("offre ajoutée en favoris")
else:
    print("offre non rajoutée")

liste_fav = o.voir_favoris(pers)
print("Liste des favoris :\n", liste_fav)
