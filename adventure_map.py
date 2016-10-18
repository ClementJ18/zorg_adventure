
from counter_dialogue import counter_dialogue
from player import *
from introduction import *

x=1
y=2
oldloc='12'
command=0
newloc='12'
event = False
import random

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
     '15':'You have found the goblin lair. The goblins\'s primitive shelters are in poor shape, with rotting wooden frames covered in brightly-coloured fungi. Inside the huts, you see mouldy blankets, crude blackthorn cudgels, and the carcasses of the farmer\'s livestock. A blackened, unplucked chicken burns over a campfire. The forest trail leads SOUTH, out of the lair. What would you like to do?',
     }
player = {'inventory':['900','000'],'gold':10000}      
world = {'01':{'type':'3','name':'DARK TAVERN CORNER','FD':['west','south','north'],'event':True},         
         '10':{'type':'4','name':'TAVERN COUNTER','FD':['east','south','west']},         
         '11':{'type':'1','name':'THE PRANCING PONY TAVERN','FD':['east']},
         '12':{'type':'1','name':'TOWN CENTER','FD':[''],'desc':''},
         '13':{'type':'2','name':'STELLA\'S POTION SHOP','keeper':'Stella', 'FD':['east','north','west']},
         '00':{'type':'0','name':''},
         '02':{'type':'0','name':''},
         '03':{'type':'0','name':''},
         #------------------------town zone----------------------------------
         '21':{'type':'1','name':'THE ANCIENT LAKE','FD':['west']},
         '22':{'type':'3','name':'PLAINS OF LITHLAD','FD':[''],'desc':'','event':False},
         '23':{'type':'1','name':'MOORS OF THE NIBIN-NOEG','FD':['west'],'desc':''},
         '31':{'type':'1','name':'ARTIFACT CHAMBER','FD':['east','north','south']},
         '30':{'type':'0','name':''},
         #------------------------plains zone--------------------------------
         '24':{'type':'3','name':'RUINED FARM','FD':['east','north'],'event':True},
         '14':{'type':'1','name':'ERYN VANWË','FD':['south','west']},
         '15':{'type':'1','name':'GOBLIN LAIR','FD':['west','east','north']}
         #------------------------Goblin's territory-------------------------
         }
#type 0 objects dubbed 'wall' are inaccesible areas and will bounce player back to previous area
#type 1 objects are accesible areas
#type 2 objects are shop areas. Key 'inventory' refers to another list of items that store owns
items = {'000':{'id':'000','type':'0','name':'HPPotion','cost':100,'fx':'000','pow':'1'},#type 0 items are potions
         '001':{'id':'001','type':'0','name':'MPPotion','cost':100,'fx':'001','pow':'1'},
         '100':{'type':'1','name':'Poisoned Dagger','cost':1250,'fx':'100'},#type 1 items are equippable
         '900':{'type':'9','name':'Adventurer\'s license','cost':0}#type 9 items are quest         
         }
shopkeeper = {'Stella':{'intro':'Welcome to Stella\'s potion store ! How may I help you \nI can get you a list of item in stock you could \'buy\' or can I help you with something\'else\'.',
                        'inventory':['000','000','000']},
                        'else':'beep boop im a robot'
                       }
def compass(loc): #some form of debugging tool (maybe have this in the game as well ?)which shows where are the exits because SCREW the exit dictionary i mean holy shit i'm not gonna spend hours filling out the exit dictionary like the game template that thing is confusing.
    print(loc)
    cx = int(loc[0])
    cy = int(loc[1])
    north = str(cx)+str(cy+1)
    south = str(cx)+str(cy-1)
    east = str(cx+1)+str(cy)
    west =str(cx-1)+str(cy)
    print(north,south,east,west,cx,cy) #don't forget to remove all the pr
    if north in world and 'north' not in world[loc]['FD']:
        print('to north:',world[north]['name'])
    if south in world and 'south' not in world[loc]['FD']:#basically asking if the room in certain direction are EXISTS and accesible or not. 
        print('to south:',world[south]['name'])
    if east in world and 'east' not in world[loc]['FD']:
        print('to east:',world[east]['name'])
    if west in world and 'west' not in world[loc]['FD']:
        print('to west:',world[west]['name'])
