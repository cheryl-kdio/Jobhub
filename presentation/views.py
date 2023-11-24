# Importation des modules nécessaires
from abc import (
    ABC,
    abstractmethod,
)  # Importation de la classe ABC et de la fonction abstractmethod
from business.services.utilisateur_service import (
    Utilisateur,
)  # Importation de la classe Utilisateur depuis le module utilisateur_service
from business.dao.utilisateur_dao import UtilisateurDao
from business.business_object.recherche import Recherche
from business.services.recherche_service import RechercheService
from tabulate import tabulate
from business.dao.profil_chercheur_emploi_dao import ProfilChercheurEmploiDao
from business.business_object.profil_chercheur_emploi import ProfilChercheurEmploi
from business.dao.recherche_dao import RechercheDao


# Définition de la classe abstraite AbstractView
class AbstractView(ABC):
    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def make_choice(self):
        pass


# Définition de la classe HomeView qui hérite de AbstractView
class HomeView(AbstractView):
    def display_info(self):
        # Affichage des informations de la page d'accueil
        print("Welcome to the application!")
        print("1. Login")
        print("2. Create an account")
        print("3. Make a Research")
        print("4. Exit")

    def make_choice(self):
        choice = input(
            "Enter your choice: "
        )  # Demande à l'utilisateur de saisir son choix
        if choice == "1":
            return LoginView()  # Retourne une instance de LoginView si le choix est 1
        elif choice == "2":
            return (
                CreateAccountView()
            )  # Retourne une instance de CreateAccountView si le choix est 2
        elif choice == "3":
            return SearchView()
        elif choice == "4":
            return None  # Retourne None si le choix est 3 (sortie de l'application)
        else:
            print("Invalid choice. Please try again.")
            return (
                HomeView()
            )  # Retourne une instance de HomeView si le choix est invalide


# Définition de la classe LoginView qui hérite de AbstractView
class LoginView(AbstractView):
    def display_info(self):
        utilisateurdao = UtilisateurDao()
        mail = utilisateurdao.get_user_info("mail")
        passw = utilisateurdao.get_user_info("mdp")
        utilisateur = Utilisateur()  # Crée une instance de Utilisateur
        compte_utilisateur = utilisateur.se_connecter(
            mail, passw
        )  # Appelle la méthode se_connecter de l'instance d'Utilisateur
        if compte_utilisateur:
            # Affiche le contenu de la page de connexion réussie
            print("Successful connection ! Welcome,", compte_utilisateur.nom)
            self.user_menu_view = UserMenuView(compte_utilisateur)
        else:
            # Affiche le contenu de la page de connexion échouée
            print("email or password incorrect.")

    def make_choice(self):
        if self.user_menu_view:
            return self.user_menu_view
        else:
            return HomeView()


# Définition de la classe CreateAccountView qui hérite de AbstractView
class CreateAccountView(AbstractView):
    def display_info(self):
        utilisateurdao = UtilisateurDao()
        mail = utilisateurdao.get_user_info("mail")
        name_user = utilisateurdao.get_user_info("name_user")
        mdp = utilisateurdao.get_user_info("mdp")
        mdp_to_check = utilisateurdao.get_user_info("mdp_to_check")
        utilisateur = Utilisateur()  # Crée une instance de Utilisateur
        utilisateur.create_account(
            name_user, mail, mdp, mdp_to_check
        )  # Appelle la méthode create_account de l'instance d'Utilisateur
        # Affiche le contenu de la page de création de compte réussie
        print("Compte créé avec succès !")

    def make_choice(self):
        return (
            HomeView()
        )  # Retourne une instance de HomeView pour revenir à la page d'accueil


class UserMenuView(AbstractView):
    def __init__(self, user):
        self.user = user

    def display_info(self):
        print(f"Welcome, {self.user.mail}!")
        print("1. Make a research")
        print("2. See your user profile")
        print("3. Logout")

    def make_choice(self):
        choice = input("Enter your choice: ")
        if choice == "1":
            return SearchView(self.user)
        elif choice == "2":
            # Perform action 2
            return ProfileView(self.user)
        elif choice == "3":
            print("Logged out.")
            return HomeView()
        else:
            print("Invalid choice. Please try again.")
            return UserMenuView(self.user)


