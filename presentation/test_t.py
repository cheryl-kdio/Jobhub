from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.compte_utilisateur import CompteUtilisateur
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService
from business.dao.recherche_dao import RechercheDao
from presentation.user_service_t import Utilisateur
from presentation.user_dao_t import UtilisateurDao
from business.dao.offre_dao import OffreDao

#Pierre = Utilisateur().create_account() 
personne= Utilisateur().se_connecter(mail="cherylk@gmail.com",passw="Patate12")

personne._connexion