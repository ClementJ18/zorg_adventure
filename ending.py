from player import *

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