class SearchView(AbstractView):
    def __init__(self, user=None):
        self.user = user
        self.recherche = None

    def display_info(self):
        print("Search for job listings:")
        results_per_page = input("Enter results per page: ")
        what = input("Enter the job title or keywords: ")

        # Créez un objet Recherche avec les critères de recherche saisis par l'utilisateur
        query_params = {"results_per_page": results_per_page, "what": what}
        self.recherche = Recherche(query_params=query_params)

        rechercheservice = RechercheService()
        offres = rechercheservice.obtenir_resultats(self.recherche)

        data = {
            "n": [i + 1 for i, offre in enumerate(offres)],
            "Titre": [offre.titre for offre in offres],
            "Domaine": [offre.domaine for offre in offres],
            "Lieu": [offre.lieu for offre in offres],
            "Type de Contrat": [offre.type_contrat for offre in offres],
            "Entreprise ": [offre.entreprise for offre in offres],
        }
        print(tabulate(data, headers="keys", tablefmt="pretty"))

        input("Pressez entrée pour continuer :")
        print("1. Consulter l'offre en détail ")
        print("2. Sauvegarder la recherche dans votre profil")
        print("3. Faire une nouvelle recherche ")
        print("4. Retour à l'accueil")
        print("5. Deconnexion")

    def make_choice(self):
        choice = input("Your choice: ")
        if choice == "1":
            # TO DO
            pass
        elif choice == "2":
            if self.user:
                if self.recherche:
                    return SaveSearchView(self.user, self.recherche)
                else:
                    print("Please perform a search before saving it.")
            else:
                print("You need to be logged in to save a search.")
                return HomeView()
        elif choice == "3":
            return SearchView(self.user)
        elif choice == "4":
            return HomeView()
        elif choice == "5":
            print("Logged out.")
            return None
        else:
            print("Invalid choice. Please try again.")
            return UserMenuView(self.email)

        return HomeView()


class ProfileView(AbstractView):
    def __init__(self, user):
        self.user = user

    def display_info(self):
        pced = ProfilChercheurEmploiDao()
        print(pced.voir_profil_chercheur_emploi(self.user))
        input("Appuyez sur Entrée pour continuer...")
        print("1. Modify your profile :")
        print("2. Back")
        print("3. Log Out")
        print("4. Exit")

    def make_choice(self):
        choice = input("Enter your choice: ")
        if choice == "1":
            return ModifProfile(self.user)
        elif choice == "2":
            return UserMenuView(self.user)
        elif choice == "3":
            print("Logged out.")
            return HomeView()
        elif choice == "4":
            return None
        else:
            print("Invalid choice. Please try again.")
            return UserMenuView(self.email)


class ModifProfile(AbstractView):
    def __init__(self, user):
        self.user = user

    def display_info(self):
        while True:
            print("Quelles informations souhaitez-vous modifier ?")
            print("1. Lieu")
            print("2. Domaine")
            print("3. Salaire minimum")
            print("4. Type de contrat")
            print("5. Salaire maximum")
            print("6. Terminer les modifications et retourner au menu précédent")

            choices = input(
                "Entrez les numéros des options que vous souhaitez modifier (séparés par des espaces) : "
            )

            choices = choices.split()
            choices = [int(choice) for choice in choices]

            if not choices:
                print("Aucune option sélectionnée. Veuillez entrer au moins un numéro.")
                continue

            # Créez une instance de ProfilChercheurEmploi avec les nouvelles valeurs
            nouveau_profil = ProfilChercheurEmploi()

            for choice in choices:
                if choice == 1:
                    nouveau_profil.lieu = input("Nouveau lieu : ")
                elif choice == 2:
                    nouveau_profil.domaine = input("Nouveau domaine : ")
                elif choice == 3:
                    nouveau_profil.salaire_minimum = input("Nouveau salaire minimum : ")
                elif choice == 4:
                    nouveau_profil.type_contrat = input("Nouveau type de contrat : ")
                elif choice == 5:
                    nouveau_profil.salaire_maximum = input("Nouveau salaire maximum : ")
                else:
                    print("Option invalide : ", choice)

            # Appelez la méthode pour modifier le profil
            profil_dao = ProfilChercheurEmploiDao()
            profil_dao.modifier_profil_chercheur_emploi(nouveau_profil)

            terminate = input("Terminer les modifications ? (Oui/Non) ").strip().lower()
            if terminate == "oui":
                break

    def make_choice(self):
        return ProfileView(self.user)


class SaveSearchView(AbstractView):
    def __init__(self, user, recherche):
        self.user = user
        self.recherche = recherche

    def display_info(self):
        print("Save the search to your profile:")
        if RechercheDao().sauvegarder_recherche(self.recherche, self.user):
            print("Search saved successfully.")
        else:
            print("Search could not be saved. It may already exist in your profile.")
        input("Press Enter to continue...")

    def make_choice(self):
        return UserMenuView(self.user)


# Fonction principale du programme
def main():
    current_view = HomeView()  # Crée une instance de HomeView pour commencer
    while current_view is not None:
        current_view.display_info()  # Affiche les informations de la vue actuelle
        current_view = current_view.make_choice()


# Point d'entrée du programme
if __name__ == "__main__":
    main()
