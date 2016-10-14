x=1
y=2
oldloc=''
command=0
import random
desc13='A small sign hanging above a building made of bricks as opposed to wooden house besides it. \nOne can barely makes out the writing on the sign to read \"Stella\'s potion store\" \nInside there\'s a counter similar to a bar but instead of liquor on the shelf, \nit is filled with numerous bottles of coloured liquids. \n\nBehind the counter stood one girl...'
player = {'hp':100,'mp':100,'inventory':['900'],'gold':10000}      
world = {'12':{'type':'1','name':'town'},#type 1 objects are accesible areas
         '11':{'type':'1','name':'lower town'},
         '10':{'type':'1','name':'tavern'},
         '00':{'type':'1','name':'null'},
         '20':{'type':'1','name':'null'},
         '13':{'type':'2','name':'Stella\'s potion store','keeper':'Stella','desc':desc13}, #type 2 objects are shop areas. Key 'inventory' refers to another list of items that store owns
         '02':{'type':'1','name':'null'},
         '22':{'type':'1','name':'town exit'},
         '21':{'type':'0','name':'null'},#type 0 objects dubbed 'wall' are inaccesible areas and will bounce player back to previous area
         '01':{'type':'0','name':'null'},
         '03':{'type':'0','name':'null'},
         '23':{'type':'0','name':'null'},
         #------------------------town zone----------------------------------
         '32':{'type':'1','name':'plains'},
         '31':{'type':'1','name':'plains-lake intersection'},
         '33':{'type':'1','name':'upper plains'},
         '34':{'type':'1','name':'Farm'}
         }
items = {'000':{'type':'0','name':'HPPotion','cost':100,'fx':'000','pow':'1'},#type 0 items are potions
         '001':{'type':'0','name':'MPPotion','cost':100,'fx':'001','pow':'1'},
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
    for items_on_sale in shopkeeper[keeper]['inventory']: #Iterate through all items in the shopkeeper's inventory
        print(items_on_sale)
    print('what do you want to buy ?')
    is_valid_transaction = False
    print('you have',player['gold'],'remaining')
    while is_valid_transaction == False: #Loop until is_valid_transaction is true
        gold = player['gold']
        print('type item name to buy')
        buy = input('buy')
        print('price :',items[buy]['cost']) 
        if buy in shopkeeper[keeper]['inventory'] and gold-items[buy]['cost'] >= 0:
            print('price :',items[buy]['cost']) 
            player['gold']= gold-items[buy]['cost']#subtracts the cost of itemss from the golds player owns
            player['inventory'].append(shopkeeper[keeper]['inventory'].pop(shopkeeper[keeper]['inventory'].index(buy)))# x.appends() adds item to list x.pop(i) removes items of index i from list and return that value x.index returns the index of that item in list
            print(shopkeeper[keeper]['inventory'])
            print(player['inventory'])
            print('you have',player['gold'],'remaining')
            buyagain = input('Buy more items ?')
            if buyagain == 'yes':
                is_valid_transaction = False
            elif buyagain == 'no':
                is_valid_transaction = True
        else:
            print('Either you don\'t have enough money or that item doesn\'t exist')
            


while True:
    is_valid_direction = False
    while is_valid_direction == False:
        command=input('go :')#ask what direction
        is_valid_direction = True
        if command == 'north':
            y=int(y)+1
        elif command == 'south':#change coordiante corresponding to the direction you are walking
            y=int(y)-1
        elif command == 'east':
            x=int(x)+1
        elif command == 'west':
            x=int(x)-1
        else:
            print('invalid direction')
            is_valid_direction = False
        newloc=str(x)+str(y)#new location is a string return from move function
    if world[newloc]['type'] == '1':#if type is 1 print location
        print('you are at :',world[newloc]['name'])

        
    elif world[newloc]['type'] == '0':#if type is 0 revert back to old location
        print('You cannot go that way!!')
        x=oldloc[0]
        y=oldloc[1]
    elif world[newloc]['type'] == '2': #if type is 2 initiate shop subroutine and go back
        print('you are at :',world[newloc]['name'])
        shop(newloc)
        x=oldloc[0]
        y=oldloc[1]
        print('you are back at',world[oldloc]['name'])
    oldloc=str(x)+str(y)#old location
    
    
        
