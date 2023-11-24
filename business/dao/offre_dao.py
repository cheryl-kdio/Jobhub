from business.dao.db_connection import DBConnection
from utils.singleton import Singleton
from business.business_object.offre import Offre
from business.business_object.recherche import Recherche
from business.business_object.compte_utilisateur import CompteUtilisateur
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

        deja_favoris = self.deja_favoris(offre, utilisateur)
        if deja_favoris is not None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Sauvegarder l'offre d'un utilisateur
                cursor.execute(
                    "INSERT INTO projet2A.offre(id_offre,titre, domaine, lieu, type_contrat, lien_offre, salaire_minimum, entreprise,description, utilisateur_id) "
                    " VALUES (%(id_offre)s,%(titre)s, %(domaine)s, %(lieu)s, %(type_contrat)s, %(lien_offre)s, %(salaire_minimum)s, %(entreprise)s ,%(description)s, %(utilisateur_id)s)  "
                    "RETURNING id_offre",
                    {
                        "id_offre": offre.id_offre,
                        "titre": offre.titre,
                        "domaine": offre.domaine,
                        "lieu": offre.lieu,
                        "type_contrat": offre.type_contrat,
                        "lien_offre": offre.lien_offre,
                        "salaire_minimum": offre.salaire_minimum
                        if offre.salaire_minimum
                        else None,
                        "description": offre.description,
                        "entreprise": offre.entreprise,
                        "utilisateur_id": utilisateur.id,
                    },
                )
                res = cursor.fetchone()
        if res:
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
                lien_offre=row["lien_offre"],
                salaire_minimum=row["salaire_minimum"],
                entreprise=row["entreprise"],
                description=row["description"],
            )
            for row in res
        ]
        return offres

    def candidater(self, offre, utilisateur):
        """
        Sauvegarde l'offre dans la base de données

        Parameters
        ----------

        offre : Offre
            Offre à candidater
        utilisateur : CompteUtilisateur
            Utilisateur qui candidate à l'offre

        Returns
        -------
            True si la candidature a bien été effectuée
        """
        created = False

        deja_favoris = self.deja_favoris(offre, utilisateur)
        if deja_favoris is not None:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Sauvegarder l'offre d'un utilisateur
                    cursor.execute(
                        "UPDATE projet2A.offre SET candidature_envoyee = TRUE WHERE id_offre = %(id_offre)s;",
                        {
                            "id_offre": offre.id_offre,
                        },
                    )
                    res = cursor.rowcount
            if res > 0:
                created = True
            else:
                return None
        else :
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Sauvegarder l'offre d'un utilisateur
                    cursor.execute(
                        "INSERT INTO projet2A.offre(id_offre,titre, domaine, lieu, type_contrat, lien_offre, salaire_minimum, entreprise,description, utilisateur_id,candidature_envoyee) "
                        " VALUES (%(id_offre)s,%(titre)s, %(domaine)s, %(lieu)s, %(type_contrat)s, %(lien_offre)s, %(salaire_minimum)s, %(entreprise)s ,%(description)s, %(utilisateur_id)s,TRUE)  "
                        "RETURNING id_offre",
                        {
                            "id_offre": offre.id_offre,
                            "titre": offre.titre,
                            "domaine": offre.domaine,
                            "lieu": offre.lieu,
                            "type_contrat": offre.type_contrat,
                            "lien_offre": offre.lien_offre,
                            "salaire_minimum": offre.salaire_minimum
                            if offre.salaire_minimum
                            else None,
                            "description": offre.description,
                            "entreprise": offre.entreprise,
                            "utilisateur_id": utilisateur.id,
                        },
                    )
                    res = cursor.fetchone()
            if res:
                created = True
            return created

    def voir_candidatures(self, utilisateur):
        """
         Voir les candidatures d'un utilisateur

         Parameters
         ----------
         utilisateur : CompteUtilisateur
               Utilisateur qui a candidaté l'offre
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
                    "WHERE utilisateur_id=%(id_utilisateur)s"
                    "AND candidature_envoyee=TRUE",
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
                lien_offre=row["lien_offre"],
                salaire_minimum=row["salaire_minimum"],
                entreprise=row["entreprise"],
                description=row["description"],
            )
            for row in res
        ]
        return offres

    def deja_candidat(self, offre, utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                query = (
                    "SELECT candidature_envoyee FROM projet2A.offre o "
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
            return res["candidature_envoyee"]
        else:
            return None
