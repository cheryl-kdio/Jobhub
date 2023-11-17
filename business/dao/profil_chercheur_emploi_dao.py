from business.dao.db_connection import DBConnection
from utils.singleton import Singleton
from business.client.profil_chercheur_emploi import ProfilChercheurEmploi
from business.client.recherche import Recherche
from business.services.recherche_service import RechercheService



class ProfilChercheurEmploiDao:
    def maj(self,profil_chercheur_emploi):
        with DBConnection().connection as connection:
                with connection.cursor() as cur:
                    update_query = """UPDATE projet2A.profil_chercheur_emploi
                    SET mots_cles=(%s,mots_cles)
                        lieu = COALESCE(%s, lieu), 
                        distance = COALESCE(%s, distance), 
                        type_contrat = COALESCE(%s, type_contrat), 
                    WHERE id_compte_utilisateur = %s """

                    cur.execute(
                        update_query,
                        (mots_cles, lieu, profil_chercheur_emploi.distance, profil_chercheur_emploi.type_contrat, profil_chercheur_emploi.id_profil_chercheur_emploi),
                    )
                    
                    if cur.rowcount > 0:
                        return True
                    else:
                        return False


    def deja_cree(self, profil_chercheur_emploi, utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                query = (
                    "SELECT * FROM projet2A.profil_chercheur_emploi "
                    "WHERE nom =%(nom)s AND utilisateur_id= %(utilisateur_id)s"
                )
                params = {
                    "nom": profil_chercheur_emploi.nom,
                    "utilisateur_id": utilisateur.id,
                }
                cursor.execute(query, params)
                res = cursor.fetchone()
        if res is not None:
            return res["id_profil_chercheur_emploi"]
        else:
            return None

    def match_criteres(self, profil_chercheur_emploi):
        recherche_init = Recherche(profil_chercheur_emploi.query_params)
        r = RechercheService()
        offres = r.obtenir_resultats(recherche_init)
        return offres

    def ajouter_profil_chercheur_emploi(self, profil_chercheur_emploi, utilisateur):
        """
        Sauvegarde l'offre dans la base de données

        Parameters
        ----------
        profil_chercheur_emploi : profil_chercheur_emploi
            Offre à sauvegarder
        utilisateur : CompteUtilisateur
            Utilisateur qui sauvegarde l'offre

        Returns
        -------
            ID du profil sauvegardé, ou None si le profil existe déjà
        """

        # Check if the profile already exists
        created = False
        deja_cree_id = self.deja_cree(profil_chercheur_emploi, utilisateur)
        if deja_cree_id is not None:
            return created  # Profile already exists

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Sauvegarder le nouveau profil d'un utilisateur
                cursor.execute(
                    "INSERT INTO projet2A.profil_chercheur_emploi (nom, lieu, mots_cles, type_contrat, utilisateur_id) "
                    "VALUES (%(nom)s, %(lieu)s, %(mots_cles)s, %(type_contrat)s, %(utilisateur_id)s) "
                    "RETURNING id_profil_chercheur_emploi",
                    {
                        "nom": profil_chercheur_emploi.nom,
                        "mots_cles" :profil_chercheur_emploi.mots_cles,
                        "lieu": profil_chercheur_emploi.lieu,
                        "type_contrat": profil_chercheur_emploi.type_contrat,
                        "utilisateur_id": utilisateur.id,
                    },
                )
                res = cursor.fetchone()

        if res:
            profil_chercheur_emploi.id_profil_chercheur_emploi = res["id_profil_chercheur_emploi"]
            created=True
        return created

    def supprimer_profil_chercheur_emploi(self, profil_chercheur_emploi):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Supprimer l'offre sauvegardé d'un utilisateur
                cursor.execute(
                    "DELETE FROM projet2A.profil_chercheur_emploi        "
                    " WHERE id_profil_chercheur_emploi = %(id_profil_chercheur_emploi)s      ",
                    {
                        "id_profil_chercheur_emploi": profil_chercheur_emploi.id_profil_chercheur_emploi
                    },
                )
                res = cursor.rowcount

        return res > 0

    def voir_profil_chercheur_emploi(self, utilisateur):
        """
         Voir les profils chercheur emploi de la base de données

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
                    "FROM projet2A.profil_chercheur_emploi "
                    "WHERE utilisateur_id=%(id_utilisateur)s",
                    {"id_utilisateur": utilisateur.id},
                )
                res = cursor.fetchall()

        profils = [
            ProfilChercheurEmploi(
                id_profil_chercheur_emploi=row["id_profil_chercheur_emploi"],
                nom=row["nom"],
                mots_cles=row["mots_cles"],
                lieu=row["lieu"],
                distance=row["distance"],
                type_contrat=row["type_contrat"],
            )
            for row in res
        ]
        return profils
