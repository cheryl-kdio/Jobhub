from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.utilisateur_dao import UtilisateurDao
import json


class RechercheDao(metaclass=Singleton):
    def supprimer_recherche(
        self, recherche: Recherche, utilisateur: CompteUtilisateur
    ) -> bool:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Supprimer la recherche d'un utilisateur
                cursor.execute(
                    "DELETE FROM projet2A.recherche "
                    "WHERE query_params=%(query_params)s and utilisateur_id =%(utilisateur_id)s ",
                    {
                        "query_params": json.dumps(recherche.query_params),
                        "utilisateur_id": utilisateur.id,
                    },
                )
                res = cursor.rowcount
        return res > 0

    def sauvegarder_recherche(
        self, recherche: Recherche, utilisateur: CompteUtilisateur
    ):
        """
        Sauvegarde la recherche dans la base de données

        Parameters
        ----------
        recherche : Recherche
            Recherche à sauvegarder
        utilisateur : CompteUtilisateur
            Utilisateur qui sauvegarde la recherche

        Returns
        -------
            True si la recherche a bien été sauvegardée
        """
        created = False

        deja_favoris = self.deja_favoris(recherche, utilisateur.id)
        if deja_favoris is True:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Sauvegarder la recherche d'un utilisateur
                cursor.execute(
                    "INSERT INTO projet2A.recherche(query_params, utilisateur_id) "
                    "VALUES (%(parametre)s, %(utilisateur_id)s) "
                    "RETURNING id_recherche",
                    {
                        "parametre": json.dumps(recherche.query_params),
                        "utilisateur_id": utilisateur.id,
                    },
                )
                res = cursor.fetchone()

        if res:
            recherche.id_recherche = res["id_recherche"]
            created = True

        return created

    def deja_favoris(self, recherche, id_utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                query = (
                    "SELECT id_recherche FROM projet2A.recherche r "
                    "WHERE r.query_params=%(query_params)s AND r.utilisateur_id= %(utilisateur_id)s "
                )
                params = {
                    "query_params": json.dumps(recherche.query_params),
                    "utilisateur_id": id_utilisateur,
                }
                cursor.execute(query, params)
                res = cursor.fetchone()
        return res is not None

    def voir_favoris(self, utilisateur):
        id_utilisateur = UtilisateurDao().get_value_from_mail(
            utilisateur.mail, "id_compte_utilisateur"
        )

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                "Sauvegarder recherche d'un utilisateur"
                cursor.execute(
                    "SELECT * "
                    "FROM projet2A.recherche "
                    "WHERE utilisateur_id=%(id_utilisateur)s",
                    {"id_utilisateur": id_utilisateur},
                )
                res = cursor.fetchall()
        recherches = []

        if res:
            for row in res:
                recherche = Recherche(
                    query_params=json.loads(row["query_params"])
                ).query_params
                recherches.append(recherche)
        print(
            recherches
        )  ## remettre en return + voir comment on peut faire pour aller plus loin
