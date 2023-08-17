lettres_valides = "atcg"


def verification_adn(chaine_adn):
    if not isinstance(chaine_adn, str):
        return False

    for lettre in chaine_adn:
        if lettre not in lettres_valides:
            return False

    return True


def saisie_adn(message):
    chaine_adn = input(message)
    if verification_adn(chaine_adn):
        return chaine_adn

    return None


def proportion(chaine_adn, sequence_adn):
    nb_occurences = chaine_adn.count(sequence_adn)
    return 100*nb_occurences*len(sequence_adn) / len(chaine_adn)
