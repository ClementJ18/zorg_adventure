from player import *
from player_defeat import *
from test_combat import *

def boss_fight():
	print("EVIL BOSS: Hello,",player_stats["name"]+". I have been expecting you. ")
	print("YOU: Cliché much?")
	print("EVIL BOSS: Perhaps. Now I will give you a choice, JOIN me or die trying to FIGHT. The choice is yours, do you perefer to rule by my side the world of Zorg or die alone in the darkness?")
	player_input = input(">").lower().strip()

	if player_input == "fight":
		print("YOU: THE LIGHT SHALL TRIUMPH! You cannot corrupt me servant of Chaos, I will vanquish you.")
		print("EVIL BOSS: And I'm the cliché one? SO BE IT, DIE!!")
		set_foe('unkillable_boss',0,0,0,0)
		playerstat_update()
		fight()
		print()
		print("You lay on the ground, bleeding from many injuries. Your weapon feels heavy in your hand, your clothes weigh you down. Despair is near, after all, why not give in, it would be much easier to give in, to just shut your eyes and let the darkness consume everything... Suddenly you can feel a light shining and the artifact floats out of your pocket and embeds itself in your sword. You hear a voice in your head \"Fight. Fight! FIGHT!\" You body is filled with renewed strength, you grab your weapon and strike the Dark Lord. The strike weakens him badly, and your strength is renewed once again. Now, the true battle may begin.")
		set_foe('final_boss',0,0,0,0)
		playerstat_update()
		fight()
		from ending import *

	elif player_input == "join":
		print("You approach and pledge your alleagance to the the Dark Lord but as you stand back up he stabs you in the heart and sends your dying body across the room. ")
		print("EVIL BOSS:You should have known I would betray you, after all I am evil.")
		player_defeat()