from player import *

# exp necessary to level up
exp_before_next_level = 50

def level_up():
	while player_stats["experience"] >= exp_before_next_level:
			# reset exp counter
			player_stats["experience"] = player_stats["experience"] - exp_before_next_level
			# level up the player
			player_stats["level"] = player_stats["level"] + 1
			# add health and mana
			player_stats["max_health"] = player_stats["max_health"] + 10
			player_stats["health"] = player_stats["health"] + 10
			player_stats["max_mana"] = player_stats["max_mana"] + 25
			player_stats["mana"] = player_stats["mana"] + 25
			# increase experience necessary to level up
			exp_before_next_level = 2 * exp_before_next_level