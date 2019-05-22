from effect import Effect

class stunned(Effect):

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


class poisoned(Effect):

    def __init__(self, sourcePlayer, targetPlayer, duration, damage):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.amount = damage
        self.message = targetPlayer.className + " " + targetPlayer.name + " has been poisoned!"

    def apply(self):
        self.targetPlayer.health = self.targetPlayer.health - self.amount
        print(self.targetPlayer.className + " " + self.targetPlayer.name + " took " + str(self.amount) + " poison damage!")

class healOverTime(Effect):

    def __init__(self, sourcePlayer, targetPlayer, duration, damage):
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.duration = duration
        self.amount = damage
        self.message = targetPlayer.className + " " + targetPlayer.name + " started healing!"

    def apply(self):
        self.targetPlayer.health = min(self.targetPlayer.health + self.amount, self.targetPlayer.maxHealth)
        print(self.targetPlayer.className + " " + self.targetPlayer.name + " healed for " + str(
            self.amount) + " health!")


class weaken(Effect):

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
            self.targetPlayer.attack = self.targetPlayer.attack - self.amount

    def remove(self):
        self.targetPlayer.attack = self.targetPlayer.attack + self.amount


class strengthen(Effect):

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
            self.targetPlayer.attack = self.targetPlayer.attack + self.amount

    def remove(self):
        self.targetPlayer.attack = self.targetPlayer.attack - self.amount


class harden(Effect):

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
            self.targetPlayer.defense = self.targetPlayer.defense + self.amount

    def remove(self):
        self.targetPlayer.defense = self.targetPlayer.defense - self.amount

class soften(Effect):

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
            self.targetPlayer.defense = self.targetPlayer.defense - self.amount

    def remove(self):
        self.targetPlayer.defense = self.targetPlayer.defense + self.amount




