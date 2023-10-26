from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.offre import Offre
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.recherche_dao import RechercheDao
from business.services.recherche_service import RechercheService
from business.dao.utilisateur_dao import UtilisateurDao
from business.dao.utilisateur_dao import UtilisateurDao


class OffreDao(metaclass=Singleton):
    def supprimer_offre(self, offre) -> bool:
        """
        Suppression d'une offre sauvegardé par un utilisateur dans la base de données

        Parameters
        ----------
        offre : Offre
            Offre sauvegardé par un utilisateur à supprimer de la base de données

        Returns
        -------
            True si l'offre a bien été supprimé
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Supprimer l'offre sauvegardé d'un utilisateur
                cursor.execute(
                    "DELETE FROM projet2A.offre        "
                    " WHERE id_offre = %(id_offre)s      ",
                    {"id_offre": offre.id_offre},
                )
                res = cursor.fetchone()

        return res is not None

    def deja_favoris(self, offre, id_utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                query = (
                    "SELECT id_offre FROM projet2A.offre o "
                    "WHERE o.titre=%(titre)s AND o.domaine = %(domaine)s AND o.lieu =%(lieu)s AND "
                    "o.type_contrat = %(type_contrat)s AND o.lien_offre =%(lien_offre)s AND "
                    "o.salaire_minimum = %(salaire_minimum)s AND o.etre_en_favoris= %(etre_en_favoris)s AND o.utilisateur_id= %(utilisateur_id)s"
                )
                params = {
                    "titre": offre.titre,
                    "domaine": offre.domaine,
                    "lieu": offre.lieu,
                    "type_contrat": offre.type_contrat,
                    "lien_offre": offre.lien_offre,
                    "salaire_minimum": offre.salaire_minimum,
                    "etre_en_favoris": offre._etre_en_favoris,
                    "utilisateur_id": id_utilisateur,
                }
                cursor.execute(query, params)
                res = cursor.fetchone()
        return res is not None

    def ajouter_offre(self, offre, id_utilisateur):
        """
        Sauvegarde l'offre dans la base de données

        Parameters
        ----------

        offre : Offre
            Offre à sauvegarder
        utilisateur : CompteUtilisateur
            Utilisateur qui sauvegarde l'offre

        Returns
        -------
            True si l'offre a bien été sauvegardée
        """
        created = False

        deja_favoris = self.deja_favoris(offre, id_utilisateur)
        if deja_favoris is None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Sauvegarder l'offre d'un utilisateur
                cursor.execute(
                    "INSERT INTO projet2A.offre(titre, domaine, lieu, type_contrat, lien_offre, salaire_minimum, etre_en_favoris, utilisateur_id) "
                    " VALUES (%(titre)s, %(domaine)s, %(lieu)s, %(type_contrat)s, %(lien_offre)s, %(salaire_minimum)s, %(etre_en_favoris)s, %(utilisateur_id)s)  "
                    "RETURNING id_offre",
                    {
                        "titre": offre.titre,
                        "domaine": offre.domaine,
                        "lieu": offre.lieu,
                        "type_contrat": offre.type_contrat,
                        "lien_offre": offre.lien_offre,
                        "salaire_minimum": offre.salaire_minimum,
                        "etre_en_favoris": offre._etre_en_favoris,
                        "utilisateur_id": id_utilisateur,
                    },
                )
                res = cursor.fetchone()
        if res:
            offre.id = res["id_offre"]
            created = True


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
print(b)
