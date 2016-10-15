from introduction import player_stats
from random import randint
current_enemy={"name":"Golbin","health":25,"damage_min":5,"damage_max":11}

def print_menu_battle():
    if player_stats["class"] == "mage":
        print("HEAL yourself.")
        print("CAST a spell at the enemy")
    elif player_stats["class"] == "warrior":
        print("USE Blade Fury.")
        print("PROTECT yourself with your shield.")
    elif player_stats["class"] == "rogue":
        print("pew pew")
    elif player_stats["class"] == "Dark Lord of Dorath":
        print("BLOW UP the enemy.")
        print("BRING DOWN a rain of meteors on the land")
    else:
        print("ERROR")


def damage_deal():
    if player_stats["class"] == "mage":
        return randint(5,10)
    elif player_stats["class"] == "warrior":
        return randint(8,14)
    elif player_stats["class"] == "rogue":
        return randint(3,15)
    elif player_stats["class"] == "Dark Lord of Dorath":
        return randint(25,35)
    else:
        print("ERROR")


def fight_enemy_goblin():
    print("You have", player_stats["health"],"health points remaining.")
    print("The Golbin has",current_enemy["health"],"health points remaning.")
    print("You can:")
    print("DEAL DAMAGE to the enemy.")
    print_menu_battle()
    print("SHOW your stats.")
    if player_stats["class"]== "rogue":
        current_enemy["health"]= current_enemy["health"] - 5
    player_input = input("What would you like to do?").strip().lower()
    if player_input == "deal damage":
        damage_dealt = damage_deal()
        current_enemy["health"] = current_enemy["health"] - damage_dealt
        print(damage_dealt)
        if current_enemy["health"] <= 0:
            print("Well done, you defeated the Golbin.")
            player_stats["experience"]= player_stats["experience"] + 50
        else:
            goblin_counter()
            fight_enemy_goblin()
        

player_input = input("What enemy? ")
if player_input == "goblin":
    print("You have encountered a Golbin. You must battle him or die trying.")
    fight_enemy_goblin()
else:
    print("Sorry, what?")
