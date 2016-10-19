from player import *

my_Puzzle = " drop golden coin"
def puzzle():
    player_input=input(">").strip().lower()
    if player_input == "drop golden coin":
       print("You threw a piece of gold into the ritual circle, the ground shook and the magic barrier disappeared. A couple of goblins came to investiage") 
    elif player_input == "investigate ritual circle":
        print("There is a stone table in the middle of the ritual circle. The answer for the riddle on the tablet will break the barrier")
        puzzle()
    elif player_input == "investigate magic barrier":
        print ("There is nothing special about the barrier")
        puzzle()
    else:
        print("Sorry, what?")
        puzzle()


print("===Dark Castle Ritual Room===")
print("After entering the Dark Castle undetected you look around and notice that you are in a ritual room. The room is covered in rubble, broken pottery and moss. It is too dangerous to go back, to the EAST there is a granite door that will take you to the great hall but it's blocked by a powerful magic barrier")
print("")
print("You notice that inside the ritual circle there is a stone tablet that says 'A GOLDEN CROWN, A GOLDEN TAIL, NO BODY,YOU MUST DROP IT TO UNLOCK THE DOOR")
print("")
print("You can:")
print("Investigate the ritual circle")
print("Investigate the magic barrier")
print("  ____ ___   __ __   ___ ____  ______ __ __ ____    ___       ____  ____ ___ ___   ___ ")
print(" /    |   \ |  |  | /  _]    \|      |  |  |    \  /  _]     /    |/    |   |   | /  _]")
print("|  o  |    \|  |  |/  [_|  _  |      |  |  |  D  )/  [_     |   __|  o  | _   _ |/  [_ ")
print("|     |  D  |  |  |    _]  |  |_|  |_|  |  |    /|    _]    |  |  |     |  \_/  |    _]")
print("|  _  |     |  :  |   [_|  |  | |  | |  :  |    \|   [_     |  |_ |  _  |   |   |   [_ ")
print("|  |  |     |\   /|     |  |  | |  | |     |  .  \     |    |     |  |  |   |   |     |")
print("|__|__|_____| \_/ |_____|__|__| |__|  \__,_|__|\_|_____|    |___,_|__|__|___|___|_____|")
puzzle()
