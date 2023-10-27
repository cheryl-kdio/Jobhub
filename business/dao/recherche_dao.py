from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur


class RechercheDao(metaclass=Singleton):
    def supprimer_recherche(
        self, recherche: Recherche, utilisateur: CompteUtilisateur
    ) -> bool:
        """Suppression d'une recherche sauvegardé dans la base de données

        Parameters
        ----------
        user : id_recherche
            recherche à supprimer des sauvegardes

        Returns
        -------
            True si la recherche a bien été supprimé
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer la recherche d'un utilisateur
                    cursor.execute(
                        "DELETE FROM projet2A.recherche "
                        " WHERE id_recherche=%(id_recherche)s and id_utilisateur=%(id_utilisateur)s ", 
                        {
                            "id_recherche": recherche.id_recherche,
                            "id_utilisateur": utilisateur.id,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0

    def sauvegarder_recherche(
        self, nom_recherche: str, recherche: Recherche, utilisateur: CompteUtilisateur
    ):
        """
        Sauvegarde la recherche dans la base de données

        Parameters
        ----------
        nom_recherche : str
            Nom de la recherche
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
        if deja_favoris is None:
            return created
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Sauvegarder la recherche d'un utilisateur
                    cursor.execute(
                        "INSERT INTO projet2A.recherche(nom_recherche, parametre, resultat, utilisateur_id) "
                        " VALUES (%(nom_recherche)s, %(parametre)s),  %(resultat)s, %(utilisateur_id)s)",
                        "RETURNING id_recherche",
                        {
                            "nom_recherche": nom_recherche,
                            "parametre": recherche.params,
                            "resultat": recherche.response,
                            "utilisateur_id": utilisateur.id,
                        },
                    )
                    res = cursor.fetchone()

            if res:
                recherche.id = res["id_recherche"]
                created = True

            return created
        except Exception as e:
            raise e

    def deja_favoris(self, recherche, id_utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                query = (
                    "SELECT id_recherche FROM projet2A.recherche r "
                    "WHERE r.query_params=%(query_params)s AND r.utilisateur_id= %(utilisateur_id)s"
                    "RETURNING id_recherche"
                )
                params = {
                    "query_params" : recherche.query_params,
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
                    # Sauvegarder recherche d'un utilisateur
                    cursor.execute(
                        "SELECT * "
                        "FROM projet2A.recherche "
                        "WHERE utilisateur_id=%(id_utilisateur)s"
                        "RETURNING id_recherche",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
            recherches = []

            if res:
                for row in res:
                    recherche = Recherche(
                        query_params=row["query_params"],
                    )
                    recherches.append(recherche)
            return recherches




