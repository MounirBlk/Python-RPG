
from math import floor
from random import randint

""" Class Item """

class Item():

    def __init__(self, level, type_personnage):
        # Catact. d'un object
        self.attaque = 1
        self.defense = 1
        self.vitesse = 1
        self.chance = 1
        self.mana = 1
        self.vie = 1

        chance = randint(1, floor((level/2)+1)) # 1.{chance} * catégorie buff
        randItem = floor(randint(0, len(LIST_ITEMS)-1))
        
        self.name = self.get_name_by_key(randItem) # Objet name give
        self.objet = LIST_ITEMS[self.name] # Objet give

        if self.objet["catg"] == 1: # Si object de type attaque
            self.attaque = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 2:
            self.defense = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 3:
            self.vitesse = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 4:
            self.chance = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 5:
            self.mana = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100
        elif self.objet["catg"] == 6:
            self.vie = (1+(2 if type_personnage == self.objet['type_personnage'] else 1)/100)+chance/100

    def get_name_by_key(self, n=0):
        if n < 0:
            n += len(LIST_ITEMS)
        for i, key in enumerate(LIST_ITEMS.keys()):
            if i == n:
                return key
        raise IndexError("dictionary index out of range")

    def __str__(self):
        return "Key:"+str(self.objet["key"])+"\n"+"Name:"+self.name+"\n"+"Type items:"+str(self.objet["catg"])+"\n"+"Attaque:"+str(self.attaque)+"\n"+"Defense:"+str(self.defense)+"\n"+"Vitesse:"+str(self.vitesse)+"\n"+"Chance:"+str(self.chance)+"\n"+"Mana:"+str(self.mana)+"\n"+"Vie:"+str(self.vie)+"\n"

LIST_ITEMS = {
    "Epee": {
        "key": 1,
        "catg": 1,
        "type_personnage": 1,
    },
    "Arc": {
        "key": 2,
        "catg": 1,
        "type_personnage": 1,
    },
    "Baton": {
        "key": 3,
        "catg": 1,
        "type_personnage": 3,
    },
    "Dague": {
        "key": 4,
        "catg": 1,
        "type_personnage": 2,
    },
    "Casque": {
        "key": 5,
        "catg": 2,
        "type_personnage": 1,
    },
    "Bouclier": {
        "key": 6,
        "catg": 2,
        "type_personnage": 1,
    },
    "Fumigene": {
        "key": 7,
        "catg": 2,
        "type_personnage": 2,
    },
    "AirJordan": {
        "key": 8,
        "catg": 3,
        "type_personnage": 2,
    },
    "Moto": {
        "key": 9,
        "catg": 3,
        "type_personnage": 3,
    },
    "Batmobile": {
        "key": 10,
        "catg": 3,
        "type_personnage": 2,
    },
    "Cheval": {
        "key": 11,
        "catg": 3,
        "type_personnage": 1,
    },
    "Trefle": {
        "key": 12,
        "catg": 4,
        "type_personnage": 2,
    },
    "Fer": {
        "key": 13,
        "catg": 4,
        "type_personnage": 1,
    },
    "As": {
        "key": 14,
        "catg": 4,
        "type_personnage": 3,
    },
    "Lapin": {
        "key": 15,
        "catg": 4,
        "type_personnage": 2,
    },
    "Grigri": {
        "key": 16,
        "catg": 5,
        "type_personnage": 2,
    },
    "Talisman": {
        "key": 17,
        "catg": 5,
        "type_personnage": 1,
    },
    "Baguette": {
        "key": 18,
        "catg": 5,
        "type_personnage": 3,
    },
    "Grimoire": {
        "key": 19,
        "catg": 5,
        "type_personnage": 3,
    },
    "Breuvage": {
        "key": 20,
        "catg": 6,
        "type_personnage": 1,
    },
    "Potion": {
        "key": 21,
        "catg": 6,
        "type_personnage": 3,
    },
    "Defribrillateur": {
        "key": 22,
        "catg": 6,
        "type_personnage": 2,
    },
    "Senzu": {
        "key": 23,
        "catg": 6,
        "type_personnage": 3,
    },
    "Bague": {
        "key": 24,
        "catg": 2,
        "type_personnage": 3,
    },
}


if __name__ == "__main__":
    item = Item(10, 1)
    print(item)