import random


"""
EXERCICE 2
"""


def stats():
    list_of_dice = [random.randint(1,6) for _ in range(4)]
    list_of_dice.sort(reverse=True)
    list_of_dice.pop()
    return sum(list_of_dice)


stat = stats()
print(stat)


class NPC:
    def __init__(self):
        self.force = stats()
        self.agilite = stats()
        self.constitution = stats()
        self.intelligence = stats()
        self.sagesse = stats()
        self.charisme = stats()
        self.classe_armour = random.randint(1, 12)
        self.nom = ""
        self.race = ""
        self.espece = ""
        self.point_de_vie = 20
        self.profession = ""

    def show_characteristics(self):
        print(f"Force = `{self.force}")
        print(f"Agilité = {self.agilite}")
        print(f"Constitution = {self.constitution}")
        print(f"Intelligence = {self.intelligence}")
        print(f"Sagesse = {self.sagesse}")
        print(f"Charisme = {self.charisme}")
        print(f"Classe d'armour = {self.classe_armour}")
        print(f"Nom = {self.nom}")
        print(f"Race = {self.race}")
        print(f"Espece = {self.espece}")
        print(f"Vie = {self.point_de_vie}")
        print(f"Profession = {self.profession}")


class Kobold(NPC):
    def __init__(self):
        super().__init__()

    @staticmethod
    def faire_attaque(cible):
        dommage = random.randint(1, 20)
        if dommage == 20:
            cible.subir_degats(8)
        elif dommage == 1:
            print("Miss")
        else:
            if dommage > cible.classe_armour:
                cible.subir_degats(6)
            else:
                print("Miss")

    def subir_dommage(self, degats):
        self.point_de_vie = self.point_de_vie - degats


class Hero(NPC):

    def __init(self):
        super().__init__()

    @staticmethod
    def faire_attaque(cible):
        dommage = random.randint(1, 20)
        if dommage == 20:
            print("Attaque critique!")
            cible.subir_degats(8)
        elif dommage == 1:
            print("Miss")
        else:
            if dommage > cible.classe_armour:
                cible.subir_degats(6)
            else:
                cible.subir_degats(dommage)

    def subir_dommage(self, degats):
        self.point_de_vie = self.point_de_vie - degats
