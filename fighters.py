from fighter import fighter
from effects import *
import random

class Warrior(fighter):
    className = "Warrior"
    effects = []

    def __init__(self, health=126.0, attack=15.0, defense=4.0, speed=1.5, name="Boi", decideMove = None):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        if decideMove:
            self.decideMove = decideMove

    # Wild swing
    class attack1:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * (random.randint(6, 16)/10.0)

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= appliedDamage
            print(fighter.className + " " + fighter.name + " wildly swings at " + opponent.className + " " +
                  opponent.name + " for " + str(appliedDamage) + " damage!")
            return fighter, opponent

    # Battle roar
    class attack2:
        def __init__(self, fighter):
            self.fighter = fighter
            self.amount = 6
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
            self.damage = fighter.attack * 0.80 * (random.randint(8, 12)/10)

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage, 0.5)
            opponent.health -= appliedDamage
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " with a piercing blow for " + str(self.damage) + " damage!")
            return fighter, opponent

    # Pommel Strike
    class attack4:
        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.55 * (random.randint(8, 12)/10)
            self.stunChance = 35
            self.stunDuration = 1
            self.stunDurationRange = 0

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= appliedDamage
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " with their pommel, damaging them for " + str(appliedDamage) + " damage!")
            if random.randint(0,100) < self.stunChance:
                opponent.effects.append(stunned(fighter,opponent,self.stunDuration + random.randint(0, self.stunDurationRange)))
                print(opponent.className + " " + opponent.name + " was stunned!")
            return fighter, opponent



class Healer(fighter):
    effects = []

    def __init__(self, health=81.0, attack=10.0, defense=3.0, speed=3.0, name="Boi", decideMove = None):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.className = "Healer"
        if decideMove:
            self.decideMove = decideMove

    # Retribution
    class attack1:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * (random.randint(8, 12)/10)

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
            self.amount = 5.5
            self.duration = 6

        def effect(self, fighter, opponent):
            fighter.effects.append(healOverTime(fighter, fighter, self.duration, self.amount ))
            print(fighter.className + " " + fighter.name + " started healing!")
            return fighter, opponent

    # Purify
    class attack3:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.3 * (random.randint(8, 12)/10)
            self.names = ["Assassin", "Warrior", "Healer", "Juggernaut"]
            self.defaultDefense = [0, 2, 3, 8]
            self.defaultAttack = [20, 15, 10, 5]

        def effect(self, fighter, opponent):
            eff = opponent.effects
            appliedDamage = self.damage * len(eff)
            opponent.effects = []
            for i in range(len(self.names)):
                if opponent.className == self.names[i]:
                    opponent.defense = self.defaultDefense[i]
                    opponent.attack = self.defaultAttack[i]
            fighter.health -= 5 - 0.5 * appliedDamage
            opponent.health -= appliedDamage
            print(fighter.className + " " + fighter.name + " purifies " + opponent.className + " " +
                  opponent.name + ", causing 5 damage to themself and dealing " + str(appliedDamage)
                  + " damage, removing all effects!")
            return fighter, opponent

    # Test of Faith
    class attack4:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack  * (random.randint(8, 12)/10)
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
    effects = []
    className = "Assassin"

    def __init__(self, health=58.0, attack=20.0, defense=0.0, speed=5.0, name="Boi", decideMove = None):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.className = "Assassin"
        if decideMove:
            self.decideMove= decideMove

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
            self.damage = fighter.attack  * (random.randint(8, 12)/10)
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
            self.revealChance = 20

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
            self.damage = fighter.attack * 0.95  * (random.randint(8, 12)/10)
            self.revealChance = 25
            self.amount = 3
            self.duration = 3

        def effect(self, fighter, opponent):
            opponent.health -= max(self.damage, 0.5)
            opponent.effects.append(soften(fighter,opponent, self.duration, self.amount))
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " in the back for " + str(self.damage) + " damage and lowering their defense by " +
                  str(self.amount) + "!")
            fighter.sharpenBlade(self.revealChance)
            return fighter, opponent

    # Poisoned blade
    class attack4:
        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * 0.55  * (random.randint(8, 12)/10)
            self.duration = 4
            self.poisonDamage = 3
            self.revealChance = 15

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= max(appliedDamage, 0.5)
            eff = opponent.effects
            multiplier = 1.5
            for effect in eff:
                if isinstance(effect, healOverTime):
                    multiplier += 0.75
            print(fighter.className + " " + fighter.name + " strikes " + opponent.className + " " +
                  opponent.name + " with a poisoned blade, damaging them for " + str(self.damage) + " damage!")
            if random.randint(0,100) < 75:
                opponent.effects.append(poisoned(fighter,opponent,self.duration, self.poisonDamage * multiplier))
                print(opponent.className + " " + opponent.name + " was poisoned!")
            fighter.sharpenBlade(self.revealChance)
            return fighter, opponent

    def decideMove(self, opponent):
        return random.choice([self.attack1(self), self.attack2(self), self.attack3(self), self.attack4(self)])




