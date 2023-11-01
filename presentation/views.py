# Importation des modules nécessaires
from abc import (
    ABC,
    abstractmethod,
)  # Importation de la classe ABC et de la fonction abstractmethod
from business.services.utilisateur_service import (
    Utilisateur,
)  # Importation de la classe Utilisateur depuis le module utilisateur_service
from business.dao.utilisateur_dao import UtilisateurDao


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
            return ResearchView()
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
        compte_utilisateur = (
            utilisateur.se_connecter(mail, passw)
        )  # Appelle la méthode se_connecter de l'instance d'Utilisateur
        if compte_utilisateur:
            # Affiche le contenu de la page de connexion réussie
            print("Successful connection ! Welcome,", compte_utilisateur.nom)
            self.user_menu_view = UserMenuView(compte_utilisateur.mail)
        else:
            # Affiche le contenu de la page de connexion échouée
            print("email or password incorrect.")

    def make_choice(self):
        if self.user_menu_view:
            return self.user_menu_view  # Renvoyez l'instance de UserMenuView si elle a été créée
        else:
            return HomeView


# Définition de la classe CreateAccountView qui hérite de AbstractView
class CreateAccountView(AbstractView):
    def display_info(self):
        utilisateurdao = UtilisateurDao()
        mail = utilisateurdao.get_user_info("mail")
        name_user = utilisateurdao.get_user_info("name_user")
        mdp = utilisateurdao.get_user_info("mdp")
        mdp_to_check = utilisateurdao.get_user_info("mdp_to_check")
        utilisateur = Utilisateur()  # Crée une instance de Utilisateur
        utilisateur.create_account(name_user, mail, mdp, mdp_to_check)  # Appelle la méthode create_account de l'instance d'Utilisateur
        # Affiche le contenu de la page de création de compte réussie
        print("Compte créé avec succès !")

    def make_choice(self):
        return (
            HomeView()
        )  # Retourne une instance de HomeView pour revenir à la page d'accueil


class UserMenuView(AbstractView):
    def __init__(self, email):
        self.email = email

    def display_info(self):
        print(f"Welcome, {self.email}!")
        print("1. Make a research")
        print("2. See your user profile")
        print("3. Logout")

    def make_choice(self):
        choice = input("Enter your choice: ")
        if choice == "1":
            # Perform action 1
            return UserMenuView(self.email)
        elif choice == "2":
            # Perform action 2
            return UserMenuView(self.email)
        elif choice == "3":
            print("Logged out.")
            return HomeView()
        else:
            print("Invalid choice. Please try again.")
            return UserMenuView(self.email)


# Fonction principale du programme
def main():
    current_view = HomeView()  # Crée une instance de HomeView pour commencer
    while current_view is not None:
        current_view.display_info()  # Affiche les informations de la vue actuelle
        current_view = (
            current_view.make_choice()
        )  # Détermine la prochaine vue en fonction du choix de l'utilisateur






# Point d'entrée du programme
if __name__ == "__main__":
    main()
