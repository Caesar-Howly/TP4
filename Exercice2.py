import random


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


class NPC:
    def __init__(self, nom, race, espece, profession):
        self.force = stats()
        self.agilite = stats()
        self.constitution = stats()
        self.intelligence = stats()
        self.sagesse = stats()
        self.charisme = stats()
        self.classe_armour = random.randint(1, 12)
        self.nom = nom
        self.race = race
        self.espece = espece
        self.point_de_vie = 20
        self.profession = profession

    def show_characteristics(self):
        print(f"Force =")
        print(f"Agilité = ")
        print(f"Constitution = ")
        print(f"Intelligence = ")
        print(f"Sagesse = ")
        print(f"Charisme = ")
        print(f"Classe d'armour = ")
        print(f"Nom = ")
        print(f"Race = ")
        print(f"Espece = ")
        print(f"Vie = ")
        print(f"Profession = ")
