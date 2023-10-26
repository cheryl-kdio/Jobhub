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
                        " WHERE id_recherche=%(id_recherche)s and id_utilisateur=%(id_utilisateur)s ",  ## Demander des infos
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
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Sauvegarder la recherche d'un utilisateur
                    cursor.execute(
                        "INSERT INTO projet2A.recherche(nom_recherche, parametre, resultat, utilisateur_id) "
                        " VALUES (%(nom_recherche)s, %(parametre)s),  %(resultat)s, %(utilisateur_id)s)                  ",
                        {
                            "nom_recherche": nom_recherche,
                            "parametre": recherche.params,
                            "resultat": recherche.response,
                            "utilisateur_id": utilisateur.id,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise
