from InquirerPy import prompt
from presentation.abstract_view import AbstractView
from presentation.session import Session
from business.dao.offre_dao import OffreDao


class OffreView(AbstractView):
    def __init__(self, user, langue):
        self.user = user
        self.langue = langue

    def display_info(self):
        pass

    def make_choice(self):
        o = OffreDao()
        choix_offres = [
            {
                "name": f"{str(i+1)} . Title: {offre.titre}, Location: {offre.lieu}"
                if self.langue == "anglais"
                else f"{str(i+1)}. Titre: {offre.titre}, Lieu: {offre.lieu}",
                "value": offre,
            }
            for i, offre in enumerate(o.voir_favoris(self.user))
        ] + [{"name": "Retour", "value": None}]

        if len(choix_offres) == 1:
            print(
                "Vous n'avez pas d'offres sauvegardées"
                if self.langue == "français"
                else "You don't have any saved offers."
            )

            self.__questions = [
                {
                    "type": "confirm",
                    "name": "oui",
                    "message": "Souhaiter vous lancer une recherche ?"
                    if self.langue == "français"
                    else "Do you want to start a reasearch ? ",
                    "default": True,
                }
            ]

            answers = prompt(self.__questions)

            if answers["oui"]:
                from presentation.recherche_view import RechercheView

                return RechercheView(langue=self.langue, user=self.user)
            else:
                from presentation.user_view import UserView

                return UserView(user=self.user, langue=self.langue)

        else:
            message_fr = "Choisissez une offre à détailler : \n - - - - - - - - - - - - - - - - - - - -\n"
            message_en = "Choose a job to view in detail."
            message = message_fr if self.langue == "français" else message_en

            self.__questions = {
                "type": "list",
                "message": message,
                "choices": choix_offres,
            }

            answers = prompt(self.__questions)
            if answers[0] in ("Retour", "Return"):
                from presentation.user_view import UserView

                return UserView(self.user, self.langue)
            else:
                print(answers[0])
                self.__questions = [
                    {
                        "type": "confirm",
                        "name": "oui",
                        "message": "Souhaitez-vous candidater à cette offre ?"
                        if self.langue == "français"
                        else "Apply to this job?",
                        "default": True,
                    }
                ]
                answers2 = prompt(self.__questions)
                if answers2["oui"]:
                    if o.deja_candidat(answers[0], self.user):
                        print("Vous avez dejà envoyé votre candidature")
                        return OffreView(user=self.user, langue=self.langue)

                    else:
                        o.candidater(answers[0], self.user)
                        message_fr = "Votre candidature a bien été envoyée!"
                        message_en = "Your submission was sent !"
                        message = (
                            message_fr if self.langue == "français" else message_en
                        )
                        print(message)
                        return OffreView(user=self.user, langue=self.langue)

                else:
                    self.__questions = [
                        {
                            "type": "confirm",
                            "name": "oui",
                            "message": "Souhaitez-vous supprimer l'offre de vos favoris ?"
                            if self.langue == "français"
                            else "Delete the offer from your favorites?",
                            "default": True,
                        }
                    ]
                    answers2 = prompt(self.__questions)
                    if answers2["oui"]:
                        o.supprimer_offre(answers[0])
                        message_deleted_fr = "L'offre a bien été supprimée"
                        message_deleted_en = "The offer has been deleted"
                        message_deleted = (
                            message_deleted_fr
                            if self.langue == "français"
                            else message_deleted_en
                        )
                        print(message_deleted)
                        return OffreView(user=self.user, langue=self.langue)
                    else:
                        from presentation.user_view import UserView

                        return UserView(user=self.user, langue=self.langue)
