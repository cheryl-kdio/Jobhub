from Business_layer.CompteUtilisateur import CompteUtilisateur

# Création d'une instance de CompteUtilisateur

utilisateur1 = CompteUtilisateur(
    id=1,
    mdp="motdepasse123",
    nom="John Doe",
    date_naissance="1990-05-15",
    mail="john.doe@example.com",
    tel=1234567890,
    ville="Villeville",
    code_postal=12345,
)

# Accès aux attributs de l'utilisateur
print(f"ID de l'utilisateur : {utilisateur1.id}")
print(f"Nom de l'utilisateur : {utilisateur1.nom}")
print(f"Âge de l'utilisateur : {utilisateur1.age} ans")
print(f"Adresse e-mail de l'utilisateur : {utilisateur1.mail}")
print(f"Numéro de téléphone de l'utilisateur : {utilisateur1.tel}")
print(f"Ville de résidence de l'utilisateur : {utilisateur1.ville}")
print(f"Code postal de la ville de résidence : {utilisateur1.code_postal}")

# Appel de la méthode pour se déconnecter
utilisateur1.se_deconnecter()

# Vérification de l'état de connexion
if utilisateur1._connexion:
    print("L'utilisateur est connecté.")
else:
    print("L'utilisateur est déconnecté.")
