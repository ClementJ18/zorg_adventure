from player import *

def level_up():
	global exp_before_next_level

	while player_stats["experience"] >= exp_before_next_level:
			
			player_stats["experience"] = player_stats["experience"] - exp_before_next_level
			
			player_stats["level"] = player_stats["level"] + 1
			
			player_stats["max_health"] = player_stats["max_health"] + 25
			player_stats["health"] = player_stats["health"] + 25
			player_stats["max_mana"] = player_stats["max_mana"] + 10
			player_stats["mana"] = player_stats["mana"] + 10
			
			exp_before_next_level = 2 * exp_before_next_level

			print("You have leveled up! You are now level " + str(player_stats["level"]) + ".")