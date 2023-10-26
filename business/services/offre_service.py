from business.client.offre import Offre
from business.client.compte_utilisateur import CompteUtilisateur

class OffreService:
    def mettre_en_favoris(self, offre):
        offre.etre_en_favoris = True
        return

    def voir_favoris(self) -> List[Offre]:
        
