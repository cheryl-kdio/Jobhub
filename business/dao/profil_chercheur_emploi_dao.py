from business.dao.db_connection import DBConnection
from business.singleton import Singleton
from business.client.profil_chercheur_emploi import ProfilChercheurEmploi
from business.client.recherche import Recherche


class ProfilChercheurEmploiDao:
    def modifier_profil_chercheur_emploi(self, profil_chercheur_emploi):
        with DBConnection().connection as connection:
            with connection.cursor() as cur:
                update = """
                UPDATE projet2A.profil_chercheur_emploi
                SET lieu=COALESCE(%s,lieu), domaine=COALESCE(%s,domaine), salaire_minimum=COALESCE(%s,salaire_minimum),
                    type_contrat = COALESCE(%s,type_contrat), salaire_maximum=COALESCE(%s,salaire_maximum)
                WHERE id_profil_chercheur_emploi = %(id_profil_chercheur_emploi)s AND utilisateur_id = %(utilisateur_id)s 
                """

                cur.execute(
                    update,
                    (
                        profil_chercheur_emploi.lieu,
                        profil_chercheur_emploi.domaine,
                        profil_chercheur_emploi.salaire_minimum,
                        profil_chercheur_emploi.type_contrat,
                        profil_chercheur_emploi.salaire_maximum,
                        profil_chercheur_emploi.id_profil_chercheur_emploi,
                        profil_chercheur_emploi.utilisateur_id,
                    ),
                )

    def deja_enregistré(self, profil_chercheur_emploi, utilisateur):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                query = (
                    "SELECT * FROM projet2A.profil_chercheur_emploi "
                    "WHERE lieu =%(lieu)s AND domaine=%(domaine)s AND salaire_minimum=%(salaire_minimum)s "
                    "AND salaire_maximum=%(salaire_maximum)s AND type_contrat=%(type_contrat)s  AND"
                    " utilisateur_id= %(utilisateur_id)s"
                )
                params = {
                    "lieu": profil_chercheur_emploi.lieu,
                    "domaine": profil_chercheur_emploi.domaine,
                    "salaire_minimum": profil_chercheur_emploi.salaire_minimum,
                    "salaire_maximum": profil_chercheur_emploi.salaire_maximum,
                    "type_contrat": profil_chercheur_emploi.type_contrat,
                    "utilisateur_id": utilisateur.id,
                }
                cursor.execute(query, params)
                res = cursor.fetchone()
        if res is not None:
            return res["id_profil_chercheur_emploi"]
        else:
            return None

    def match_criteres(self, profil_chercheur_emploi):
        query_params = {
            "where": profil_chercheur_emploi.lieu,
            "category": profil_chercheur_emploi.domaine,
            "distance": 10,
            "salary_min": profil_chercheur_emploi.salaire_minimum,
            "salary_max": profil_chercheur_emploi.salaire_maximum,
            "type_contrat": profil_chercheur_emploi.type_contrat,
        }
        recherche = Recherche(query_params)
        alertes = []
        if recherche.response.status_code == 200:
            jobs = recherche.response.json()["results"]
            for job in jobs:
                alerte = ProfilChercheurEmploi(
                    lieu=job.get("location", {}).get("display_name", ""),
                    domaine=job.get("category", {}).get("label", ""),
                    salaire_minimum=job.get("salary_min", ""),
                    salaire_maximum=job.get("salary_max", ""),
                    type_contrat=job.get("contract_type", ""),
                )
                if alerte:
                    alertes.append(alerte)

            return alertes

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
            True si l'offre a bien été sauvegardée
        """
        created = False

        deja_favoris = self.deja_enregistré(profil_chercheur_emploi, utilisateur)
        if deja_favoris is not None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # Sauvegarder l'offre d'un utilisateur
                cursor.execute(
                    "INSERT INTO projet2A.profil_chercheur_emploi (lieu, domaine, salaire_minimum, salaire_maximum,type_contrat,utilisateur_id) "
                    "VALUES (%(lieu)s, %(domaine)s, %(salaire_minimum)s, %(salaire_maximum)s,%(type_contrat)s, %(utilisateur_id)s)"
                    "RETURNING id_profil_chercheur_emploi",
                    {
                        "lieu": profil_chercheur_emploi.lieu,
                        "domaine": profil_chercheur_emploi.domaine,
                        "salaire_minimum": profil_chercheur_emploi.salaire_minimum,
                        "salaire_maximum": profil_chercheur_emploi.salaire_maximum,
                        "type_contrat": profil_chercheur_emploi.type_contrat,
                        "utilisateur_id": utilisateur.id,
                    },
                )
                res = cursor.fetchone()
        if res:
            profil_chercheur_emploi.id_profil_chercheur_emploi = res[
                "id_profil_chercheur_emploi"
            ]
            created = True
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
                lieu=row["lieu"],
                domaine=row["domaine"],
                salaire_minimum=row["salaire_minimum"],
                salaire_maximum=row["salaire_maximum"],
                type_contrat=row["type_contrat"],
            )
            for row in res
        ]
        return profils
