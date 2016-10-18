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
        print(player_stats["forestCounter"])
        if player_input == "agree":
            player_stats["forestCounter"] = 1
            print("thankyou plz bring me water")
            print(player_stats["forestCounter"])
            break
            # transport player back to Eryn Vanwë

        elif player_input == "refuse":
                        
            karmaCounter = karmaCounter - 1
            player_stats["forestCounter"] = 2
            print("You turn your back on the old man and start to walk away. 'Please,' he wheezes, but you are already out of sight.")
            print(player_stats["forestCounter"])
            # transport player back to Eryn Vanwë

            break

        else:
            print("Sorry, what?")

def re_forest_encounter_2():
    global karmaCounter
    print(player_stats["forestCounter"])
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

            print("The old man opens his eyes and sees the pail of water. You lift it to his lips and gently tip some of its contents into\nhis mouth. \'Bless you, my boy,\' he whispers. 'Here, take these…' He slowly reaches into his pocket and retrieves 5\ncopper coins. You place the pail beside him, take the coins and give him directions before returning to the trail.")
            print()

            # transport the player back to Eryn Vanwë
            player_stats["forestCounter"] = 2
            break
        elif player_input == "pour":
            player_inventory.remove("pail")
            print("Why would you goes through the trouble of bringing me the water just to pour it down !?")
            karmaCounter = karmaCounter - 3
            print("You took the money off the old")
            player_stats["money"] = player_stats["money"] + 15
            player_stats["forestCounter"] = 2
            break

        else:
            print("Sorry, what?")

"""

    if forestCounter == 1:
        print("You see a well. An empty metal bucket sits beside it.")

        print("FILL the bucket")

    if player_input == "FILL" and forestCounter == 1:

        player_inventory.append("pail")

    # print available exits (and farm description?) again


"""