from effect import effect

class stunned(effect):

    def __init__(self, sourcePlayer, targetPlayer, duration):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.message = targetPlayer.className + " " + targetPlayer.name + " has been stunned!"

    def apply(self):
        if not self.targetPlayer.stunned:
            self.targetPlayer.stunned = True

    def remove(self):
        self.targetPlayer.stunned = False


class poisoned(effect):

    def __init__(self, sourcePlayer, targetPlayer, duration, damage):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.damage = damage
        self.message = targetPlayer.className + " " + targetPlayer.name + " has been poisoned!"

    def apply(self):
        self.targetPlayer.health = self.targetPlayer.health - self.damage
        print(self.targetPlayer.className + " " + self.targetPlayer.name + " took " + str(self.damage) + " poison damage!")

class healOverTime(effect):

    def __init__(self, sourcePlayer, targetPlayer, duration, damage):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.damage = damage
        self.message = targetPlayer.className + " " + targetPlayer.name + " started healing!"

    def apply(self):
        self.targetPlayer.health = min(self.targetPlayer.health + self.damage, self.targetPlayer.maxHealth)
        print(self.targetPlayer.className + " " + self.targetPlayer.name + " healed for " + str(
            self.damage) + " health!")


class weaken(effect):

    def __init__(self, sourcePlayer, targetPlayer, duration, amount):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.amount = amount
        self.originalAttack = targetPlayer.attack
        self.message = targetPlayer.className + " " + targetPlayer.name + " had their attack reduced!"

    def apply(self):
        if not self.applied:
            self.applied = True
            self.targetPlayer.attack = self.originalAttack - self.amount

    def remove(self):
        self.targetPlayer.attack = self.originalAttack


class strengthen(effect):

    def __init__(self, sourcePlayer, targetPlayer, duration, amount):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.amount = amount
        self.originalAttack = targetPlayer.attack
        self.message = targetPlayer.className + " " + targetPlayer.name + " had their attack increased!"

    def apply(self):

        if not self.applied:
            self.applied = True
            self.targetPlayer.attack = self.originalAttack + self.amount

    def remove(self):
        self.targetPlayer.attack = self.targetPlayer.attack - self.amount
        print(self.targetPlayer.attack)


class harden(effect):

    def __init__(self, sourcePlayer, targetPlayer, duration, amount):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.amount = amount
        self.originalDefense = targetPlayer.defense
        self.message = targetPlayer.className + " " + targetPlayer.name + " had their defense increased!"

    def apply(self):
        if not self.applied:
            self.applied = True
            self.targetPlayer.defense = self.originalDefense + self.amount

    def remove(self):
        self.targetPlayer.defense = self.originalDefense

class soften(effect):

    def __init__(self, sourcePlayer, targetPlayer, duration, amount):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.amount = amount
        self.originalDefense = targetPlayer.defense
        self.message = targetPlayer.className + " " + targetPlayer.name + " had their defense reduced!"

    def apply(self):
        if not self.applied:
            self.applied = True
            self.targetPlayer.defense = self.originalDefense - self.amount

    def remove(self):
        self.targetPlayer.defense = self.originalDefense




