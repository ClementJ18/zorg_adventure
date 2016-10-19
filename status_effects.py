import random
from player import *
from test_combat import *

# poison reduces health by 1% of max health each turn

def poisoning(poison_active):
    print(poison_active)
    if subjects['player']['poison_active'] == False:
        if random.randint(0, 9) <= 7:
            subjects['player']['poison_active'] = True
            print('poison activated')
    


def poison_damage(poison_active):
    print(subjects['player']['poison_active'])
    if subjects['player']['poison_active'] == True:
        poison_damage = int(0.01 * player_stats["max_health"])
        subjects['player']["hp"] = subjects['player']["hp"] - poison_damage
        print("You have taken " + str(poison_damage) + " damage due to poisoning!")
