from business.dao.db_connection import DBConnection
from business import Singleton
from business.client.compte_utilisateur import CompteUtilisateur


class CompteUtilisateurDao(metaclass=Singleton):
    def supprimer(self, user) -> bool:
        """Suppression d'un utilisateur dans la base de données

        Parameters
        ----------
        user : CompteUtilisateur
            utilisateur à supprimer de la base de données

        Returns
        -------
            True si l'utilisateur a bien été supprimé
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un utilisateur
                    cursor.execute(
                        "DELETE FROM projet2A.compte_utilisateur           "
                        " WHERE id_compte_utilisateur=%(id_compte_utilisateur)s      ",  # creer db compte_utilisateur ou changer le nom...
                        {"id_compte_utilisateur": user.id_compte_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0

    def update(self, attribut, attribut_contenu, user):
        """Mise à jour des informations d'un utilisateur dans la base de données

        Parameters
        ----------
        attribut : str
            attribut de l'utilisateur à mettre à jour dans la base de données

        attribut_contenu : str
            contenu de l'attribut de l'utilisateur à mettre à jour dans la base de données

        Returns
        -------
            True si l'utilisateur a bien été mis à jour
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un utilisateur
                    cursor.execute(
                        "UPDATE projet2A.compte_utilisateur           "
                        " SET %(attribut)s=%(attribut_contenu)s      "
                        " WHERE id_compte_utilisateur=%(id_compte_utilisateur)s     ",  # creer db compte_utilisateur ou changer le nom...
                        {
                            "attribut": attribut,
                            "attribut_contenu": attribut_contenu,
                            "id_compte_utilisateur": user.id_compte_utilisateur,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            print(e)
            raise

        return res > 0
