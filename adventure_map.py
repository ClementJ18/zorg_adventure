from counter_dialogue import counter_dialogue
from player import *
from introduction import *
from LakeRandomEvent import lakeRandomEvent
from plainsRandomEvent import plainsRandomEvent
from gameparser import *
from re_forest import *
from player_defeat import player_defeat
from test_combat import *

x=1
y=2
oldloc='12'
command=0
newloc='12'
event = False
import random
a = 8

desc={'13':'A small sign hanging above a building made of bricks as opposed to wooden house besides it. \nOne can barely makes out the writing on the sign to read \"Stella\'s potion store\" \nInside there\'s a counter similar to a bar but instead of liquor on the shelf, \nit is filled with numerous bottles of coloured liquids. \n\nBehind the counter stood one girl... ',
     '11':'You are in the Prancing Pony Tavern. The atmosphere is what you\'d expect; loud, lively and with a sense of familiarity. You observe the area and see people drinking in one corner. In another area there are a couple of men who look as if they\'re about to fight. You see a picture of creature on the wall, it appears the townfolk want it dead as its eating their cattle. You see the barman south of you at the counter having a drink himself. You notice a dark corner west of you, where there is a hooded figure with his head down.  What would you like to do?',
     '12':'The Town is embellished with cobbled and paved streets, there are also a number of natural baths. There are a mixture of victorian townhouses and there are a mix of semi-detached and detached houses. The shop is located in the North, the Plains of Lithlad in the East and the Tavern in the South. What would you like to do?',
     '10':'You stand in front of the table where the hooded figures is looking upon an ancient book. He doesn’t seem to have noticed you. What would you like to do?',
     '01':'It\'s just an empty table that smells of beer.',
     '22':'You arrive upon a grassy plain, before you miles of grass can be seen waving in the mild breeze that gently flows eastward. The sun shines timidly bathing the plains in light and in the distance you can see a lake reflecting it. Behind you the town stands, a bit of black smoke rising it from it due to the recent goblin invasion. Further north you can see that the flat plain becomes slightly hilly. What would you like to do?',
     '23':'A grassy valley spreads out in front of you, bushes grow around the prominent rocks and small animals scurry all around the place. In the north you can see the valley rising and melding into mountains covered in forest with a farm at its base. Towards the east a terrible black gate blocks the way, patrolled by goblin archers and trolls. In the south the plains flatten down and becomes a vast land of grass. What would you like to do?',
     '21':'You arrive at the Ancient Lake. The lake is very beautiful in the sunlight, large and full of water\'s edge creatures. You can hear the sound of gushing water and presume it\'s the waterfall connected to the lake which is towards the east. The sound is quite odd however, as there is a strange echo. A glistening light catches your gaze, you notice something in the lake. Towards the north, you see luscious grass,  it can only be the Plains of Lithlad. What would you like to do?',
     '31':'The Cave is particularly large and has humid conditions. The water falls at a fast pace and the water is murky. At the end of the room you can see a magical pendant radiating with power and lighting the room with multicolored beams. As you approach an apparition appears in front of you, challenging to a fight. What would you like to do?',
     '24':'You arrive on a destroyed farm, it has been burnt to the ground and the stones that held the roof have been thrown down. Nothing but ruins remain, the lifeless bodies of the parents are nowhere in sight, either they fled or were devoured.',
     '14':'You are standing in the forest of Eryn Vanwë. Bars of light pierce the canopy of oak and beech, illuminating the glossy leaves of the shrubs below. The odours of damp earth and wild garlic mingle with the smell of the burning farm to the EAST. A dirt trail leads to the NORTH, deeper into the woods and towards a cluster of shabby huts and tents. What would you like to do?',
     '15':'You have found the goblin lair. The goblins\' primitive shelters are in poor shape, with rotting wooden frames covered in brightly-coloured fungi. Inside the huts, you see mouldy blankets, crude blackthorn cudgels, and the carcasses of the farmer\'s livestock. A blackened, unplucked chicken burns over a campfire. The forest trail leads SOUTH, out of the lair. What would you like to do?',
     }

