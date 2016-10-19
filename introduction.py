from player import *
from name import *

def pick_player_class():
    player_class = input("I want to be a: ").strip().lower()
    print()
    if player_class in ["warrior","a warrior"]:
        player_inventory.append("Sword of Azeroth")
        player_inventory.append("Light Armor")
        player_stats["health"]=150
        player_stats["max_health"]=150
        player_stats["class"]="warrior"
        player_stats["rage"]=0
        player_stats["max_rage"]=10
        player_stats["evasion"]=10
        player_stats["level"]=0
        player_stats_show()
    elif player_class in ["mage","a mage"]:
        player_inventory.append("Magic Staff of Varda")
        player_inventory.append("Robe of Valinor")
        player_stats["health"]=100
        player_stats["max_health"]=100
        player_stats["class"]="mage"
        player_stats["mana"]=50
        player_stats["max_mana"]=50
        player_stats["evasion"]=10
        player_stats["level"]=0
        player_stats_show()
    elif player_class in ["rogue", "a rogue"]:
        player_inventory.append("Bow of the Galadhrim")
        player_inventory.append("Ranger Cloak")
        player_stats["health"]=100
        player_stats["max_health"]=100
        player_stats["class"]="rogue"
        player_stats["mana"]=15
        player_stats["max_mana"]=15
        player_stats["evasion"]=40
        player_stats["arrows"]=2
        player_stats["level"]=0
        player_stats_show()
    elif player_class == "game master":
        player_input =input("? ")
        if player_input == "Gandalf":
            print("Welcome, Game Master")
            player_inventory.append("Grond the Hammer of the Underworld")
            player_inventory.append("Black Armor of Morgoth")
            player_stats_show()
        else:
            print("That's what I thought.")
            pick_player_class()
    else:
        print("Sorry, what?")
        pick_player_class()
def player_stats_show():
    print("You are now a", str(player_stats["class"]) + ".")
    print("Your name is", str(player_stats["name"]) + ".")
    print("You are level", str(player_stats["level"]) + ".")
    print("You have",player_stats["health"],"/",player_stats["max_health"],"health.")
    print("You have",player_stats["experience"],"experience points.")
    if player_stats["class"] == "rogue":
        print("You have",player_stats["arrows"],"arrows remaining.")
    elif player_stats["class"] == "mage":
        print("You have",player_stats["mana"],"/",player_stats["max_mana"],"mana.")
    elif player_stats["class"] == "warrior":
        print("You have",player_stats["rage"],"/",player_stats["max_rage"],"rage.")
    else:
        pass
    print("You have", ', '.join(player_inventory) + ".")
    print()

def player_ready():

    player_input = input("You are about to enter a world of adventure. Are you ready, brave adventurer? ").strip().lower()
    print()
    if player_input == "yes":
        print("Well then, onwards. --- INITIATING ADVENTURE ---")
    elif player_input == "no":
        print("Hahaha, cute. You thought you had a choice. Anyways: --- INITIATING AVENTURE ---")
    else:
        print("Sorry, what?")
        player_ready()

intro_screen()
print()
input("                                  --- PRESS ANY KEY TO START ---")
print()

print("Welcome to Group 20's text adventure. This is a test of skill, wit and strength through the land of Zorg. You are a young adventurer and have just \narrived in this country; you have nothing but your courage and brains and will to battle monsters, rescue citizens in distress and oppose all evil. \nBut be weary, for evil breeds evil and deeds unworthy of heroes will be punished.")
print()
print("Before we start, what's your name, mighty hero?")
player_stats["name"] = input("My name is: ").strip()
print()

print(player_stats["name"] + "? That is a name filled with promise of heroic deeds.")
print()
print("You can pick one of the three classes available. There are:")
print("NAME                 |    WARRIOR              |    MAGE                |   ROGUE")
print("Speciality           |    Increased Health     |    Increased Mana      |   Evasion")
print("Weapon               |    Sword                |    Staff               |   Dagger")
print("Secondary Weapon     |    Shield               |    Magic               |   Bow")
print("Ability              |    Damage Boost         |    Self-Heal, Fireball,|   Ranged Attack")
print("                     |                         |    Freeze Spells       |                    ")
print("Fuel for Abilities   |    Rage (dealing and    |    Mana (potions and   |   Arrows (looting and")
print("                     |    taking damage)       |    leveling up)        |   buying at shop)")
print()


pick_player_class()
player_ready()
print()
print("=== TOWN ===")
print("The Town is embellished with cobbled and paved streets, there are also a number of natural baths. There are Victorian townhouses and a mixture of \nsemi-detached and detached houses. A shop is located to the NORTH, the Plains of Lithlad to the EAST and a tavern to the SOUTH. \nWhat would you like to do?")
print("You can:")
print("SHOW INVENTORY")
print("SHOW STATS")
print("GO SOUTH to THE PRANCING PONY TAVERN.")
print("GO NORTH to STELLA'S SHOP.")
