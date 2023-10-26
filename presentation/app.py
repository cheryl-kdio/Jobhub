from flask import Flask, render_template, request
from business.client.recherche import Recherche
from business.client.compte_utilisateur import CompteUtilisateur
from business.dao.recherche_dao import RechercheDao
from business.services.recherche_service import RechercheService
from business.dao.utilisateur_dao import UtilisateurDao


app = Flask(__name__)
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


@app.route("/se_connecter")
def se_connecter():
    # Cette fonction pourrait récupérer des détails supplémentaires sur l'offre sélectionnée
    if request.method == "POST":
        mail = request.form.get(mail)
        mdp = request.form.get(mdp)

        utilisateur = Utilisateur().se_connecter()

    return render_template("connexion.html")


if __name__ == "__main__":
    app.run(debug=True)
