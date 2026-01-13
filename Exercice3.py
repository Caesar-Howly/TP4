import random
from enum import Enum

def stats():
    de_1 = random.randint(1, 6)
    de_2 = random.randint(1, 6)
    de_3 = random.randint(1, 6)
    de_4 = random.randint(1, 6)

    list_of_dice = [de_1, de_2, de_3, de_4]
    smallest_die = list_of_dice[0]

    for i in list_of_dice:
        if i < smallest_die:
            smallest_die = i

    ans = de_1 + de_2 + de_3 + de_4 - smallest_die

    return ans


stat = stats()
print(stat)


class Status(Enum):
    lawful_good = 1
    lawful_neutral = 2
    lawful_evil = 3
    neutral_good = 4
    true_neutral = 5
    neutral_evil = 6
    chaotic_good = 7
    chaotic_neutral = 8
    chaotic_evil = 9
    non_defini = 10


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
        self.enum = Enum(random.randint(1, 10))

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
            pass
        else:
            if dommage > cible.classe_armour:
                cible.subir_degats(6)
            else:
                pass

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
            pass
        else:
            if dommage > cible.classe_armour:
                cible.subir_degats(6)
            else:
                cible.subir_degats(dommage)

    def subir_dommage(self, degats):
        self.point_de_vie = self.point_de_vie - degats
