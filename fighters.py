from fighter import fighter
from effects import *
import random

class Warrior(fighter):
    className = "Warrior"

    def __init__(self, health=126.0, attack=15.0, defense=2.0, speed=1.5, name="Boi"):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        # self.turn = 0

    def getAttack1(self):
        return self.attack1(self)

    def getAttack2(self):
        return self.attack2(self)

    # Wild swing
    class attack1:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * (random.randint(8, 14)/10.0)

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -=appliedDamage
            print(fighter.className + " " + fighter.name + " wildly swings at " + opponent.className + " " +
                  opponent.name + " for " + str(appliedDamage) + " damage!")
            return fighter, opponent

    # Battle roar
    class attack2:
        def __init__(self, fighter):
            self.fighter = fighter
            self.amount = 5
            self.duration = 4

        def effect(self, fighter, opponent):
            fighter.effects.append(strengthen(fighter, fighter, self.duration, self.amount ))
            print(fighter.className + " " + fighter.name + " roars with fury, increasing their attack by " +
                  str(self.amount) + "!")
            return fighter, opponent

    # Piercing strike
    class attack3:
        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.65

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= max(appliedDamage, 0.5)
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " with a piercing blow for " + str(self.damage) + " damage!")
            return fighter, opponent

    # Pommel Strike
    class attack4:
        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.65

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= max(appliedDamage, 0.5)
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " with their pommel, damaging them for " + str(self.damage) + " damage!")
            if random.randint(0,100) < 35:
                opponent.effects.append(stunned(fighter,opponent,1))
                print(opponent.className + " " + opponent.name + " was stunned!")
            return fighter, opponent

    def decideMove(self, opponent):
        return random.choice([self.attack1(self), self.attack2(self), self.attack3(self), self.attack4(self)])


class Healer(fighter):

    def __init__(self, health=81.0, attack=10.0, defense=3.0, speed=3.0, name="Boi"):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.className = "Healer"
        # self.turn = 0

    def getAttack1(self):
        return self.attack1(self)

    def getAttack2(self):
        return self.attack2(self)

    # Retribution
    class attack1:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= appliedDamage
            fighter.health += self.damage * 0.75
            fighter.health = min(fighter.health, fighter.maxHealth)
            print(fighter.className + " " + fighter.name + " casts retribution on " + opponent.className + " " +
                  opponent.name + " for " + str(appliedDamage) + " damage!")
            print(fighter.className + " " + fighter.name + " heals for " + str(self.damage/3) + " health!")
            return fighter, opponent


    # Healing hand
    class attack2:

        def __init__(self, fighter):
            self.fighter = fighter
            self.amount = 4
            self.duration = 4

        def effect(self, fighter, opponent):
            fighter.effects.append(healOverTime(fighter, fighter, self.duration, self.amount ))
            print(fighter.className + " " + fighter.name + " started healing!")
            return fighter, opponent

    # Purify
    class attack3:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack
            self.amount = 5.75
            self.duration = 5

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage, 0.5)
            fighter.health -= appliedDamage
            fighter.health = min(fighter.health, fighter.maxHealth)
            fighter.effects.append(healOverTime(fighter,fighter,self.duration, self.amount))
            print(fighter.className + " " + fighter.name + " purifies themselves, causing " + str(appliedDamage) +
                  " damage and beginning to heal!")
            return fighter, opponent

    # Test of Faith
    class attack4:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack
            self.amount = 4
            self.duration = 4

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage * 3 - opponent.defense, 0.5)
            opponent.health -= appliedDamage
            fighter.health = min(fighter.health, fighter.maxHealth)
            opponent.effects.append(healOverTime(opponent, opponent, self.duration, self.amount))
            print(fighter.className + " " + fighter.name + " tests " + opponent.className + " " +
                  opponent.name + "'s faith dealing " + str(appliedDamage) + " damage and starting to heal them!")
            return fighter, opponent

    def decideMove(self, opponent):
        return random.choice([self.attack1(self), self.attack2(self), self.attack3(self), self.attack4(self)])