world = {'01':{'type':'7','name':'DARK TAVERN CORNER','FD':['west','south','north'],'event':True},         
         '10':{'type':'4','name':'TAVERN COUNTER','FD':['east','south','west']},         
         '11':{'type':'1','name':'THE PRANCING PONY TAVERN','FD':['east']},
         '12':{'type':'1','name':'TOWN CENTER','FD':['west','east'],'desc':''},
         '13':{'type':'2','name':'STELLA\'S SHOP', 'FD':['east','north','west']},
         '00':{'type':'0','name':'Guard wall'},
         '02':{'type':'0','name':'Guard wall'},
         '03':{'type':'0','name':'Guard wall'},
         #------------------------town zone----------------------------------
         '21':{'type':'3','name':'THE ANCIENT LAKE','FD':['west','south','east'],'event':False},
         '22':{'type':'3','name':'PLAINS OF LITHLAD','FD':['east'],'desc':'','event':False},
         '23':{'type':'8','name':'MOORS OF THE NIBIN-NOEG','FD':['west', 'east'],'desc':''},
         '31':{'type':'6','name':'ARTIFACT CHAMBER','FD':['east','north','south']},
         '30':{'type':'0','name':''},
         '33':{'type':'9','name':'EVIL CASTLE'},
         #------------------------plains zone--------------------------------
         '24':{'type':'5','name':'RUINED FARM','FD':['east','north'],'event':True},
         '14':{'type':'3','name':'ERYN VANWË','FD':['south','west'],'event':False},
         '15':{'type':'3','name':'GOBLIN LAIR','FD':['west','east','north'],'event':True}
         #------------------------Goblin's territory-------------------------
         }
#type 0 objects dubbed 'wall' are inaccesible areas and will bounce player back to previous area
#type 1 objects are accesible areas
#type 2 objects are shop areas. Key 'inventory' refers to another list of items that store owns


shopkeeper = {'Stella':{'intro':'Welcome to Stella\'s potion store ! How may I help you \nI can get you a list of item in stock you could \'buy\' or can I help you with something\'else\'.',
                        'inventory':['health_potion','mana_potion','arrows']},
                        'else':'beep boop im a robot'
                       }
def compass(loc): #some form of debugging tool (maybe have this in the game as well ?)

    cx = int(loc[0])
    cy = int(loc[1])
    north = str(cx)+str(cy+1)
    south = str(cx)+str(cy-1)
    east = str(cx+1)+str(cy)
    west =str(cx-1)+str(cy)
    
    print("SHOW INVENTORY")
    print("SHOW STATS")

    if north in world and 'north' not in world[loc]['FD']:
        print('GO NORTH to',world[north]['name'])
    if south in world and 'south' not in world[loc]['FD']:#basically asking if the room in certain direction are EXISTS and accesible or not. 
        print('GO SOUTH to',world[south]['name'])
    if east in world and 'east' not in world[loc]['FD']:
        print('GO EAST to',world[east]['name'])
    if west in world and 'west' not in world[loc]['FD']:
        print('GO WEST to',world[west]['name'])

def shop():

    print("As you enter the shop owner greets you: \"Welcome to my shop traveller, what can I do for you?\" You look around, on the shelves you can see many items for daily life and food. You can also see many phials of different color but only a couple items truly catch your eye.")

    while True:
        if player_stats["class"] == "rogue":
            print("You can:")
            print("BUY a health potion for 15 coins or an arrow for 5 coins.")
            print("GO SOUTH to the town.")
        if player_stats["class"] == "warrior":
            print("You can:")
            print("BUY a health potion for 15 coins.")
            print("GO SOUTH to the town.")
        if player_stats["class"] == "mage":
            print("You can:")
            print("BUY a health potion for 15 coins or a mana potion for 25 coins.")
            print("GO SOUTH to the town.")
        else:
            pass
        player_input = input(">").lower().strip()
        if player_input in ["arrow", "buy an arrow", "buy arrow", "an arrow"] and player_stats["class"] == "rogue" and player_stats["money"] >= 3:
            player_stats["money"] = player_stats["money"] - 3
            player_stats["arrows"] = player_stats["arrows"] + 1
            print("Bought an arrow.")
            print("Would you like to buy anything else?")
        elif player_input in ["mana", "mana potion", "buy mana potion", "a mana potion"] and player_stats["class"] == "mage" and player_stats["money"] >= 25:
            player_stats["money"] = player_stats["money"] - 25
            player_inventory.append("mana_potion")
            print("Bought a mana potion")
            print("Would you like to buy anything else?")
        elif player_input in ["health", "health potion", "buy health potion", "a health potion", "buy a health potion"] and player_stats["money"] >= 15:
            player_stats["money"] = player_stats["money"] - 15
            player_inventory.append("health_potion")
            print("Bought a health potion")
            print("Would you like to buy anything else?")
        elif player_input == "go south":
            break
        else:
            print("Either you don't have enough money or the command was not recognized.")
            shop_input()

                                          
