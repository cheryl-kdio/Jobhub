import pytest
from business.dao.utilisateur_dao import UtilisateurDao


utilisateurdao = UtilisateurDao()


def test_get_mail():
    adresses_email = utilisateurdao.get_mail()

    assert isinstance(adresses_email, list)
    assert len(adresses_email) > 0

    for email in adresses_email:
        assert isinstance(email, str)


def test_get_value_from_mail():
    resultat = UtilisateurDao().get_value_from_mail("louise.louise@gmail.com", "nom")

    assert resultat == "louise"
    result = UtilisateurDao().get_value_from_mail("louis.louise@gmail.com", "nom")

    assert result is None


def test_get_mdp_salt():
    resultat = UtilisateurDao().get_salt_mdp("louise.louise@gmail.com")

    assert (
        resultat["mdp"]
        == "$argon2id$v=19$m=65536,t=3,p=4$8DhmVYtGPTnnoC6cdm8rAg$gR7ocn48noQ5oLmoAYOUf79GV0GHZn0chbna8mCpr4E"
    )
    assert resultat["sel"] == "Ij1enqw5lNCTu7N3"


def test_iterer_donnees():
    id_utilisateurs = utilisateurdao.iterer_donnees()
    assert isinstance(id_utilisateurs, list)
    assert len(id_utilisateurs) > 0


def test_recuperer_utilisateur():
    id_utilisateur_existant = 1
    utilisateur = utilisateurdao.recuperer_utilisateur(id_utilisateur_existant)

    assert isinstance(utilisateur, list)

    assert len(utilisateur) > 0

    assert isinstance(utilisateur[0], dict)





if __name__ == "__main__":
    pytest.main()