class Assassin(fighter):
    className = "Assassin"

    def __init__(self, health=58.0, attack=20.0, defense=0.0, speed=5.0, name="Boi"):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.className = "Assassin"
        # self.turn = 0

    def getAttack1(self):
        return self.attack1(self)

    def getAttack2(self):
        return self.attack2(self)

    def sharpenBlade(self, chance):
        duration = 6
        amount = 2
        if random.randint(0, 100) < chance:
            print(self.className + " " + self.name + "'s sharpens their blade!")
            self.effects.append(strengthen(self,self,duration,amount))

    # Targeted thrust
    class attack1:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack
            self.revealChance = 35

        def effect(self, fighter, opponent):
            critMessage = ''
            if random.randint(0, 100) < 13:
                self.damage *= 3
                critMessage = ' A critical hit!'
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -=appliedDamage
            print(fighter.className + " " + fighter.name + " performs an expert thrust at " + opponent.className + " " +
                  opponent.name + " for " + str(appliedDamage) + " damage!" + critMessage)
            fighter.sharpenBlade(self.revealChance)
            return fighter, opponent

    # Smoke bomb
    class attack2:
        def __init__(self, fighter):
            self.fighter = fighter
            self.amount = 5
            self.duration = 3
            self.stunChance = 50
            self.stunDuration = 1
            self.revealChance = 10

        def effect(self, fighter, opponent):
            fighter.effects.append(harden(fighter,fighter,self.duration,self.amount))
            print(fighter.className + " " + fighter.name +
                  " casts a smoke bomb, obscuring vision and raising their defense by " + str(self.amount) + "!")
            if random.randint(0, 100) < self.stunChance:
                opponent.effects.append(stunned(fighter, opponent, self.stunDuration))
            fighter.sharpenBlade(self.revealChance)
            return fighter, opponent

    # Backstab
    class attack3:
        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.85
            self.revealChance = 20

        def effect(self, fighter, opponent):
            opponent.health -= max(self.damage, 0.5)
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " in the back for " + str(self.damage) + " damage!")
            fighter.sharpenBlade(self.revealChance)
            return fighter, opponent

    # Poisoned blade
    class attack4:
        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.85
            self.duration = 4
            self.poisonDamage = 3
            self.revealChance = 15

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= max(appliedDamage, 0.5)
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " with a poisoned blade, damaging them for " + str(self.damage) + " damage!")
            if random.randint(0,100) < 55:
                opponent.effects.append(poisoned(fighter,opponent,self.duration, self.poisonDamage))
                print(opponent.className + " " + opponent.name + " was poisoned!")
            fighter.sharpenBlade(self.revealChance)
            return fighter, opponent

    def decideMove(self, opponent):
        return random.choice([self.attack1(self), self.attack2(self), self.attack3(self), self.attack4(self)])



class Healer2(fighter):

    def __init__(self, health=81.0, attack=10.0, defense=3.0, speed=3.0, name="Boi"):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.className = "Healer"
        # self.turn = 0

    def getAttack1(self):
        return self.attack1(self)

    def getAttack2(self):
        return self.attack2(self)

    # Retribution
    class attack1:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= appliedDamage
            fighter.health += self.damage * 0.75
            fighter.health = min(fighter.health, fighter.maxHealth)
            print(fighter.className + " " + fighter.name + " casts retribution on " + opponent.className + " " +
                  opponent.name + " for " + str(appliedDamage) + " damage!")
            print(fighter.className + " " + fighter.name + " heals for " + str(self.damage/3) + " health!")
            return fighter, opponent

    # Healing hand
    class attack2:

        def __init__(self, fighter):
            self.fighter = fighter
            self.amount = 4
            self.duration = 4

        def effect(self, fighter, opponent):
            fighter.effects.append(healOverTime(fighter, fighter, self.duration, self.amount ))
            print(fighter.className + " " + fighter.name + " started healing!")
            return fighter, opponent

    # Purify
    class attack3:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack
            self.amount = 5.75
            self.duration = 5

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage, 0.5)
            fighter.health -= appliedDamage
            fighter.health = min(fighter.health, fighter.maxHealth)
            fighter.effects.append(healOverTime(fighter,fighter,self.duration, self.amount))
            print(fighter.className + " " + fighter.name + " purifies themselves, causing " + str(appliedDamage) +
                  " damage and beginning to heal!")
            return fighter, opponent

    # Test of Faith
    class attack4:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack
            self.amount = 4
            self.duration = 4

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage * 3 - opponent.defense, 0.5)
            opponent.health -= appliedDamage
            fighter.health = min(fighter.health, fighter.maxHealth)
            opponent.effects.append(healOverTime(opponent, opponent, self.duration, self.amount))
            print(fighter.className + " " + fighter.name + " tests " + opponent.className + " " +
                  opponent.name + "'s faith dealing " + str(appliedDamage) + " damage and starting to heal them!")
            return fighter, opponent

    def decideMove(self, opponent):
        return random.choice([self.attack1(self), self.attack2(self), self.attack3(self), self.attack4(self)])


class Warrior2(fighter):
    className = "Warrior"

    def __init__(self, health=126.0, attack=15.0, defense=2.0, speed=1.5, name="Boi"):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        # self.turn = 0

    def getAttack1(self):
        return self.attack1(self)

    def getAttack2(self):
        return self.attack2(self)

    # Wild swing
    class attack1:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * (random.randint(8, 14)/10.0)

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -=appliedDamage
            print(fighter.className + " " + fighter.name + " wildly swings at " + opponent.className + " " +
                  opponent.name + " for " + str(appliedDamage) + " damage!")
            return fighter, opponent

    # Battle roar
    class attack2:
        def __init__(self, fighter):
            self.fighter = fighter
            self.amount = 5
            self.duration = 4

        def effect(self, fighter, opponent):
            fighter.effects.append(strengthen(fighter, fighter, self.duration, self.amount ))
            print(fighter.className + " " + fighter.name + " roars with fury, increasing their attack by " +
                  str(self.amount) + "!")
            return fighter, opponent

    # Piercing strike
    class attack3:
        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.65

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= max(appliedDamage, 0.5)
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " with a piercing blow for " + str(self.damage) + " damage!")
            return fighter, opponent

    # Pommel Strike
    class attack4:
        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.65

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= max(appliedDamage, 0.5)
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " with their pommel, damaging them for " + str(self.damage) + " damage!")
            if random.randint(0,100) < 35:
                opponent.effects.append(stunned(fighter,opponent,1))
                print(opponent.className + " " + opponent.name + " was stunned!")
            return fighter, opponent

    def decideMove(self, opponent):
        return random.choice([self.attack1(self), self.attack2(self), self.attack3(self), self.attack4(self)])
