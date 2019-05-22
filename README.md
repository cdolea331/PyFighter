# PyFighter
Text-based, turn-based fighter.

To test your code simply replace the code in combatant1AI with your decideMove function(don't rename it/change the function heading), change combatant 1's type to whatever class you are using and run fight.py to see the result of 1000 rounds with combatant 2. To test two AI against each other, paste the second AI into combatant2AI and change the class of combatant 2.


This code will be used for the PyFighter Big Brain AI tournament. 

Players will develop AI for at least 1 class, and player's AI will be pitted against each other in a tournament until one person is the winner. 

The winner will recieve 20$ and the official title of "Big Brain"

It is highly recommended you develop more than 1 AI, both because changes may be made if absolutely necessary during the tournament, and for strategic diversity.

Changes/Patch notes will be update here

Secifications: 

You may not change any of your or your opponent's fields (variables/attributes), methods or other charactaristics. Yourcode should only looks at these variables to return an instance of the class who's attack you wish to use.


Upcoming Changes:
-Healer purify will be reworked:

Purify
-Sacrifice 10 hp, remove all effects from enemy and deal 3 * the number of effects removed in damage.


v1.1:

New class: Juggernaut
Stats-- HP:150 Att: 5 Def: 8

Attack 1: Shield bash

Damage: 1 * attack + 0.25 * defense

Effect: 15% chance to stun



Attack 2: Bulwark

Effect: Raise defense by 5 for 4 turns. 20% chance to raise by 10 instead of 5.



Attack 3: Bone Breaker

Damage: 1 * attack

Effect: Lower enemy attack by 2/3/4 if the opponent has 0-10/11-19/20+ attack



Attack 4: The Fury

Damage: 0.75 * defense

Damage(enraged): 1.15 * attack

Effect: Current defense is added to attack and defense is reduced to 0 for 3 turns. If The Fury is cast again during this time, it becomes an attack-based damaging attack.




All classes
-All classes now have a damage range of 0.8 - 1.2 * normal damage value


Assassin
-Assassin backstab now does 1 * attack damage

Warrior
-Warrior roar bug fixed
-Pommel strike can now stun from 1-2 turns
-Wild swing damage range changed to 0.6 - 1.5

Healer
-healing hand buffed from 4 health for 4 turns to 5 health for 5 turns (total 16 -> 20)

