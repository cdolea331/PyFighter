from time import sleep
from fighters import *
from effect import effect
from effects import *
import colorama


def fight(fighter1, fighter2):
    turns = 0
    while fighter1.health > 0 and fighter2.health > 0:
        # if fighter1.speed >= fighter2.speed:
        #     print(colorama.Fore.BLUE)
        #     fighter1, fighter2 = takeTurn(fighter1, fighter2)
        #     sleep(2)
        #     print(colorama.Fore.RED)
        #     fighter2, fighter1 = takeTurn(fighter2, fighter1)
        #     sleep(2)
        #     turns+=1
        # else:
        print(colorama.Fore.RED)
        print(fighter2.attack)
        print(fighter2.effects)
        fighter2, fighter1 = takeTurn(fighter2, fighter1)
        # sleep(2)
        print()
        print(colorama.Fore.BLUE)
        fighter1, fighter2 = takeTurn(fighter1, fighter2)
        # sleep(2)
        turns += 1

        showStats(fighter1, fighter2)
        # sleep(1.5)

        # print("fighter1 hp: " + str(fighter1.health) + " defense:" + str(fighter1.defense)  +
        #       "\nfighter2 hp: " + str(fighter2.health) + " defense:" + str(fighter2.defense)  + "\n--------------\n\n\n")
        # sleep(3)
    print(colorama.Fore.RED + colorama.Back.YELLOW)
    if fighter1.health < 0 and fighter2.health < 0:
        print("Draw!")
        return turns, 2
    elif fighter1.health <= 0:
        print(colorama.Fore.RED + colorama.Back.YELLOW)
        print(fighter2.className + " " + fighter2.name + " wins!")
        return turns, 2
    else:
        print(colorama.Fore.BLUE + colorama.Back.YELLOW)
        print(fighter1.className + " " + fighter1.name + " wins!")
        return turns, 1


def takeTurn(fighter, opponent):
    fighter.tickEffects()
    if not fighter.stunned:
        move = fighter.decideMove(opponent)
        fighter, opponent = move.effect(fighter, opponent)
    else:
        print(fighter.className + " " + fighter.name + " is stunned!")
    print("\n")
    return fighter, opponent

def showStats(fighter1, fighter2):
    print(colorama.Back.WHITE)
    pips1 = int(fighter1.health//5)
    pips2 = int(fighter2.health//5)
    fighter1HP = 'I' * pips1
    fighter2HP = 'I' * pips2
    print(colorama.Fore.RED + colorama.Back.BLACK)
    fighter1HP = fighter1HP.ljust(int(fighter1.maxHealth//5)) #
    print(colorama.Fore.BLUE + colorama.Back.BLACK)
    fighter2HP = fighter2HP.ljust(int(fighter2.maxHealth//5))


    print(fighter1.className + "    " + fighter1.name +
          "\n Health:  [" + fighter1HP + ']' + ' ' + str(fighter1.health) + '/' + str(fighter1.maxHealth))

    print(fighter2.className + "    " + fighter2.name +
          "\n Health:  [" + fighter2HP + ']' + ' ' + str(fighter2.health) + '/' + str(fighter2.maxHealth))
    print("\n\n\n")
    # print(colorama.Back.BLACK)

combatant1 = healer()
combatant2 = healer2()
# # fight()
# combatant2.effects.append(poisoned(combatant2, combatant2, 4, 6))
# combatant2.effects.append(healOverTime(combatant2, combatant2, 4, 6))
# combatant2.effects.append(stunned(combatant2, combatant2, 4))

#
# print(combatant2.effects)
# for effect in combatant2.effects:
#     print(type(effect))
#     if isinstance(effect, poisoned):
#         print(effect.duration)
#         print(effect.damage)
#         print("he's poisoned")
# fight(combatant1, combatant2)
# warFighter.health -= 50

amount = 0
p1Wins = 0
p2Wins = 0
for i in range(1000):
    combatant1 = warrior(name="Alan")
    combatant2 = warrior2(name="Adrian")
    results = fight(combatant1, combatant2)
    amount += results[0]
    if results[1] == 1:
        p1Wins += 1
    else:
        p2Wins += 1



print(amount/1000)
print("Alan: " + str(p1Wins) + " Adrian: " + str(p2Wins))

#
# print(myFighter.attack)
# while len(myFighter.effects) > 0:
#     # print(len(myFighter.effects))
#     print(myFighter.health)
#     print("duration: " + str(myFighter.effects[0].duration))
#     myFighter.tickEffects()
# print(myFighter.health)

