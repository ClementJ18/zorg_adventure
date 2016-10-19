import random
from player import *
from player_defeat import player_defeat
from status_effect import *
subjects_list = ['player']
foe ={'goblin':{'hp':30,'mhp':30,'dmg':5},
      'hypergoblin':{'hp':15,'mhp':15,'dmg':7},
      'guardian':{'hp':70,'mhp':70,'dmg':8},
      'kirill_the_star_kiriller':{'hp':99999999,'mhp':99999999,'dmg':99999999},
      'goblin_king':{'hp':100,'mhp':100,'dmg':15}
      }
      


bteam = []
subjects = {}

#no need to modify this variable
global dead
dead=[]

com_list=['atk','heal']
sup_com=['heal']
atk_com=['atk']
rteam = ['player']
def playerstat_update():#Update playerstat to the local dictionary
    subjects.update({'player':{}})
    playerparameter = {'hp':player_stats["health"]+player_stats["level"]*70,
                       'mhp':player_stats["health"]+player_stats["level"]*70,
                       'dmg':5+player_stats["level"]*3,
                       'mp':player_stats["mana"]+player_stats["level"]*70,
                       'mmp':player_stats["mana"]+player_stats["level"]*70}
    subjects['player'].update(playerparameter)
    

def turn(subject):#Function which determines the action that a subjects is going to perform, do not use
    mag=0
    if subject == 'player':#If the subject is the player, player choose his action. He can use any action with anyone even if it makes no sense
        #eg. attack himself/heal his enemies maybe to allow strategic advantage such as rage build up in warrior
        is_valid_command = False
        while is_valid_command == False:
            is_valid_command = True
            subject_input = (input('(combat)>')).split()#takes a sentence, separate to action - target
            if subject_input[0] == 'null':
                action = 'null'
                target = 'player'
            elif subject_input[0] == 'use':
                try:
                    potion_use=player_inventory.pop(player_inventory.index(subject_input[1]))
                    print(potion_use)
                    if potion_use == 'health_potion' and subjects['player']['hp'] < subjects['player']['mhp']:
                        mag = 300
                        action = 'heal'
                        target = 'player'
                    else:
                        print('you cannot use that')
                    
                        
                except:
                    print('THAT POTION DOES NOT EXIST')
                    is_valid_command = False

            elif subject_input[0] == 'atk':
                try:
                    action = 'atk'
                    target = subject_input[1]
                    mag = subjects[subject]['dmg']
                except:
                    print('something goes wrong')
                    is_valid_command = False
            elif subject_input[0] == 'cast':
                try:
                    if subject_input[1] == 'fireball':
                        action = 'fireball'
                        target = subject_input[3]
                        mag = 50
                except:
                    print('wrong spell')
                    is_valid_command = False
            else:
                try:
                    action = subject_input[0]
                    target = subject_input[1]
                except:
                    print('no bully program >:(')
                    is_valid_command = False
            
                        

        print('use',action,'on',target)#debugging 
        
        
    elif subject in bteam: #If the subject is the enemies, action also determined by random numbers
        if len(rteam)>0:
            action = com_list[random.randint(0,1)]
        else:
            action = 'heal'
        if action in atk_com:
            mag = subjects[subject]['dmg']
            target = 'player'
        elif action in sup_com:
            mag = 5
            target = bteam[random.randint(0,len(bteam)-1)]#Essentially the same as your teammate's behaviour except the enemies will harm you and heal their 

        print('use',action,'on',target)#debugging 
    
        
    act(action,subject,target,mag)#Takes 3 parameters : action(what to do) subject(who do it) and target(do to who ?)



def act(act,subject,target,mag):#do not use
    
    if act == 'atk':#IF action is attack, will deal X damage target
        subjects[target]['hp'] -= mag#x-=... and x+=... are equivalent to x=x+... or x=x-... they're just shorter
        print(target,'lost 5 health',subjects[target]['hp'],'remain')
    elif act == 'fireball':
        subjects[target]['hp'] -= mag
        print('fireball hits',target,'for',mag,'damage !')
        subjects[subject]['mp'] -= mag/2
        print('mana :',str(subjects[subject]['mp'])+'/'+str(subjects[subject]['mmp']))
        
    elif act == 'heal':#IF action is heal, will deal X damage target
        subjects[target]['hp'] += mag
        if subjects[target]['hp']>subjects[target]['mhp']:
            subjects[target]['hp'] = subjects[target]['mhp']
        print(target,'gain',mag,'health',subjects[target]['hp'],'remain')
    if act == 'null':
        pass
    else:
        pass
    
def set_foe(f1,f2,f3,f4,f5):#Update enemies to local dictionary
    foelist=[f1,f2,f3,f4,f5]
    for i in foelist:
        if i != 0:
            subjects.update({i:foe[i]})
            subjects_list.append(i)
            bteam.append(i)
        
def clear_dict():#Very important, delete every single terms in local dictionary, do not use
    delete =[]
    for i in subjects:
        print(i)
        delete.append(i)
    for i in delete:
        del subjects[i]
    delete=[]
def fight():#Fight module
    
    global dead
    while len(rteam) > 0 and len(bteam) >0:
        
        for unit in subjects:#Rotate through dictionary for each subjects to be the 'subjects' of the turn
            if subjects[unit]['hp']<0:
                pass
            else:
                print('turn',unit)#debugging 
                turn(unit)#It is now unit's turn. 
        print('END round')#When everyone has a go at a turn once the round ends and the fights starts again.
        for i in subjects:
            print(i,'have',subjects[i]['hp'],'left')
            if subjects[i]['hp']<0:
                dead.append(i)
                print('=======',i,'dead','=======')
        if len(dead) > 0:
            for i in dead:
                if i in rteam:
                    rteam.remove(i)
                elif i in bteam:
                    bteam.remove(i)
                if i in subjects_list:
                    subjects_list.remove(i)
                if i in subjects:
                    del subjects[i]
            dead = []
            print('rteam',rteam,'bteam',bteam,'subjects',subjects,'subjlist',subjects_list)
    if len(bteam) > 0:
        print('enemies wins')
        player_defeat()
    else:
        print('u win')
        clear_dict()
        #givexp
        #give stuff
        
            
                    
                
            

    
