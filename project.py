import random
import time
import json
import unittest



class Proffession:
    has_artifact = False
    def __init__(self, strength, agility, vitality, intelegence, spirit,
                 charm, level, expirience):
        self.strength = strength + level * 10 / 100 * strength
        self.agility = agility + level * 10 / 100 * agility
        self.vitality = vitality + level * 10 / 100 * vitality
        self.intelegence = intelegence + level * 10 / 100 * vitality
        self.spirit = spirit +  level * 10 / 100 * spirit
        self.charm = charm + level * 10 / 100 * charm
        self.level = level
        self.expirience = expirience
        self.total_health = self.vitality * level * 10
        self.total_stamina = self.vitality * level * 20
        self.total_mana = self.intelegence * level * 10
        self.mana_recovery_per_round = self.intelegence * level / 100
        self.current_hp = self.total_health
        self.current_mana = self.total_mana


    def is_alive(self):
        return self.current_hp > 0


    def get_hp(self):
        return self.current_hp


    def get_hit(self, hit):
        self.current_hp -= hit
        if self.current_hp <= 0:
            print(self, "died")


    def get_healed(self, heal):
        if not self.is_alive():
            return False
        if self.current_mana > 0:
            self.current_hp += heal
            self.current_mana -= heal * 2
            if self.current_hp > self.total_health:
                self.current_hp = self.total_health

            
    def equip(self, artifact):
        self.artifact = artifact
        self.has_artifact = True


    def hit(self):
        if self.has_artifact:
            return self.strength * 3 + self.artifact.hit()
        else:
            return self.strength * 5


    def level_up(self):
        if self.expirience >= 100 * self.level:
            print("Congratulation you leveled up")
            self.expirience = self.expirience - 100 * self.level
            self.level = self.level + 1


    def stats(self):
        print("strength:")
        print(self.strength)
        print("agility:")
        print(self.agility)
        print("vitality:")
        print(self.vitality)
        print("intelegence:")
        print(self.intelegence)
        print("spirit:")
        print(self.spirit)
        print("charm:")
        print(self.charm)
        print("level:")
        print(self.level)
        print("expirience:")
        print(self.expirience)
        print("total_health:")
        print(self.total_health)
        print("total_stamina:")
        print(self.total_stamina)
        print("total_mana:")
        print(self.total_mana)
        print("current_hp:")
        print(self.total_health)

    
class Warrior(Proffession):
    def __str__(self):
        return "Warrior"


    
class Archer(Proffession):
    def __str__(self):
        return "Archer"


    
class Mage(Proffession):


    def hit(self):
        if self.has_artifact:
            return self.intelegence * 3 * self.level + self.artifact.hit()
        else:
            return self.intelegence * 5 * self.level

        
    def __repr__(self):
        return "Mage"


    
class Thief(Proffession):
    def __str__(self):
        return "Thief"


    
class Priest(Proffession):
    def __str__(self):
        return "Priest"



class Monster:
    has_artifact = False
    def __init__(self, name, enrage, level):
        self.name = name
        self.total_health = 100 * level
        self.enrage = enrage
        self.current_hp = self.total_health
        self.level = level
        self.base_damage = 10 * level


    def is_alive(self):
        return self.current_hp > 0


    def get_hp(self):
        return self.current_hp


    def get_hit(self, hit):
        self.current_hp -= hit
        if self.current_hp <= 0:
            print(self, "died")


    def get_healed(self, heal):
        if not self.is_alive():
            return False
        self.current_hp += heal
        if self.current_hp > self.total_health:
            self.current_hp = self.total_health


    def equip(self, artifact):
        self.artifact = artifact
        self.has_artifact = True


    def hit(self):
        if self.has_artifact:
            return self.base_damage + round(self.artifact.hit() * self.enrage ** self.enrage, 2)
        else:
            return self.base_damage


    def respawn(self):
        self.current_hp = self.total_health


        
class Goblin(Monster):
    def __init__(self, name, enrage, level):
        self.name = name
        self.total_health = 100 * level
        self.enrage = enrage
        self.current_hp = self.total_health
        self.level = level
        self.base_damage = 10 * level

        
    def __repr__(self):
        return "Goblin"


    
class Orc(Monster):
    def __init__(self, name, enrage, level):
        self.name = name
        self.total_health = 100 * level * 10
        self.enrage = enrage
        self.current_hp = self.total_health
        self.level = level
        self.base_damage = 10 * level * 2


    def __repr__(self):
        return "Orc"

    
