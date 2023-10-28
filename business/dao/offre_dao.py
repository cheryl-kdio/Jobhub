from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.offre import Offre
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.recherche_dao import RechercheDao
from business.services.recherche_service import RechercheService
from business.dao.utilisateur_dao import UtilisateurDao


class OffreDao(metaclass=Singleton):
    def supprimer_offre(self, offre) -> bool:
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
                    "DELETE FROM projet2A.offre        "
                    " WHERE id_offre = %(id_offre)s      ",
                    {"id_offre": offre.id_offre},
                )
                res = cursor.rowcount

        return res > 0

    def deja_favoris(self, offre, utilisateur):
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
                    "utilisateur_id": utilisateur.id,
                }
                cursor.execute(query, params)
                res = cursor.fetchone()
        return res["id_offre"] if res is not None else None

    def ajouter_offre(self, offre, utilisateur):
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
                        "utilisateur_id": utilisateur.id,
                    },
                )
                res = cursor.fetchone()
        if res:
            offre.id_offre = res["id_offre"]
            created = True
        return created

    def voir_favoris(self, utilisateur):
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
        id_utilisateur = UtilisateurDao().get_value_from_mail(
            utilisateur.mail, "id_compte_utilisateur"
        )

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Sauvegarder l'offre d'un utilisateur
                cursor.execute(
                    "SELECT * "
                    "FROM projet2A.offre "
                    "WHERE utilisateur_id=%(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur},
                )
                res = cursor.fetchall()

        offres = [Offre(id_offre=row["id_offre"], titre=row["titre"], domaine=row["domaine"],
                lieu=row["lieu"], type_contrat=row["type_contrat"], lien_offre=row["lien_offre"],
                salaire_minimum=row["salaire_minimum"]) for row in res]
        return offres



