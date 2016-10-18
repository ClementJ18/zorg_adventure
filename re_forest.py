from player import *

def re_forest_encounter_1():
    global karmaCounter

    print("You come across an old man sat at the base of a tree. Noticing your presence, he slowly turns his head and looks up at you, \nbut his gaze appears unfocused. 'My boy,' he says. I've been lost in these woods for days and I'm parched. Won't you go to \nthe nearby farm and ask them for a pail of water? At this rate, I won't have the energy to make it home...'")
    print()
    while True:
        print("You can:")
        print("AGREE to help the old man")
        print("REFUSE to help the old man")
        player_input = input(">").strip().lower()
        print()
        
        if player_input == "agree":
            player_stats["forestCounter"] = 1
            print("'Make haste, my boy...'")
            
            break
            
        elif player_input == "refuse":
                        
            karmaCounter = karmaCounter - 1
            player_stats["forestCounter"] = 2
            print("You turn your back on the old man and start to walk away. 'Please,' he wheezes, but you are already out of sight.")

            break

        else:
            print("Sorry, what?")

def re_forest_encounter_2():
    global karmaCounter
    
    print("The old man leans against the tree with closed eyes, breathing weakly.")
    print()

    while True:
        print("You can:")
        print("OFFER the old man water")
        print("POUR the water on the ground")
        
        player_input = input(">").strip().lower()

        if player_input == "offer":
            player_inventory.remove("pail")

            karmaCounter = karmaCounter + 1
            player_stats["money"] = player_stats["money"] + 5

            print("The old man opens his eyes and sees the pail of water. You lift it to his lips and gently tip some of its contents into\nhis mouth. \'Bless you, my boy,\' he whispers. 'Here, take these...' He slowly reaches into his pocket and retrieves 5\ncopper coins. You place the pail beside him, take the coins and give him directions before returning to the trail.")
            print()

            player_stats["forestCounter"] = 2

            break
        elif player_input == "pour":
            player_inventory.remove("pail")

            print("'Why would you go through the trouble of bringing me water just to pour it away?!'")
            print("You rifle through the old man's pockets and find 5 copper.")

            karmaCounter = karmaCounter - 4
            player_stats["money"] = player_stats["money"] + 5
            player_stats["forestCounter"] = 2

            break

        else:
            print("Sorry, what?")