class WaterTank:
    """Classe qui permet la gestion d'une citerne"""

    total_volume = 0

    def __init__(self, poids_vide, capacite_max, niveau_remplissage):
        # Poids à vide en Kg
        self.poids_vide = poids_vide
        # Capacité max de la citerne en litres
        self.capacite_max = capacite_max
        # Niveau de remplissage de la citerne en litres
        self.niveau_remplissage = niveau_remplissage
        WaterTank.total_volume += niveau_remplissage

    @property
    def poids_total(self):
        return self.poids_vide + self.capacite_max

    def remplir_citerne(self, nb_litres):
        """
        Remplir la citerne

        nb_litres: Nombre de litres à ajouter
        returns: Nombre de litres réellement ajoutés
        """
        nb_litres_ajoutes = nb_litres if self.niveau_remplissage + nb_litres <= self.capacite_max \
            else self.capacite_max - self.niveau_remplissage

        self.niveau_remplissage += nb_litres_ajoutes
        WaterTank.total_volume += nb_litres_ajoutes
        return nb_litres_ajoutes

    def vider_citerne(self, nb_litres):
        """
        Vider la citerne

        nb_litres: Nombre de litres à enlever
        returns: Nombre de litres réellement enlevés
        """
        nb_litres_retires = nb_litres if self.niveau_remplissage - nb_litres >= 0 \
            else self.niveau_remplissage

        self.niveau_remplissage -= nb_litres_retires
        WaterTank.total_volume -= nb_litres_retires
        return nb_litres_retires


citerne1 = WaterTank(100, 1000, 0)
citerne2 = WaterTank(100, 1000, 0)
print(WaterTank.total_volume)

citerne1.remplir_citerne(250)
citerne2.remplir_citerne(500)
print(WaterTank.total_volume)

citerne1.vider_citerne(300)
citerne2.remplir_citerne(600)
print(WaterTank.total_volume)

print(f"Poids total: {citerne2.poids_total}")
