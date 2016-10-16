from player import *

questCounter = 1
def player_quest1_menu():
    global questCounter
    player_input=input(">").strip().lower()
    if player_input == "go east":
        #return east
        pass
    elif player_input == "talk":
        #begin quest 1
        questCounter = questCounter +1
        print("Welcome",player_stats["name"])
    elif player_input == "steal":
        #insta-defeat
        print("\"YOU FOOL!\" Yells the old man, \"You are not worthy of being a hero, die now and curse in vain!\" And with that he melts the flesh off your bones and sends you to meet your maker.")
        
    else:
        print("Sorry, what?")
        player_quest1_menu()


print("===DARK TAVERN CORNER===")
print()
print("You stand in front of the table where the hooded figures is looking upon an ancient book. He doesn\'t seem to have noticed you. What would you like to do?")
print("You can:")
print("GO EAST back to the center of the tavern.")
print("TALK to the hooded man.")
print("STEAL the book which looks like it could bring you power and fame beyond anything you can imagine.")
player_quest1_menu()