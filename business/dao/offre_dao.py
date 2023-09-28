from business.dao.db_connection import DBConnection
from business import Singleton


class OffreDao(metaclass=Singleton):
    def supprimer_recherche(self, recherche) -> bool:
        """Suppression d'une offre sauvegardé par un utilisateur dans la base de données

        Parameters
        ----------
        user : Offre
            Offre sauvegardé par un utilisateur à supprimer de la base de données

        Returns
        -------
            True si l'offre a bien été supprimé
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer l'offre sauvegardé d'un utilisateur
                    cursor.execute(
                        "DELETE FROM projet2A.offre           "
                        " WHERE id_offre=%(id_offre)s      ",  # creer db compte_utilisateur ou changer le nom...
                        {"id_offre": recherche.id_offre},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0

    ## Besoin de finir cette fonction en fonction de ce qu'on affiche
    def sauvegarder_offre(
        self, nom_offre: str, offre: Offre, utilisateur: CompteUtilisateur
    ):
        """
        Sauvegarde l'offre dans la base de données

        Parameters
        ----------
        nom_recherche : str
            Nom de l'offre
        offre : Offre
            Offre à sauvegarder
        utilisateur : CompteUtilisateur
            Utilisateur qui sauvegarde l'offre

        Returns
        -------
            True si l'offre a bien été sauvegardée
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Sauvegarder l'offre d'un utilisateur
                    cursor.execute(
                        "INSERT INTO projet2A.offre(nom_recherche, parametre, resultat, utilisateur_id) "
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
