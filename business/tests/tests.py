from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.utilisateur_dao import UtilisateurDao
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService
from business.dao.recherche_dao import RechercheDao
from business.services.utilisateur_service import Utilisateur
from business.dao.offre_dao import OffreDao

# Pierre = Utilisateur().create_account() 
pierre= Utilisateur().se_connecter()

query_params = {
    "results_per_page": 20,
    "what": "python dev",
    # "where": "london",
    # "sort_direction": "up",
    # "sort_by": "relevance",
    # "category": "IT Jobs",
    # "distance": 10,
    # "salary_min": 50000,
    # "salary_max": 100000,
    # "permanent": "1",
    # "part_time": "0",
    # "full_time": "1",
    # "contract": "0",
}

a = Recherche(query_params=query_params)
b = RechercheService().obtenir_resultats(a)
print(b[0])
OffreDao().ajouter_offre(b[0],pierre.id)
