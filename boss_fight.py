from player import *
from player_defeat import *

print("EVIL BOSS: Hello,",player_stats["name"]+". I have been expecting you. ")
print("YOU: Cliché much?")
print("EVIL BOSS: Perhaps. Now I will give you a choice, JOIN me or die trying to FIGHT. The choice is yours, do you perefer to rule by my side the world of Zorg or die alone in the darkness?")
player_input = input(">").lower().strip()

if player_input == "fight":
	print("YOU: THE LIGHT SHALL TRIUMPH! You cannot corrupt me servant of Chaos, I will vanquish you.")
	print("EVIL BOSS: And I'm the cliché one? SO BE IT, DIE!!")
	#fight
elif player_input == "join":
	print("You approach and pledge your alleagance to the the Dark Lord but as you stand back up he stabs you in the heart and sends your dying body across the room. ")
	print("EVIL BOSS:You should have known I would betray you, after all I am evil.")
	player_defeat()