def event(loc):
    global plainCounter
    global lakeCounter
    global forestCounter
    global questCounter
    global a
    #This is literally a sample set of event to demonstrate how you can manipulates event triggers by having some action ( like accessing some place ) triggers the other event so it could happen when otherwise nothing will
    #Delete this shit later
    if loc == '22': #accessing plains after visiting the dark tavern corner will made the old man showed up
        if plainCounter == 0:
            plainsRandomEvent()
            plainCounter = 1
            print('=== THE PLAINS OF LITHLAD ===')
            print(desc['22'])
        else:
            pass
    
    elif loc == '21': #ancient lake trigger
        if lakeCounter == 0:
            lakeRandomEvent()
            lakeCounter = 1
        else:
            pass
    
    elif loc == '14':#EVENT 14 ==================================================================
        if player_stats["forestCounter"] == 0:
            re_forest_encounter_1()
            
        elif player_stats["forestCounter"] == 1:
            if "pail" in player_inventory:
                re_forest_encounter_2()
            else:
                print("The old man leans against the tree with closed eyes, breathing weakly. You should get him that water soon.")
        else:
            pass
    elif loc == '15' and questCounter == 3:
        print('you see 2 goblin')
        set_foe('goblin','hypergoblin',0,0,0)
        playerstat_update()
        fight()
        print('The goblin king is angered by your action and taunt you into a fight')
        playerstat_update()
        set_foe('goblin_king',0,0,0,0)
        fight()
        print('you raid his stash and find cool looking map about cool sutff in the lake')
        print('coooooooooooooooooooooooooooool')
        world['21']['FD'].remove('east')
        questCounter=4
        
    else:
        pass
    world[loc]['event'] = False #This kills the event trigger so that an event may only happen once unless made happen again.

        
while True:
    is_valid_command = False# set this to false
    if event == True:
        is_valid_command = True
        
    while is_valid_command == False:
        command=normalise_input(input('> '))#ask what direction
        is_valid_command = True
        if len(command) > 1:
            if command[0] == 'go' and command[1] in world[oldloc]['FD']:
                is_valid_command = False
                print('Sorry, you can\'t go that way.')         
            else:
                if command[1] == 'north':
                    y=int(y)+1
                elif command[1] == 'south':#change coordiante corresponding to the direction you are walking
                    y=int(y)-1
                elif command[1] == 'east':
                    x=int(x)+1
                elif command[1] == 'west':
                    x=int(x)-1
                elif command == ['where','am','i']:
                    print('at',world[str(x)+str(y)]['name'])
                    is_valid_command = False
                elif 'take' in command and x == 3 and y == 1 and questCounter == 4:
                    print("You take the artifact.")
                    player_inventory.append("artifact")
                    questCounter = 5
                else:
                    is_valid_command = False
                    print('invalid command')
        else:
            if command[0] == 'compass':
                compass(str(x)+str(y))
                is_valid_command = False
            elif command[0] == 'talk' and x == 0 and y == 1 and questCounter == 0:
                print("Before you even open your mouth, the hooded figure looks up. 'I have been waiting for you,' he says. 'And we have much to discuss. An Evil threatens this land, you must save it for it is the only things that still stands between it and the rest of the world, if this land were to fall evil would run afoul everywhere. Take this money and go prepare yourself for the many bettles to come, then you should make your way EAST of the town for many trials await you. As he finishes you can feel the world spin around you and you faint.")
                input("Press Enter to continue...")
                player_stats["money"] = 9999999
                questCounter = 1
                newloc = "01"
                x = 0
                y = 1
                world['12']['FD'].remove('east')
            elif command[0] == 'steal' and x == 0 and y == 1 and questCounter == 0:
                print("Before you can even reach for the book the hooded figure look straight at you and a voice sounds off in your head 'YOU FOOL! YOU ARE UNWORTHY OF BEING A HERO, DIE NOW AND CURSE IN VAIN! The old man stands up and you can see his eyes radiating with power as he sends you to the afterlife.")
                player_defeat()
            elif command[0] == 'fill' and x == 2 and y == 4 and player_stats["forestCounter"] == 1 and "pail" not in player_inventory:
                print("You fill the bucket.")
                player_inventory.append("pail")
                a = 10
            elif command[0] == 'take' and x == 3 and y == 1 and questCounter == 4 and "artifact" not in player_inventory:
                print("You take the artifact.")
                player_inventory.append("artifact")
                questCounter = 5
                world['23']['FD'].remove('east')
            elif command[0] == 'inventory':
                print(player_inventory)
                is_valid_command = False
            elif command[0] == 'stats':
                print(player_stats)
                is_valid_command = False
            else:
                is_valid_command = False
                print('invalid command')
                
    newloc=str(x)+str(y)#newloc is the same as x and y but are just strings
