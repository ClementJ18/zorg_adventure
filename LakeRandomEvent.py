from player import *

def player_choice2():
    global karmaCounter
    player_input = input(">").strip().lower()
    if player_input == "kill":
        print(" You have successfully killed the creature and retrieved the item. It's the Coin of Glück. This item did come with a cost, you lose a bit of health as the dead creature secreted some mild poison.")
        player_stats["health"] = player_stats["health"] - 5
        player_inventory.append("Coin of Glück")
        karmaCounter = karmaCounter + 1
        #Return to Lake
    elif player_input == "take":
        print("You've managed to take the item, its the Coin of Pech, but at a cost. The creature attacked you when you tried taking it and you have lost some health")   
        player_stats["health"] = player_stats["health"] - 10
        player_inventory.append("Coin of Pesh")
        karmaCounter = karmaCounter - 1
        #Return to Lake
    elif player_input == "do nothing":
        #Return to Lake
    else:
        print("Sorry, what?")
        player_choice2()


print("===The Ancient Lake===")
print("You investigate the source of the light and notice an item in the lake. You are not sure what it could be. However, there appears to be an amphibious creature of some sort resting peacefully beside it.")
print()
print("You can:")
print(">KILL the creature and take the item.")
print(">TAKE the item without killing the creature.")
print(">Do Nothing.")
player_choice2()
print(player_inventory)
print(player_stats)
