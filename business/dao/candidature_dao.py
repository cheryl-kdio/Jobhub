from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.offre import Offre
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.recherche_dao import RechercheDao
from business.services.recherche_service import RechercheService
from business.dao.utilisateur_dao import UtilisateurDao


class Candidature_Dao(metaclass=Singleton):
    def supprimer_candidature(self, offre) -> bool:
        """
        Suppression d'une offre favoris d'un utilisateur dans la base de données

        Parameters
        ----------
        offre : Offre
            Offre sauvegardée par un utilisateur à supprimer de la base de données

        Returns
        -------
            True si l'offre a bien été supprimé
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Supprimer l'offre sauvegardé d'un utilisateur
                cursor.execute(
                    "DELETE FROM projet2A.candidatures        "
                    " WHERE id_offre = %(id_offre)s      ",
                    {"id_offre": offre.id_offre},
                )
                res = cursor.rowcount

        return res > 0

    def deja_favoris(self, offre, utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                query = (
                    "SELECT * FROM projet2A.offre o "
                    "WHERE id_offre =%(id_offre)s AND "
                    " o.utilisateur_id= %(utilisateur_id)s"
                )
                params = {
                    "id_offre": offre.id_offre,
                    "utilisateur_id": utilisateur.id,
                }
                cursor.execute(query, params)
                res = cursor.fetchone()
        if res is not None:
            return res["id_offre"]
        else:
            return None

    def ajouter_candidature(self, offre, utilisateur):
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

        deja_favoris = self.deja_favoris(offre, utilisateur)
        if deja_favoris is not None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Sauvegarder l'offre d'un utilisateur
                cursor.execute(
                    "INSERT INTO projet2A.offre(id_offre,titre, domaine, lieu, type_contrat, entreprise, utilisateur_id) "
                    " VALUES (%(id_offre)s,%(titre)s, %(domaine)s, %(lieu)s, %(type_contrat)s, %(entreprise)s, %(utilisateur_id)s)  "
                    "RETURNING id_offre",
                    {
                        "id_offre": offre.id_offre,
                        "titre": offre.titre,
                        "domaine": offre.domaine,
                        "lieu": offre.lieu,
                        "type_contrat": offre.type_contrat,
                        "entreprise": offre.entreprise,
                        "utilisateur_id": utilisateur.id,
                    },
                )
                res = cursor.fetchone()
        if res:
            created = True
        return created

    def voir_candidature(self, utilisateur):
        """
         Voir les offres favoris de la base de données

         Parameters
         ----------
         utilisateur : CompteUtilisateur
               Utilisateur qui sauvegarde l'offre
        Returns
         -------
             True si l'offre a bien été sauvegardée
        """

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Sauvegarder l'offre d'un utilisateur
                cursor.execute(
                    "SELECT * "
                    "FROM projet2A.offre "
                    "WHERE utilisateur_id=%(id_utilisateur)s",
                    {"id_utilisateur": utilisateur.id},
                )
                res = cursor.fetchall()

        offres = [
            Offre(
                id_offre=row["id_offre"],
                titre=row["titre"],
                domaine=row["domaine"],
                lieu=row["lieu"],
                type_contrat=row["type_contrat"],
                entreprise=row["entreprise"],
            )
            for row in res
        ]
        return offres



