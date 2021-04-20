import random
import tkinter
import json

def login():
    f = open('Users.json', "r")
    data = json.load(f.read())
    name = input("What is your ingame name?")
    for i in range(1):
        if(name == ["Users"][i]["name"]):
            print("Successfull login!")
        
    
    f.close()



#def register():

class Proffesion:
    def __init__(self, strength, agility, vitality, intelegence, spirit, charm, level, expirience):
        self.strength = strength
        self.agility = agility
        self.vitality = vitality
        self.intelegence = intelegence
        self.spirit = spirit
        self.charm = charm
        self.level = level
        self.expirience = expirience
        self.total_health = vitality * level * 10
        self.total_mana = intelegence * level * 10
        self.magic_regeneration_per_second = self.total_mana / 100
        self.health_regeneration_per_second = self.total_health / 100
    
class Warrior(Proffesion):
    def __str__(self):
        return "Warrior"
class Archer(Proffesion):
    def __str__(self):
        return "Archer"
class Mage(Proffesion):
    def __str__(self):
        return "Mage"
class Thief(Proffesion):
    def __str__(self):
        return "Thief"
class Priest(Proffesion):
    def __str__(self):
        return "Priest"

class Account:
    def __init__(self, name, age, gender, Proffesion):
        self.name = name
        self.age = age
        self.gender = gender
        self.Proffesion = Proffesion


