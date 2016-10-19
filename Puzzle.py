from player import *
from test_combat import *
my_Puzzle = " drop golden coin"

def negative_ending():
    print("TAKE the gem.")
    print("DESTROY the gem.")
    player_input = input(">").strip().lower()
    if player_input == "take":
        print("You take the gem and it's power surges through you. You see the entire world and learn of all it's secrets in an instant. Nothing can stop you know, the world is at your mercy. Or is it...")
        #start adventure again with intro2
    elif player_input == "destroy":
        print("You brandish your sword and strike at the gem. Your sword shatters upon it and one of the projectiles wounds you. You decide to smash the gem with your bear hands but the moment you cease the gem, it tries to take control of you. For what seems an eternity you fight for your survival but in the end the weigh of all the evil you have caused crushes you and you become a mindless puppet of this evil force. Hopefully one will arise to stop you...")
    else:
        print("Sorry, what?")
        negative_ending()

def postive_ending():
    print("LEAVE the gem.")
    print("DESTROY the gem.")
    player_input = input(">").strip().lower()
    if player_input == "leave":
        print("You leave the gem behind, uninterested by the promise of fake power it offers. As you exit the castle you can hear a terrible scream of agony as it crumbles behind you. You return to the village victorious and are greeted by a great banquet in your honour. Remeber today, for today life is good.")
    if player_input == "destroy":
       print("You brandish your sword and strike at the gem. Your sword shatters upon it and one of the projectiles wounds you. You decide to smash the gem with your bear hands but the moment you cease the gem, it tries to take control of you. For what seems an eternity you fight for your survival and, helped by the prayers of those you have helped along the way to emerge victorious, dispelling the magic in a ray of dark magic that lights the sky. As you leave the palace you see the people of the town running towards the temple, eager to see if you are okay. They arrive just in time to catch you as you collapse from exhaustion. Later you awaken and are invited to a great banquet prepared in your honour. Remember today, for today life is good.") 

    else:
        print("Sorry, what?")
        postive_ending()

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
    if (karmaCounter >= -1) and (karmaCounter <= 1):
      print("You have finally slained the evil Dark Lord, well played. His body lies in front of you, lifeless and yet still menacing. You exit the castle but do not have the courage to return to the town, the things you have done to achieve this victory leave a bitter taste in your mouth. You prefer to wrap your cape around you and leave into the sunset.")
    elif karmaCounter > 1:
      print("You have finally slained the evil Dark Lord, well played. His body lies in front of you, lifeless and yet still menacing. You turn around, ready to leave and enjoy the peace. As you begin to walk away so suddenly hear a sound, like a rasping voice, whispering to you.\"Shre nazg golugranu kilmi nudur, Ombi Kuzddurbagu gundum-ishi bagu. (Where are you going warrior? Your reward already lays here.\" As you turn around you see that a gem has risen out of the lifeless body of the Dark Lord. What would you like to do?")
      postive_ending()
    elif karmaCounter < -1:
      print("You have finally slained the evil Dark Lord, well played. His body lies in front of you, lifeless and yet still menacing. You turn around, ready to leave and enjoy your just reward for saving those miserable people. As you begin to walk away so suddenly hear a sound, like a rasping voice, whispering to you.\"Shre nazg golugranu kilmi nudur, Ombi Kuzddurbagu gundum-ishi bagu. (Where are you going warrior? Your reward already lays here.\" As you turn around you see that a gem has risen out of the lifeless body of the Dark Lord. A gem of immense power, the power to rule over this land. Why not take it? After all you'e earned it. What would you like to do?")
      negative_ending()
    else:
      print("How the hell did you manage to break my beautiful karma counter? Just whatever; you win, youpih. Cue the fireworks.")

  elif player_input == "join":
    print("You approach and pledge your alleagance to the the Dark Lord but as you stand back up he stabs you in the heart and sends your dying body across the room. ")
    print("EVIL BOSS:You should have known I would betray you, after all I am evil.")
    player_defeat()

def puzzle():
    player_input=input(">").strip().lower()
    if player_input == "drop golden coin":
       print("You threw a piece of gold into the ritual circle, the ground shook and the magic barrier disappeared. A couple of apparition came to investigate")
       player_inventory.remove('a golden coin') 
       set_foe('apparition_1', 'guardian',0,0,0)
       playerstat_update()
       fight()
       print("You defeat the two apparitions, as they disappear into nothingness you hear a great voice inviting you upstairs")
       boss_fight()
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
