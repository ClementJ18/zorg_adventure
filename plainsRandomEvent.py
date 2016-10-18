from player import *

def plainsRandomEvent():
    def player_choice():
        global karmaCounter
        potion = "health_potion"
        player_input = input(">").strip().lower()
        if player_input == "give":
            if potion in player_inventory:
                player_inventory.remove("health_potion")
                print("The man thanks for for your help and gives you some money in return.")
                player_stats["money"] = player_stats["money"] + 75
                karmaCounter = karmaCounter + 1
            #return to plains 2
            else:
                print("You don't have any potions")
                player_choice()
            #return to plains 2
        elif player_input == "leave":
            pass
            
        #return to plains 2
        elif player_input == "attack":
            print("You kill the man and loot his box... You monster")
            print("You gain a health potion and 25 coins.")
            karmaCounter = karmaCounter - 1
            player_stats["money"]= player_stats["money"] +25
            player_inventory.append("health_potion")
            if player_stats["class"] == "rogue":
                player_stats["arrows"] = player_stats["arrows"] + 2
                print("You gained 2 arrows.")
        #return to plains 2
        else:
            print("Sorry, what?")
            player_choice()

    print("===PLAINS OF KARMA==")
    print("You see a caravan that has been attacked, around it lay many dead bodies both goblins and bodies of men. One man still lives, he is resting against a box, his sword lay by him and his back turned to you. You can see arrows, potions and money in the boxes.")
    print()
    print("You can:")
    print("GIVE the man a potion and bandage his wounds.")
    print("LEAVE the man be.")
    print("ATTACK the man and take the loot you see in the box.")
    player_choice()
