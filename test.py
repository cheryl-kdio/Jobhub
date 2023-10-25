from getpass import getpass
from argon2 import PasswordHasher

# Génération du mot de asse
ph = PasswordHasher()
password = getpass("Mot de passe : ")
hashed_password = ph.hash(password)

print(hashed_password)

# Vérification mot de passe
password_to_check = getpass("Vérification du mot de passe : ")
try:
    ph.verify(hashed_password, password_to_check)
    print("Le mot de passe est valide.")
except:
    print("Le mot de passe est invalide.")