class Orge(Monster):
    def __init__(self, name, enrage, level):
        self.name = name
        self.total_health = 100 * level * 5
        self.enrage = enrage
        self.current_hp = self.total_health
        self.level = level
        self.base_damage = 10 * level * 3
        
        
    def __repr__(self):
        return "Orge"


    
class Dragon(Monster):
    def __init__(self, name, enrage, level):
        self.name = name
        self.total_health = 100 * level * 20
        self.enrage = enrage
        self.current_hp = self.total_health
        self.level = level
        self.base_damage = 10 * level * 10
        
        
    def __repr__(self):
        return "Dragon"
    
    
    def dragon_breath(self):
        return self.base_damage * 50



class Artifact:
    def __init__(self, name, damage, critical_strike):
        self.name = name
        self.damage = damage
        self.cr = critical_strike
        

    def is_crit(self):
        return random.randint(0, 100) < self.cr


    def hit(self):
        if self.is_crit():
            return round(self.damage * 2, 2)
        return round(self.damage, 2)

    

class Sword(Artifact):
    def __init__(self, name, damage, critical_strike):
        self.name = name
        self.damage = damage * 2
        self.cr = critical_strike / 2

    def __repr__(self):
        return self.name



class Blunt(Artifact):
    def __init__(self, name, damage, critical_strike):
        self.name = name
        self.damage = damage / 2
        self.cr = critical_strike * 2

        def __repr__(self):
            return self.name
    


class Magic_Ball(Artifact):
    def double_mana(self, mana):
        mana = mana * 2
        return mana

    def __repr__(self):
        return self.name



def battle_with_orc(player, enemy):
    while player.is_alive() and enemy.is_alive():

        if enemy.get_hp() > 30 / 100 * enemy.total_health:

            if random.randint(0,5) > 2 or player.get_hp() == player.total_health:
                temp = player.hit()
                print(player, "hits", enemy, "for", temp)
                enemy.get_hit(temp)
                time.sleep(1)

            if player.get_hp() < 50 / 100 * player.total_health:
                temp = random.randint(0, 200)
                temp = temp * player.level

                if player.current_mana > 0:
                    player.get_healed(temp)
                    print(player, "heals for", temp)
                    time.sleep(1)

            if player.is_alive() and not enemy.is_alive():

                if enemy.level > player.level:
                    player.expirience += (enemy.level - player.level) * 5
                    player.level_up()
                
            if not player.is_alive() and enemy.is_alive():

                if player.level > enemy.level:
                    player.expirience -= (player.level - enemy.level) * 5

                else:
                    player.expirience -= (enemy.level - player.level)
                    
            if not player.is_alive() or not enemy.is_alive():

                break;

            if random.uniform(0, player.agility) < 2 or enemy.get_hp() == enemy.total_health:
                temp = enemy.hit()
                print(enemy, "hits", player, "for", temp)
                player.get_hit(temp)
                time.sleep(1)
        else:
            if random.randint(0,10) > 3 or player.get_hp() == player.total_health:
                temp = player.hit()
                print(player, "hits", enemy, "for", temp)
                enemy.get_hit(temp)
                time.sleep(1)
            if player.get_hp() < 50 / 100 * player.total_health:
                temp = random.randint(0, 200)
                temp = temp * player.level
                if player.current_mana > 0:
                    player.get_healed(temp)
                    print(player, "heals for", temp)
                    time.sleep(1)

            if player.is_alive() and not enemy.is_alive():
                if enemy.level > player.level:
                    player.expirience += (enemy.level - player.level) * 5
                    player.level_up()
                
            if not player.is_alive() and enemy.is_alive():
                if player.level > enemy.level:
                    player.expirience -= (player.level - enemy.level) * 5
                else:
                    player.expirience -= (enemy.level - player.level)
                    
            if not player.is_alive() or not enemy.is_alive():
                break;


            if random.uniform(0, player.agility) < 1 or enemy.get_hp() == enemy.total_health:
                temp = enemy.hit() * 3
                enemy.get_healed(temp / 2)
                print(enemy, "hits", player, "for", temp)
                player.get_hit(temp)
                time.sleep(1)
    


