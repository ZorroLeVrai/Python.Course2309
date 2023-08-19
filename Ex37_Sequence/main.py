class IntervalError(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

class Intervalle:
    def __init__(self, borne_inferieure, borne_superieure):
        format_valide = verifier_bon_format(borne_inferieure) \
            and verifier_bon_format(borne_superieure) \
            and borne_inferieure <= borne_superieure
        if not format_valide:
            raise IntervalError("Erreur: Bornes Invalides!")
        self.__inf = borne_inferieure
        self.__sup = borne_superieure

    def modif_borne_sup(self, val):
        format_valide = verifier_bon_format(val) \
            and val >= self.__inf
        if not format_valide:
            raise IntervalError("Erreur: Bornes Invalides!")
        self.__sup = val

    def modif_borne_inf(self, val):
        format_valide = verifier_bon_format(val) \
            and val <= self.__sup
        if not format_valide:
            raise IntervalError("Erreur: Bornes Invalides!")
        self.__inf = val

    def lire_inf(self):
        return self.__inf
    
    def lire_sup(self):
        return self.__sup
    
    def __str__(self):
        return f"[{self.__inf}, {self.__sup}]"
    
    def __contains__(self, val):
        return self.__inf <= val <= self.__sup
    
    def __add__(self, other):
        if not isinstance(other, Intervalle):
            return False
        return Intervalle(self.__inf + other.__inf, self.__sup + other.__sup)
    
    def __sup__(self, other):
        if not isinstance(other, Intervalle):
            return False
        return Intervalle(self.__inf - other.__inf, self.__sup - other.__sup)
    
    def __mul__(self, other):
        if not isinstance(other, Intervalle):
            return False
        return Intervalle(self.__inf * other.__inf, self.__sup * other.__sup)
    
    def __and__(self, other):
        if not isinstance(other, Intervalle):
            return None
        borne_inf = max(self.__inf, other.__inf)
        borne_sup = min(self.__sup, other.__sup)
        if borne_inf <= borne_sup:
            return Intervalle(borne_inf, borne_sup)
        else:
            None


def verifier_bon_format(val):
    return isinstance(val, (int, float)) and val > 0


#Utilisation de la classe Intervalle
intervalle1 = Intervalle(1,10)
intervalle1.modif_borne_inf(5)
print(intervalle1)
print(11 in intervalle1)

intervalle2 = Intervalle(7, 14)
print(intervalle1 & intervalle2)