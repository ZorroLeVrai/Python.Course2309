from adn import saisie_adn, proportion

chaine_adn = saisie_adn("Entrez votre chaine ADN: ")
sequence_adn = saisie_adn("Entrez votre séquence ADN: ")

if (chaine_adn is None) or (sequence_adn is None):
    print("La chaine ou la séquence ADN n'est pas valide")
else:
    print(
        f"La proportion de la sequence est de {proportion(chaine_adn, sequence_adn):0.2f}%")