def battle_with_orge(player, enemy):
    while player.is_alive() and enemy.is_alive():
        if random.randint(0,5) > 3 or player.get_hp() == player.total_health:
            temp = player.hit()
            print(player, "hits", enemy, "for", temp)
            enemy.get_hit(temp)
            time.sleep(1)
        if player.get_hp() < 50 / 100 * player.total_health:
                temp = random.randint(0, 200)
                temp = temp * player.level
                if player.current_mana > 0:
                    player.get_healed(temp)
                    print(player, "heals for", temp)
                    time.sleep(1)

        if player.is_alive() and not enemy.is_alive():
            if enemy.level > player.level:
                player.expirience += (enemy.level - player.level) * 5
                player.level_up()
                
        if not player.is_alive() and enemy.is_alive():
            if player.level > enemy.level:
                player.expirience -= (player.level - enemy.level) * 5
            else:
                player.expirience -= (enemy.level - player.level)
                    
                
        if not player.is_alive() or not enemy.is_alive():
            break;
            
        if random.uniform(0, player.agility) < 3 or enemy.get_hp() == enemy.total_health:
            temp = enemy.hit()
            print(enemy, "hits", player, "for", temp)
            player.get_hit(temp)
            time.sleep(1)


            
def battle_with_goblin(player, enemy):
    while player.is_alive() and enemy.is_alive():
        if random.randint(0,100) > 77 or player.get_hp() == player.total_health:
            temp = player.hit()
            print(player, "hits", enemy, "for", temp)
            enemy.get_hit(temp)
            time.sleep(1)
        if player.get_hp() < 50 / 100 * player.total_health:
                temp = random.randint(0, 200)
                temp = temp * player.level
                if player.current_mana > 0:
                    player.get_healed(temp)
                    print(player, "heals for", temp)
                    time.sleep(1)

        if player.is_alive() and not enemy.is_alive():
            if enemy.level > player.level:
                player.expirience += (enemy.level - player.level) * 5
                player.level_up()
                
        if not player.is_alive() and enemy.is_alive():
            if player.level > enemy.level:
                player.expirience -= (player.level - enemy.level) * 5
            else:
                player.expirience -= (enemy.level - player.level)
                    
                
        if not player.is_alive() or not enemy.is_alive():
            break
            
        if random.uniform(0, player.agility) < 2 or enemy.get_hp() == enemy.total_health:
            temp = enemy.hit() / 2
            print(enemy, "hits", player, "for", temp)
            player.get_hit(temp)
            time.sleep(1)



def battle_with_dragon(player, enemy):
    while player.is_alive() and enemy.is_alive():
        if random.randint(0,100) > 40 or player.get_hp() == player.total_health:
            temp = player.hit()
            print(player, "hits", enemy, "for", temp)
            enemy.get_hit(temp)
            time.sleep(1)
        if player.get_hp() < 50 / 100 * player.total_health:
                temp = random.randint(0, 200)
                temp = temp * player.level
                if player.current_mana > 0:
                    player.get_healed(temp)
                    print(player, "heals for", temp)
                    time.sleep(1)

        if player.is_alive() and not enemy.is_alive():
            if enemy.level > player.level:
                player.expirience += (enemy.level - player.level) * 5
                player.level_up()
                
        if not player.is_alive() and enemy.is_alive():
            if player.level > enemy.level:
                player.expirience -= (player.level - enemy.level) * 5
            else:
                player.expirience -= (enemy.level - player.level)
                    
                
        if not player.is_alive() or not enemy.is_alive():
            break;
            
        if random.uniform(0, player.agility) < 3 or enemy.get_hp() == enemy.total_health:
            if(enemy.get_hp() < 50 or enemy.get_hp() < 30):
                if random.randint(0, 3) > 1:
                    temp = enemy.dragon_breath()
                    print(enemy, "uses Dragon breath to hit for", temp)
                    player.get_hit(temp)
                    time.sleep(1)
            else:
                temp = enemy.hit()
                print(enemy, "hits", player, "for", temp)
                player.get_hit(temp)
                time.sleep(1)
            


class Account:
    
    def __init__ (self, name = 'Name', age = 20, gender = 'male',
                  Proffession = Mage(5,5,5,10,6,5,7,112)):
        self.name = name
        self.age = age
        self.gender = gender
        self.Proffession = Proffession


    def __repr__(self):
        return self.name



h1 = Account()




def login():
    
    with open('data.json') as f:
        data = json.load(f)
        name = input("What is your ingame name?\n")
        for i in range(1, 10):
            if name == data["Player"][i]['name']:
                print("Successfull login!")
                name = data["Player"][i]['name']
                age = data["Player"][i]['age']
                gender = data["Player"][i]['gender']
                Proffession = data["Player"][i]['Proffession']
                h1.name = name
                h1.age = age
                h1.gender = gender
                h1Proffesion = Proffession
                break




d = {"name": "Kamen", "age": 15, "gender": "male",
     "Proffession": "Mage(5,5,5,10,6,5,7,112)"}



