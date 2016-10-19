import random
from player import *

# poison reduces health by 1% of max health each turn

def poisoning(poison_active):
    if random.randint(0, 9) <= 7:
        poison_active = True
    elif poison_active = True:
        pass
    else:
        poison_active = False
    return poison_active


def poison_damage(poison_active):
    if poison_active == True:
        poison_damage = int(0.01 * player_stats["max_health"])
        player_stats["health"] = player_stats["health"] - poison_damage
        print("You have taken " + str(poison_damage) + " damage due to poisoning!")