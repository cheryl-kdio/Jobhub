
class Memory: # Création classe de stockage 
    db={} # Utilisation d'un dictionnaire pour le stockage avec ID interne comme key 
        
    def add_db(self,id,value):
        self.db[id]=value # Fonction d'ajout à notre dictionnaire

    def drop_id(self,id):
        self.db.pop(id) # Fonction de Suppression à notre dictionnaire 
    def iterer_donnees(self):
        return list(self.db.items())
    
    def recuperer_utilisateur(self, id):
        # Récupère les données d'un utilisateur depuis la base de données partagée
        return self.db.get(id)
    
    def afficher_db(self) : # Affiche l'ensemble de la base de données
        for id, value in self.db.items():
            print(f"id : {id}, Données : {value}")


        