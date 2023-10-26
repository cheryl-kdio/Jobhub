from flask import Flask, render_template, request,  redirect, url_for,session
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.recherche_dao import RechercheDao
from business.services.recherche_service import RechercheService
from business.dao.utilisateur_dao import UtilisateurDao
from presentation.user_service_t import Utilisateur



app = Flask(__name__)
app.secret_key = 'cheryl' 
recherche_service = RechercheService()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query_params = {
            "results_per_page": request.form.get("results_per_page", 20),
            "what": request.form.get("what", "python dev"),
        }
        # Ajoutez chaque paramètre seulement s'il a été fourni
        for key in [
            "where",
            "category",
            "distance",
            "salary_min",
            "permanent",
            "part_time",
            "full_time",
            "contract",
        ]:
            value = request.form.get(key)
            if value:
                query_params[key] = value
        recherche = Recherche(query_params=query_params)
        offres = recherche_service.obtenir_resultats(recherche)
    else:
        offres = []
    return render_template("index.html", offres=offres)


@app.route("/offre/<int:offre_id>")
def offre(offre_id):
    # Cette fonction pourrait récupérer des détails supplémentaires sur l'offre sélectionnée
    return f"Détails de l'offre {offre_id}"

@app.route("/se_connecter", methods=['GET', 'POST'])
def se_connecter():
    utilisateur = None  # Initialise la variable utilisateur à None
    erreur = None  # Initialise la variable erreur à None
    if request.method == "POST":
        mail = request.form.get('mail')  # Récupère le mail du formulaire
        mdp = request.form.get('mdp')    # Récupère le mot de passe du formulaire
        
        utilisateur = Utilisateur().se_connecter(mail=mail, passw=mdp)
        if utilisateur is None:
            erreur = 'Connexion échouée, veuillez réessayer'
        else:
            session['user_id'] = utilisateur.id  # Suppose que utilisateur.id contient l'ID utilisateur
            return redirect(url_for('profil'))  # Redirige vers la page profil si la connexion est réussie
    
    return render_template("connexion.html", utilisateur=utilisateur, erreur=erreur)

@app.route("/profil")
def profil():
    utilisateur = obtenir_utilisateur_actuel()
    print(utilisateur)
    if utilisateur is None:
        return redirect(url_for('se_connecter'))  # Redirige vers la page de connexion si aucun utilisateur connecté
    return render_template("profil.html", utilisateur=utilisateur)

def obtenir_utilisateur_actuel():
    user_id = session.get('user_id')
    return UtilisateurDao().recuperer_utilisateur(user_id)  # Supposons que cette méthode récupère l'utilisateur par ID


if __name__ == "__main__":
    app.run(debug=True)
