from player import *
def shop():
        def shop_input():
        	if player_stats["class"] == "rogue":
        		print("You can:")
        		print("BUY a health potion for 15 coins or an arrow for 5 coins.")
        		print("GO SOUTH to the town")
        	if player_stats["class"] == "warrior":
        		print("You can:")
        		print("BUY a health potion for 15 coins.")
                        print("GO SOUTH to the town")
                if player_stats["class"] == "mage":
                        print("You can:")
                        print("BUY a health potion for 15 coins or a mana potion for 25 coins.")
                        print("GO SOUTH to the town")
                else:
                        pass
                player_input = input(">").lower().strip()
                if player_input in ["arrow", "buy an arrow", "buy arrow", "an arrow"] and player_stats["class"] == "rogue" and player_stats["money"] >= 3:
                        player_stats["money"] = player_stats["money"] - 3
                        player_stats["arrows"] = player_stats["arrows"] + 1
                        print("Bought an arrow.")
                        print("Would you like to buy anything else?")
                        shop_input()
                elif player_input in ["mana", "mana potion", "buy mana potion", "a mana potion"] and player_stats["class"] == "mage" and player_stats["money"] >= 25:
                        player_stats["money"] = player_stats["money"] - 25
                        player_inventory.append("mana_potion")
                        print("Bought a mana potion")
                        print("Would you like to buy anything else?")
                        shop_input()
                elif player_input in ["health", "health potion", "buy health potion", "a health potion", "buy a health potion"] and player_stats["money"] >= 15:
                        player_stats["money"] = player_stats["money"] - 15
                        player_inventory.append("health_potion")
                        print("Bought a health potion")
                        print("Would you like to buy anything else?")
                        shop_input()
                elif player_input == "go south":
                        #return to town
                        pass
                else:
                        print("Either you don't have enough money or the command was not recognized.")
                        shop_input()

        print("=== STELLA\'S SHOP ===")
        print("As you enter the shop owner greets you: \"Welcome to my shop traveller, what can I do for you?\" You look around, on the shelves you can see many items for daily life and food. You can also see many phials of different color but only a couple items truly catch your eye.")

        shop_input()
