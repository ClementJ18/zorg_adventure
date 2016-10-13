player_inventory=[]
player_stats={"name":"Zorg", "class":"witch-lord of Dorath", "health":500, "mana":200, "experience":0, "level":20, "money":0, "evasion":70}

def pick_player_class():
    player_class = input("I want to be a: ").strip().lower()
    if player_class == "warrior":
        player_inventory.append("Sword of Azeroth")
        player_inventory.append("Light Armor")
        player_stats["health"]=150
        player_stats["class"]="warrior"
        player_stats["mana"]=15
        player_stats["evasion"]=10
    elif player_class == "mage":
        player_inventory.append("Magic Staff of Varda")
        player_inventory.append("Robe of Valinor")
        player_stats["health"]=100
        player_stats["class"]="mage"
        player_stats["mana"]=50
        player_stats["evasion"]=10
    elif player_class == "rogue":
        player_inventory.append("Bow of the Galadhrim")
        player_inventory.append("Ranger Cloak")
        player_stats["health"]=100
        player_stats["class"]="rogue"
        player_stats["mana"]=15
        player_stats["evasion"]=40
    else:
        print("Sorry, what?")
        pick_player_class()

def player_ready():
    player_input = input("Are you ready, brave warrior? You are about to enter a world of adventure. ").strip().lower()
    if player_input == "yes":
        #move to town
        pass
    elif player_input == "no":
        #what would you like to do?
        pass
    else:
        player_ready()

print("Welcome to Group 20's text adventure. This is a test of skill, wit and strenght through the land of country_name. You are  young adventurer and have just arrived in this country, you have nothing but your courage and brains and will have to battle monsters, rescue citizens in distress and oppose all evil. But be weary, for evil breeds evil and deeds unworthy of heroes will be punished.")
print("Before we start, what's your name mighty hero?")
player_stats["name"] = input("My name is: ").strip()

print(player_stats["name"],"? That is a name filled with promise of heroic deeds.")
print("You can pick one of the three classes available. There is:")
print("NAME                     WARRIOR                  MAGE                  ROGUE")
print("Specificity              Increased Health         Increased Mana        Evasion")
print("Weapon                   Sword                    Staff                 Dagger")
print("Secondary Weapon         Shield                   Magic                 Bow")
print("Ability                  Damage Boost             Self-Heal             Ranged Attack")
print("Fuel for Abilities       Rage (dealing and        Mana (potions and     Arrows (looting and")
print("                         taking damage)           leveling up           buying at shop")
print()


pick_player_class()
print("You are now a", player_stats["class"],".")
print("Your name is",player_stats["name"])
print("You are level", player_stats["level"])
print("You have",player_stats["health"],"health points remaining.")
print("You have",player_stats["mana"],"mana points remaining.")
print("You have",player_stats["experience"],"experience points.")
print("You have", ', '.join(player_inventory))
player_ready()