def shop(loc):
    keeper = world[loc]['keeper'] #The shopkeeper variable contains the keeper of that shop
    print('owner :',keeper)
    print(desc[loc])
    print('')
    print(keeper,':',shopkeeper[keeper]['intro']) #Print the intro of that shopkeeper

    act = input('')
    if act == 'yes':
        is_valid_transaction = False
        print('Here\'s a list of avaliable items :')
        print()
        for items_on_sale in shopkeeper[keeper]['inventory']: #Iterate through all items in the shopkeeper's inventory
            print(items_on_sale)
        print('what do you want to buy ?')
        print()
        print('you have',player['gold'],'remaining')
        print()
    elif act == 'else':
        is_valid_transaction = True
    
    while is_valid_transaction == False: #Loop until is_valid_transaction is true        
        print('type item name to buy')
        buy = input('buy')
        if buy not in shopkeeper[keeper]['inventory']:
            print('item not in stock')
        elif buy in shopkeeper[keeper]['inventory']:
            player_inventory.append(shopkeeper[keeper]['inventory'].pop(shopkeeper[keeper]['inventory'].index(buy)))
            # x.appends() adds item to list x.pop(i) removes items of index i from list and return that value x.index returns the index of that item in list
            player['gold'] = player['gold'] - items[buy]['cost']
            print(player['gold'])
        elif buy == 'nothing':
            print('well that sucks... now get out of my store')
        print('Would you like to buy some other stuff ? just say \'yes\' or \'no\'')
        player_input = input('>')
        if player_input == 'yes':
            is_valid_transaction = False
        elif player_input == 'no':
            is_valid_transaction = True

                                          
def event(loc):
    #This is literally a sample set of event to demonstrate how you can manipulates event triggers by having some action ( like accessing some place ) triggers the other event so it could happen when otherwise nothing will
    #Delete this shit later
    if loc == '22': #accessing plains after visiting the dark tavern corner will made the old man showed up
        print('You have encountered an old man')
        print('He states that he is very sick and want a healing potion')
        print('Will you \'GIVE\' the potion to him or \'REFUSE\' to aid him')
        action = input('>')
        if action == 'GIVE' and player_inventory.count('000') >= 1:
            print('god bless your kind heart')
            player_inventory.remove('000')
            print('healing potion removed')
            player['gold'] += 50
            print('recieve gold from the old man')
            print(player['gold'])
        elif action == 'REFUSE':
            print('the old man simply walks away')
    elif loc == '01': #accessing dark tavern corner first time triggers the event at plains so the old man appears
        print('You overheard a conversation about an old man stranded outside east of the town')
        print('you thought it is a good idea to go there... perhaps with a healing potion')
        world['22']['event'] = True
   
    elif loc == '24':
        print('As you approach the farm you see it was destroyed and burnt by a golbin raid, anger takes control of your mind and you swear upon the old and the new gods to destroy the golbin lair situated north-west of the farm.')
    world[loc]['event'] = False #This kills the event trigger so that an event may only happen once unless made happen again.
            
while True:
    is_valid_direction = False# set this to false
    if event == True:
        is_valid_direction = True
        
    while is_valid_direction == False:
        command=input('go :')#ask what direction
        is_valid_direction = True
        if command in world[oldloc]['FD']:
            is_valid_direction = False
            print('Sorry, what?')         
        else:
            if command == 'north':
                y=int(y)+1
            elif command == 'south':#change coordiante corresponding to the direction you are walking
                y=int(y)-1
            elif command == 'east':
                x=int(x)+1
            elif command == 'west':
                x=int(x)-1
            elif command == 'where am i':
                print('at',world[str(x)+str(y)]['name'])
                is_valid_direction = False
            elif command == 'compass':
                compass(str(x)+str(y))
                is_valid_direction = False
            else:
                is_valid_direction = False
                print('invalid direction')
        newloc=str(x)+str(y)#newloc is the same as x and y but are just strings
#determining the new location^
#determining actions after reaching new location v        
    if world[newloc]['type'] == '1':#if type is 1 print location
        print("===",world[newloc]['name'],"===")
        print(desc[newloc])        
    elif world[newloc]['type'] == '0':#if type is 0 revert back to old location
        print('You cannot go that way!!')
        x=oldloc[0]
        y=oldloc[1]        
    elif world[newloc]['type'] == '2': #if type is 2 initiate shop subroutine and go back
        print("===",world[newloc]['name'],"===")
        shop(newloc)
        x=oldloc[0]
        y=oldloc[1]
        print("===",world[newloc]['name'],"===")        
    elif world[newloc]['type'] == '3':
        print("===",world[newloc]['name'],"===")
        if world[newloc]['event'] == True:
            event(newloc)
        else:
            print(desc[newloc])
            print('Apart from that there is nothing out of ordinary now.')    
    elif world[newloc]['type'] == '4':
        counter_dialogue() #go to counter, get some drink bla bla bla 
        x=oldloc[0]
        y=oldloc[1]#OH look, you're back at the tavern ! MAGIC 
        print('you are back at',world[oldloc]['name'])
        
    oldloc=str(x)+str(y)#old location
#add the new room types which are only open or close when certain conditions are met
