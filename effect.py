import fighter
class effect:

    applied = False
    def __init__(self, sourcePlayer, targetPlayer, duration, message):
        self.duration = duration
        self.sourcePlayer = sourcePlayer
        self.targetPlayer = targetPlayer
        self.message = "Effect applied"


    def apply(self):
        pass



    def remove(self):
        pass


