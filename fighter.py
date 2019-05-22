import random
import effects
class fighter:

    health = 100.0
    attack = 5.0
    defense = 2.0
    speed = 1.5
    chance = 50
    turn = 0
    stunned = False
    name = "Boi"
    effects = []

    def __init__(self, health = 100.0, attack = 5.0, defense = 2.0, speed = 1.5, chance = 50, name = "Boi"):
        self.maxHealth = health
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.chance = chance
        self.name = name
    def checkStun(self):
        for effect in self.effects:
            if isinstance(effect, effects.stunned):
                effect.apply()

    def tickEffects(self):
        self.turn += 1
        i = 0
        while i < len(self.effects):
            if self.effects[i].duration == 0:
                self.effects[i].remove()
                self.effects.remove(self.effects[i])
            else:
                self.effects[i].apply()
                self.effects[i].duration -= 1
                i += 1
        # for i in range(len(self.effects)):
        #     if i >= len(self.effects):
        #         break
        #     if self.effects[i].duration == 0:
        #         self.effects[i].remove()
        #         self.effects.remove(self.effects[i])
        #         i -= 1
        #     else:
        #         self.effects[i].apply()
        #         self.effects[i].duration -= 1
        # for effect in self.effects:
        #     if effect.duration == 0:
        #       effect.remove()
        #       self.effects.remove(effect)
        #     else:
        #         effect.apply()
        #         effect.duration -= 1

    def getAttack1(self):
        return self.attack1(self)

    def getAttack2(self):
        return self.attack2(self)

    class attack1:
        pass

    class attack2:
        pass

    class attack3:
        pass

    class attack4:
        pass

    def decideMove(self):
        return random.choice([self.attack1(), self.attack2()])
