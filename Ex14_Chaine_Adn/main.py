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

chaine_adn = saisie_adn("Entrez votre chaine ADN: ")
sequence_adn = saisie_adn("Entrez votre séquence ADN: ")

if (chaine_adn is None) or (sequence_adn is None):
    print("La chaine ou la séquence ADN n'est pas valide")
else:
    print(f"La proportion de la sequence est de {proportion(chaine_adn, sequence_adn)}%")
