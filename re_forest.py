from player import *

def re_forest_encounter_1():
	print("""
	You come across an old man sat at the base of a tree. Noticing your presence, he slowly turns his head and looks up at you, \
	but his gaze appears unfocused. 'My boy,' he says. I've been lost in these woods for days and I'm parched. Won't you go to \
	the nearby farm and ask them for a pail of water? At this rate, I won't have the energy to make it home...'
	""")
	print()

	while True:
		print("You can:")
		print("AGREE to help the old man")
		print("REFUSE to help the old man")

		player_input = input(">").strip().lower()

		if player_input == "AGREE":
			sidequestCounter = 1

			# transport player back to Eryn Vanwë

		elif player_input == "DECLINE":
			karmaCounter = karmaCounter - 1

			print("You turn your back on the old man and start to walk away. 'Please,' he wheezes, but you are already out of sight.")

			# transport player back to Eryn Vanwë

			break

		else:
			print("Sorry, what?")

def re_forest_encounter_2():
	print("The old man leans against the tree with closed eyes, breathing weakly.")
	print()

	while True:
		print("You can:")
		if pail in player_inventory:
			print("OFFER the old man water")
		print("Go EAST to Eryn Vanwë")

		player_input = input(">").strip().lower()

		if player_input == "offer" and pail in player_inventory:
			player_inventory.remove(pail)

			karmaCounter = karmaCounter + 1
			player_stats["money"] = player_stats["money"] + 5

			print("""
			The old man opens his eyes and sees the pail of water. You lift it to his lips and gently tip some of its contents into \
			his mouth. 'Bless you, my boy,' he whispers. 'Here, take these…' He slowly reaches into his pocket and retrieves 5 \
			copper coins. You place the pail beside him, take the coins and give him directions before returning to the trail.
			""")
			print()

			# transport the player back to Eryn Vanwë

			break

		else:
			print("Sorry, what?")

"""

	if sidequestCounter == 1:
		print("You see a well. An empty metal bucket sits beside it.")

		print("FILL the bucket")

	if player_input == "FILL" and sidequestCounter == 1:

		player_inventory.append(pail)

	# print available exits (and farm description?) again


"""




