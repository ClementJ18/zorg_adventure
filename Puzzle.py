from player import *
from test_combat import *
my_Puzzle = " drop golden coin"
def puzzle():
    player_input=input(">").strip().lower()
    if player_input == "drop golden coin":
       print("You threw a piece of gold into the ritual circle, the ground shook and the magic barrier disappeared. A couple of apparition came to investigate") 
       set_foe('apparition_1', 'guardian',0,0,0)
       playerstat_update()
       fight()
       print("You defeat the two apparitions, as they disappear into nothingness you hear a great voice inviting you upstairs")
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
print("You notice that inside the ritual circle there is a stone tablet that says 'A GOLDEN CROWN, A GOLDEN TAIL, NO BODY,YOU MUST DROP THE ITEM TO UNLOCK THE DOOR")
print("")
print("You can:")
print("Investigate the ritual circle")
print("Investigate the magic barrier")
puzzle()
