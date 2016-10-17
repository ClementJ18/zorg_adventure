x=1
y=2
oldloc='12'
command=0
newloc='12'
event = False
import random

desc13='A small sign hanging above a building made of bricks as opposed to wooden house besides it. \nOne can barely makes out the writing on the sign to read \"Stella\'s potion store\" \nInside there\'s a counter similar to a bar but instead of liquor on the shelf, \nit is filled with numerous bottles of coloured liquids. \n\nBehind the counter stood one girl...'
player = {'inventory':['900','000'],'gold':10000}      
world = {'01':{'type':'3','name':'Tavern : Dark corner','FD':['west','south','north'],'event':True},
         '10':{'type':'1','name':'Tavern : Counter','FD':['east','south','west']},
         '11':{'type':'1','name':'The prancing pony tavern','FD':['east']},
         '12':{'type':'1','name':'Town','FD':['']},
         '13':{'type':'2','name':'Stella\'s potion store','keeper':'Stella','desc':desc13, 'FD':['east','north','west']},
         '00':{'type':'0','name':''},
         '02':{'type':'0','name':''},
         '03':{'type':'0','name':''},
         #------------------------town zone----------------------------------
         '21':{'type':'1','name':'lake','FD':['west']},
         '22':{'type':'3','name':'plains','FD':[''],'event':False},
         '23':{'type':'1','name':'moors','FD':['west']},
         '31':{'type':'1','name':'Artifact room','FD':['east','north','south']},
         '30':{'type':'0','name':''},
         #------------------------plains zone--------------------------------
         '24':{'type':'1','name':'Ruined Farm','FD':['east','north']},
         '14':{'type':'1','name':'Forest','FD':['south']},
         '15':{'type':'1','name':'goblin\'s lair','FD':['west','east','north']}
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
shopkeeper = {'Stella':{'intro':'Welcome to Stella\'s potion store ! How may I help you', 'inventory':['000','000','000']}}


def shop(loc):
    keeper = world[loc]['keeper'] #The shopkeeper variable contains the keeper of that shop
    print('owner :',keeper)
    print(world[loc]['desc'])
    print('')
    print(keeper,':',shopkeeper[keeper]['intro']) #Print the intro of that shopkeeper
    print('Here\'s a list of avaliable items :')
    print()
    for items_on_sale in shopkeeper[keeper]['inventory']: #Iterate through all items in the shopkeeper's inventory
        print(items_on_sale)
    print('what do you want to buy ?')
    print()
    is_valid_transaction = False
    print('you have',player['gold'],'remaining')
    print()
    while is_valid_transaction == False: #Loop until is_valid_transaction is true
        
        print('type item name to buy')
        buy = input('buy')
        if buy not in shopkeeper[keeper]['inventory']:
            print('item not in stock')
        elif buy in shopkeeper[keeper]['inventory']:
            player['inventory'].append(shopkeeper[keeper]['inventory'].pop(shopkeeper[keeper]['inventory'].index(buy)))
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
        if action == 'GIVE' and player['inventory'].count('000') >= 1:
            print('god bless your kind heart')
            player['inventory'].remove('000')
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
    world[loc]['event'] = False #This kills the event trigger so that an event may only happen once unless made happen again.
        
        
        
    
while True:
    is_valid_direction = False# set this to false
    if event == True:
        is_valid_direction = True
        
    while is_valid_direction == False:
        print('you are at1 :',world[str(x)+str(y)]['name'])
        command=input('go :')#ask what direction
        is_valid_direction = True
        if command in world[oldloc]['FD']:
            is_valid_direction = False
            print(command in world[oldloc]['FD'])
            print('wrong direction motherfucker')
            
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
            else:
                is_valid_direction = False
                print('invalid direction')
        print(x,y)

        newloc=str(x)+str(y)#newloc is the same as x and y but are just strings
#determining the new location^
#determining actions after reaching new location v
        
    if world[newloc]['type'] == '1':#if type is 1 print location
        print('you are at :',world[newloc]['name'])

        
    elif world[newloc]['type'] == '0':#if type is 0 revert back to old location
        print('You cannot go that way!!')
        x=oldloc[0]
        y=oldloc[1]
        
    elif world[newloc]['type'] == '2': #if type is 2 initiate shop subroutine and go back
        print('you are at2 :',world[newloc]['name'])
        shop(newloc)
        x=oldloc[0]
        y=oldloc[1]
        print('you are back at',world[oldloc]['name'])
        
    elif world[newloc]['type'] == '3': #type 3 areas are areas which events MAY happen
        print('you are at :',world[newloc]['name'])
        if world[newloc]['event'] == True:#type 3 area will triggers the event at its location IF the event key is true
            event(newloc)
        else:
            print('Apart from that there is nothing out of ordinary. Perhaps come back later ?') #Else, it give you a hint that something could happen here.
#note that the fuction event() may also be modified to allow movement in previously forbidden direction to create a "gate" that will open
#after certain condition are met which is probably important for random events although I have a simpler solution to that...

    elif world[newloc]['type'] == '4':#future expansion...? 

        pass
            
    
    
        
    oldloc=str(x)+str(y)#old location

#add ability to move around
#add the new room types which are only open or close when certain conditions are met
#add some form of map key which changes depends on the items you have.
    
        