def register():
    with open("data.json", "r+") as file:
        name = input("What is your name?")
        age = input("What is your age?")
        gender = input("What is your gender")
        data = json.load(file)
        data.update(d)
        file.seek(0)
        json.dump(data, file)




def menu():
    
    print("Welcome to my game!!!")
    n = input("Do you want to sign in or sign up?\n")
    if n == "sign in":
        login()
        print("Your stats:\n")
        h1.Proffession.stats()
        
    if n == "sign up":
        register()
        print("If after this your games crashes, we are sorry," +
              " please preinstall the game!")
        
    i = input("If you are new or have forgoten the game, you could play" +
              " tutorial or play directly?\n")
    
    if i == "Tutorial" or i == "tutorial":
        print("Coming soon")
        return None
    
    if i == "Directly" or i == "directly":
        
        z = input("What monster do you want to play against?" +
                  "(Orc, Goblin, Orge, Dragon)\n")
        
        if z == "Orc" or z == "orc":
            battle_with_orc(h1.Proffession, Orc("Garry", 1.8, h1.Proffession.level + 2))
                
        if z == "Orge" or z == "orge":
            battle_with_orge(h1.Proffession, Orge("Zako", 1.5, h1.Proffession.level + 3))
                
        if z == "Goblin" or z == "goblin":
            battle_with_goblin(h1.Proffession, Goblin("Parry", 1.2, h1.Proffession.level + 1))
                
        if z == "Dragon" or z == "dragon":
            battle_with_dragon(h1.Proffession, Dragon("Undrela", 1, h1.Proffession.level + 5))





menu()







#testove
import unittest


z1  = Account("Admin", 123, "binary", Mage(8, 8, 8, 10, 10, 9, 15, 0))
w1 = Warrior(5, 5, 5, 5, 5, 5, 5, 5)
a1 = Archer(5, 5, 5, 5, 5, 5, 5, 5)
t1 = Thief(5, 5, 5, 5, 5, 5, 5, 5)
p1 = Priest(5, 5, 5, 5, 5, 5, 5, 5)
g1 = Goblin("asap", 1.3, 12)
orc1 = Orc("davaj", 4, 10)
orge1 = Orge("bujstra", 3, 13)
d1 = Dragon("Galep", 1, 15)
basic_sword = Sword("basic_sword", 10, 2)
b1 = Blunt("Basic blunt weapon", 30, 30)
mb1 = Magic_Ball("Basic magic ball", 50, 20)


class SimpleTest(unittest.TestCase):


    def test1(self):
        self.assertTrue(z1.Proffession.is_alive())

    def test2(self):
        self.assertTrue(z1.Proffession.get_hp())

    def test3(self):
        self.assertIsNone(z1.Proffession.get_hit(20))

    def test4(self):
        self.assertIsNone(z1.Proffession.get_healed(20))

    def test5(self):
        self.assertIsNone(z1.Proffession.equip(basic_sword))

    def test6(self):
        self.assertIsNotNone(z1.Proffession.hit())
        
    def test7(self):
        self.assertIsNone(z1.Proffession.level_up())
        
    def test8(self):
        self.assertIsNone(z1.Proffession.stats())

    def test9(self):
        self.assertIsNotNone(z1.Proffession)

    def test10(self):
        self.assertIsNotNone(w1)
        
    def test11(self):
        self.assertIsNotNone(a1)
        
    def test12(self):
        self.assertIsNotNone(t1)
        
    def test13(self):
        self.assertIsNotNone(p1)
        
    def test14(self):
        self.assertIsNone(g1.respawn())

    def test15(self):
        self.assertIsNotNone(g1)
        
    def test16(self):
        self.assertIsNotNone(orc1)
        
    def test17(self):
        self.assertIsNotNone(orge1)

    def test18(self):
        self.assertIsNotNone(d1)

    def test19(self):
        self.assertIsNotNone(d1.dragon_breath)

    def test20(self):
        self.assertIsNotNone(basic_sword.hit)

    def test21(self):
        self.assertIsNotNone(basic_sword.is_crit)
        
    def test22(self):
        self.assertIsNotNone(basic_sword)

    def test23(self):
        self.assertIsNotNone(b1)

    def test24(self):
        self.assertIsNotNone(mb1)

    def test25(self):
        self.assertEqual(mb1.double_mana(20), 40)

    def test26(self):
        self.assertIsNotNone(battle_with_goblin)

    def test27(self):
        self.assertIsNotNone(battle_with_orc)

    def test28(self):
        self.assertIsNotNone(battle_with_orge)

    def test29(self):
        self.assertIsNotNone(battle_with_dragon)

    

if __name__ == '__main__':
    unittest.main()

        
