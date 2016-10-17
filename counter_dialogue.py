from player import *

def counter_dialogue():
	print("You're at the counter of the Prancing Pony Tavern. 'Can I get you a drink?' the barkeeper asks. 'It'll cost you 2 copper.'")
	print()

	while True:
		print("You can:")
		print("BUY a drink to fully restore your health and mana")
		print("DECLINE the offer and leave the counter")

		player_input = input(">").strip().lower()

		if player_input == "buy":
			# restore the player's health and mana if they have enough money
			# otherwise, print error message

			if player_stats["money"] >= 2:
				# only charge the player if their health OR mana is depleted
				# otherwise, print error message

				if player_stats["health"] < player_stats["max_health"] or player_stats["mana"] < player_stats["max_mana"]:
					player_stats["money"] = player_stats["money"] - 2

					player_stats["health"] = player_stats["max_health"]
					player_stats["mana"] = player_stats["max_mana"]

					print("You pay 2 copper for a drink. Your health and mana have been fully restored!")
					print()

				else:
					print("'You already have full health and mana! Maybe you should lay off the drink.'")
					print()

			else:
				print("'You don't have enough copper! Come back once you have more.'")
				print()

			break

		elif player_input == "decline":
			# decline the offer

			print("You politely decline a drink.")
			print()
		
			break

		else:
			# print error message

			print("'Sorry, what was that?'")
			print()

	# return to the Prancing Pony Tavern