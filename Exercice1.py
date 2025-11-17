import random
from math import pi

"""
EXERCICE 1
"""


class StringFoo:
    def __init__(self):
        self.message = "initialiser à rien"

    def set_string(self, msg):
        self.message = msg

    def print_string(self):
        print(self.message.upper())


str1 = StringFoo()
str1.print_string()
str1.set_string("Allo")
str1.print_string()

"""
EXERCICE 2
"""


class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.aire = 0

    def calcul_aire(self):
        self.aire = self.longueur * self.largeur

    def afficher_infos(self):
        print(f"{self.aire} = {self.longueur} + {self.largeur}")


r = Rectangle(10, 9)
r.calcul_aire()
r.afficher_infos()

"""
EXERCICE 3
"""


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.aire = 0
        self.circonference = 0

    def calcul_aire(self):
        self.aire = pi * self.rayon ** 2

    def calcul_circonference(self):
        self.circonference = 2 * pi * self.rayon

    def afficher_infos(self):
        print(self.aire)
        print(self.circonference)


c = Cercle(5)
c.calcul_aire()
c.calcul_circonference()
c.afficher_infos()

"""
EXERCICE 4
"""


class Hero:
    def __init__(self, nom):
        self.vie = random.randint(1, 10) + random.randint(1, 10)
        self.attaque = random.randint(1, 6)
        self.defense = random.randint(1, 6)
        self.nom = nom
        self.dommage = 0

    def faire_attaque(self):
        return random.randint(1, 6) + self.attaque

    def recevoir_dommage(self, dmg):
        self.dommage = dmg
        self.vie -= self.dommage + self.attaque

    def en_vie(self):
        if self.vie > 0:
            print("En vie")
            return True
        else:
            print("Mort")
            return False


hero = Hero("Caesar")
hero.recevoir_dommage(15)
hero.en_vie()