#determining the new location^
#determining actions after reaching new location v
    
    print()
    if world[newloc]['type'] == '1':#if type is 1 print location
        print("===",world[newloc]['name'],"===")
        print(desc[newloc])        
    elif world[newloc]['type'] == '0':#if type is 0 revert back to old location
        print('You cannot go that way!!')
        x=oldloc[0]
        y=oldloc[1]        
    elif world[newloc]['type'] == '2': #if type is 2 initiate shop subroutine and go back
        print("===",world[newloc]['name'],"===")
        shop() 
        print("=== TOWN ===")
        print(desc["12"])
        newloc='12'
        x = 1
        y = 2 
    elif world[newloc]['type'] == '3':
        if random.randint(0,10) < a:
            world[newloc]['event'] = True
        print("===",world[newloc]['name'],"===")
        print(desc[newloc])
        if world[newloc]['event'] == True:
            event(newloc)
        else:
            print('Apart from that there is nothing out of ordinary now.')    
    elif world[newloc]['type'] == '4':
        counter_dialogue() #go to counter, get some drink bla bla bla
        newloc = "11"
        x = 1
        y = 1
        print("===",world[newloc]['name'],"===")
        print(desc[newloc])
    elif world[newloc]['type'] == '5':
        print("=== RUINED FARM ===")
        print(desc["24"])
        if questCounter == 1:
            print("You are filled with rage and swear to make the goblins pay for their cruelty. You have heard of a lair in the forest to the West.")
            questCounter = 3
        elif player_stats["forestCounter"] == 1 and "pail" not in player_inventory:
            print("You see a well. An empty metal bucket sits beside it.")
            print("FILL the bucket")
        else:
            pass
    elif world[newloc]['type'] == '6':
        print("===",world[newloc]['name'],"===")
        print(desc[newloc]) 
        if questCounter == 4:
            set_foe('apparition_1',0,0,0,0)
            playerstat_update()
            fight()
            print("You slay the apparition and it disappears.")
            print("TAKE the artifact")
    elif world[newloc]['type'] == '7':
        print("===",world[newloc]['name'],"===")
        if questCounter == 0:
            print("You stand in front of the table where the hooded figure is looking upon an ancient book. He doesn't seem to have noticed you. What would you like to do?")
            print("TALK to the figure")
            print("STEAL his book")
        else:
            print(desc[newloc])
    elif world[newloc]['type'] == '8':
        print("===",world[newloc]['name'],"===")
        print(desc[newloc])
        if questCounter == 5:
            print("You feel the artifact resonating in your pocket as you approach the castle.")
    elif world[newloc]['type'] == '9':
        from Puzzle import *
    compass(newloc)
        
    oldloc=str(x)+str(y)#old location
#add the new room types which are only open or close when certain conditions are met