class Juggernaut(fighter):
    effects = []

    def __init__(self, health=150.0, attack=5.0, defense=8.0, speed=3.0, name="Boi", decideMove = None):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.name = name
        self.className = "Juggernaut"
        if decideMove:
            self.decideMove = decideMove

    # Shield bash
    class attack1:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack + (fighter.defense * 0.40) * (random.randint(8, 12)/10)
            self.stunChance = 25
            self.stunDuration = 1

        def effect(self, fighter, opponent):
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= appliedDamage
            print(fighter.className + " " + fighter.name + " bashes " + opponent.className + " " +
                  opponent.name + " with their shield, damaging them for " + str(self.damage) + " damage!")
            if random.randint(0, 100) < self.stunChance:
                opponent.effects.append(stunned(fighter, opponent, self.stunDuration))
                print(opponent.className + " " + opponent.name + " was stunned!")
            return fighter, opponent

    # Bulwark
    class attack2:
        def __init__(self, fighter):
            self.fighter = fighter
            self.amount = 5
            self.duration = 4
            self.extraChance = 35
            self.extraAmount = 5

        def effect(self, fighter, opponent):
            if random.randint(0, 100) < self.extraChance:
                self.amount += self.extraAmount
            fighter.effects.append(harden(fighter, fighter, self.duration, self.amount))
            print(fighter.className + " " + fighter.name + " braces, raising their defense by " +
                  str(self.amount) + "!")
            return fighter, opponent
    # Bone Breaker
    class attack3:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.attack * (random.randint(8, 12)/10)
            self.duration = 4
            self.stunChance = 15
            self.stunDuration = 1
            self.amount = 3

        def effect(self, fighter, opponent):
            if opponent.attack <= 10:
                self.amount = 2

            if opponent.attack >= 20:
                self.amount = 4
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            opponent.health -= appliedDamage
            opponent.effects.append(weaken(fighter,opponent,self.duration, self.amount))
            print(fighter.className + " " + fighter.name + " pummels " + opponent.className + " " +
                  opponent.name + " for " + str(appliedDamage) + " damage and reduces their attack by " +
                  str(self.amount) + "!")
            if random.randint(0, 100) < self.stunChance:
                opponent.effects.append(stunned(fighter, opponent, self.stunDuration))
                print(opponent.className + " " + opponent.name + " was stunned!")

            return fighter, opponent

    # The Fury
    class attack4:

        def __init__(self, fighter):
            self.fighter = fighter
            self.damage = fighter.defense * 0.85 * (random.randint(8, 12)/10)
            self.duration = 3
            self.lastTurn = 0
            self.rageDamage = fighter.attack * 1.15 * (random.randint(8, 12)/10)

        def effect(self, fighter, opponent):
            if fighter.turn - self.lastTurn <= 4:
                appliedDamage = max(self.rageDamage - opponent.defense, 0.5)
                print(fighter.className + " " + fighter.name + " rages, dealing " + str(appliedDamage) + " damage!")
                return fighter, opponent
            appliedDamage = max(self.damage - opponent.defense, 0.5)
            self.lastTurn = fighter.turn
            opponent.health -= appliedDamage
            fighter.effects.append(soften(fighter, fighter, self.duration, fighter.defense))
            fighter.effects.append(strengthen(fighter, fighter, self.duration, fighter.defense))
            print(fighter.className + " " + fighter.name +
                  " breaks out in a rage, shedding his defense, raising his attack to " + str(fighter.attack + fighter.defense) +
                  " and damaging " + opponent.className + " " + opponent.name + " for " + str(appliedDamage) +
                  " damage!")
            return fighter, opponent



