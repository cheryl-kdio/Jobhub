from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.utilisateur_dao import UtilisateurDao
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService
from business.dao.recherche_dao import RechercheDao
from business.services.utilisateur_service import Utilisateur
from business.dao.offre_dao import OffreDao
from business.dao.recherche_dao import RechercheDao
from business.client.offre import Offre

# Pierre = Utilisateur().create_account("cheryl", "ck@gmail.com", "Patate12", "Patate12")
pierre = Utilisateur().se_connecter("ck@gmail.com", "Patate12")

query_params = {"results_per_page": 20, "what": "python dev"}

offre = Offre(
    titre="test",
    domaine="dev",
    lieu="spdn",
    type_contrat="CDI",
    entreprise="nike",
    id_offre=1,
)

# a = Recherche(query_params=query_params)
# RechercheDao().sauvegarder_recherche(a, pierre)
# b = RechercheService().obtenir_resultats(a)
# print(b[0])
# print(str(query_params))
OffreDao().ajouter_offre(offre, pierre)
# OffreDao().supprimer_offre(offre)
OffreDao().voir_favoris(pierre)
##Pierre sauvegarde les paramètres de sa recherche

# RechercheDao().sauvegarder_recherche(a, pierre)


### Pierre supprime sa recherche de ses favoris

# RechercheDao().supprimer_recherche(a, pierre)

# Voir favoris

# RechercheDao().voir_favoris(pierre)
