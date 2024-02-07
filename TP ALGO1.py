# Définir une classe Fraction
class Fraction:
    # Définir le constructeur
    def __init__(self, num, den):
        # Vérifier que le dénominateur est un entier strictement positif
        assert isinstance(
            den, int) and den > 0, "Le dénominateur doit être un entier strictement positif"
        # Affecter les attributs privés
        self._num = num
        self._den = den

    # Définir la méthode spéciale str (self)
    def __str__(self):
        # Si le dénominateur vaut 1, renvoyer seulement le numérateur
        if self._den == 1:
            return str(self._num)
        # Sinon, renvoyer la fraction sous la forme 'numerateur/denominateur'
        else:
            return f"{self._num}/{self._den}"

    # Définir la méthode spéciale eq (self, other)
    def __eq__(self, other):
        # Vérifier que l'autre objet est une instance de la classe Fraction
        if isinstance(other, Fraction):
            # Renvoyer True si les fractions sont égales, c'est-à-dire si le produit en croix est égal
            return self._num * other._den == self._den * other._num
        # Sinon, renvoyer False
        else:
            return False


# Créer les instances F1, F2, F3 et F4
F1 = Fraction(3, 4)
F2 = Fraction(-8, 1)
F3 = Fraction(2, 3)
F4 = Fraction(21, 28)

# Afficher les instances
print("F1 =", F1)
print("F2 =", F2)
print("F3 =", F3)
print("F4 =", F4)

# Comparer les instances
print("F1 == F2 ?", F1 == F2)
print("F1 == F3 ?", F1 == F3)
print("F1 == F4 ?", F1 == F4)
print("F2 == F3 ?", F2 == F3)
print("F2 == F4 ?", F2 == F4)
print("F3 == F4 ?", F3 == F4)
