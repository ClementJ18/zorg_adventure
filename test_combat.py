import random
from player import *
from player_defeat import player_defeat

subjects_list = ['player']
foe ={'goblin':{'hp':30,
                'mhp':30,
                'dmg':5,
                'guard':False,
                'frozen':False,
                'poison_active':False,
                'poison_counter':0,
                },
      'hypergoblin':{'hp':15,
                     'mhp':15,
                     'dmg':7,
                     'guard':False,
                     'frozen':False,
                     'poison_active':False,
                     'poison_counter':0,
                     },
      'guardian':{'hp':70,
                  'mhp':70,
                  'dmg':8,
                  'guard':False,
                  'frozen':False,
                  'poison_active':False,
                  'poison_counter':0,
                  },
      'kirill_the_star_kiriller':{'hp':99999999,
                                  'mhp':99999999,
                                  'dmg':99999999,'guard':False,
                                  'frozen':False,
                                  'poison_active':False,
                                  'poison_counter':0,
                                  },
      'goblin_king':{'hp':100,
                     'mhp':100,
                     'dmg':15,
                     'guard':False,
                     'frozen':False,
                     'poison_active':False,
                     'poison_counter':0,
                     },
      'apparition_1':{'hp':40,
                     'mhp':40,
                     'dmg':8,
                     'guard':False,
                     'frozen':False,
                     'poison_active':False,
                     'poison_counter':0,
                     },
      'unkillable_boss':{'hp':99999999,
                         'mhp':99999999,
                         'dmg':99999999,
                         'guard':False,
                         'frozen':False,
                         'poison_active':False,
                         'poison_counter':0,
                                  },
      'final_boss':{'hp':1000000000,
                    'mhp':1000000000,
                    'dmg':200,
                    'guard':False,
                    'frozen':False,
                    'poison_active':False,
                    'poison_counter':0,
                                  },
      }
Fround = 1      

items =['health_potion', 'mana_potion']
bteam = []
subjects = {}
global dead
dead=[]

com_list=['atk','heal']
sup_com=['heal']
atk_com=['atk']
rteam = ['player']
def poisoning(poison_active):

    if subjects['player']['poison_active'] == False:
        if random.randint(0, 9) <= 1:
            print('You have been poisoned')
            subjects['player']['poison_active'] = True
            subjects['player']['poison_counter'] = Fround + 3
exp_before_next_level = 50

def level_up():
    global exp_before_next_level
    while player_stats["experience"] >= exp_before_next_level:
        # reset exp counter
        player_stats["experience"] = player_stats["experience"] - exp_before_next_level
        # level up the player
        player_stats["level"] = player_stats["level"] + 1
        # add health and mana
        player_stats["max_health"] = player_stats["max_health"] + 10
        player_stats["health"] = player_stats["health"] + 10
        player_stats["max_mana"] = player_stats["max_mana"] + 25
        player_stats["mana"] = player_stats["mana"] + 25
        # increase experience necessary to level up
        exp_before_next_level = 1.2 * exp_before_next_level
        print('leveled up!')

    
    


def poison_damage(poison_active):

    if subjects['player']['poison_active'] == True:
        poison_damage = int(0.01 * player_stats["max_health"])
        subjects['player']["hp"] = subjects['player']["hp"] - poison_damage
        print("You have taken " + str(poison_damage) + " damage due to poisoning!")
        
def playerstat_update():#Update playerstat to the local dictionary
    subjects.update({'player':{}})
    playerparameter = {'hp':player_stats["health"]+player_stats["level"]*70,
                       'mhp':player_stats["health"]+player_stats["level"]*70,
                       'dmg':5+player_stats["level"]*3,
                       'mp':player_stats["mana"]+player_stats["level"]*70,
                       'mmp':player_stats["mana"]+player_stats["level"]*70,
                       'poison_active':False,
                       'poison_counter':0,
                       'guard':False,
                       'charge':0,
                       'rage':0,
                       'frozen':False}
    subjects['player'].update(playerparameter)


def turn(subject):#Function which determines the action that a subjects is going to perform, do not use
    mag=0

    
    
    if subject == 'player':#If the subject is the player, player choose his action. He can use any action with anyone even if it makes no sense
        #=========================================================
        if player_stats['class'] == 'warrior':
            print('You have',subjects['player']['rage'],'rage')
        elif player_stats['class'] == 'mage':
            print('You have',subjects['player']['mp'],'mp')
        
        elif player_stats['class'] == 'rogue' and len(bteam)>0:
            fire_at=bteam[random.randint(0,len(bteam)-1)]
            act('RAF',subject,fire_at,5+player_stats["level"]*5)
            print(player_stats["arrows"])
        #==========================================================
        #eg. attack himself/heal his enemies maybe to allow strategic advantage such as rage build up in warrior
        is_valid_command = False
        while is_valid_command == False:
            is_valid_command = True
            subject_input = (input('(combat)>')).split()#takes a sentence, separate to action - target
            if subject_input == []:
                is_valid_command = False
            elif subject_input[0] == 'null': #null 
                action = 'null'
                target = subject
            elif subject_input[0] == 'use':
                try:
                    if subject_input[1] in ['health_potion','health'] and subjects[subject]['hp'] < subjects[subject]['mhp']:
                        mag = 300
                        action = 'heal'
                        target = subject
                        potion_use = 'health_potion'
                    elif subject_input[1] == 'mana_potion' and subjects[subject]['mp'] < subjects[subject]['mmp']:
                        mag = 300
                        action = 'restore_mana'
                        target = subject
                    
                    
                    
                    else:
                        print('You cannot use that')
                    
                    print('use',player_inventory.pop(player_inventory.index(potion_use)))  
                except:
                    print('THAT POTION DOES NOT EXIST')
                    is_valid_command = False

            elif subject_input[0] == 'atk':
                try:
                    action = 'atk'
                    target = subject_input[1]
                    mag = subjects[subject]['dmg']
                except:
                    print('Target does not exist')
                    is_valid_command = False
            #CASTER==CASTER==CASTER==CASTER==CASTER==CASTER==CASTER==CASTER==CASTER==
            elif subject_input[0] == 'cast' and player_stats['class'] == 'mage':
                try:
                    if subject_input[1] == 'fireball':
                        action = 'fireball'
                        
                        target = subject_input[3]
                        mag = 50
                    elif subject_input[1] == 'freeze' and player_stats['class'] == 'mage':
                        action = 'freeze'
                        
                        target = subject_input[3]
                        mag = 40
                except:
                    print('Wrong spell')
                    is_valid_command = False
            elif subject_input[0] == 'heal':
                try:
                    action = subject_input[0]
                    target = subject_input[1]
                    mag = 20
                except:
                    print('invalid target or invalid spell use')
        
            #FIGHTER==FIGHTER==FIGHTER==FIGHTER==FIGHTER==FIGHTER==FIGHTER==FIGHTER==
            elif subject_input[0] == 'guard' and player_stats['class'] == 'warrior':
                action = 'guard'
                target = subject
                mag = player_stats['level']+1
            elif subject_input[0] == 'strike' and player_stats['class'] == 'warrior':
                try:
                    action = 'strike'
                    target = subject_input[1]
                    mag = subjects[subject]['dmg'] + subjects[subject]['charge']
                except:
                    print('Target does not exist')
                    is_valid_command = False
            

            
            
        
                
            #ROGUE==ROGUE==ROGUE==ROGUE==ROGUE==ROGUE==ROGUE==ROGUE==ROGUE==ROGUE==

            else:
                try:
                    is_valid_command = False
                except:
                    print('Your commands makes no sense !')
                    is_valid_command = False
                        

        #debugging 
        
        
    elif subject in bteam: #If the subject is the enemies, action also determined by random numbers
        if len(rteam)>0:
            action = com_list[random.randint(0,1)]
        else:
            action = 'heal'
        if action in atk_com:
            mag = subjects[subject]['dmg']
            target = 'player'
            poisoning(subjects['player']['poison_active'])
            
        elif action in sup_com:
            mag = 5
            target = bteam[random.randint(0,len(bteam)-1)]#Essentially the same as your teammate's behaviour except the enemies will harm you and heal their 

        print(subject,'use',action,'on',target)
    
    try:    
        act(action,subject,target,mag)#Takes 3 parameters : action(what to do) subject(who do it) and target(do to who ?)
    except:
        print('Wrong action or target')
        turn(subject)
        


def act(act,subject,target,mag):#do not use
    
    if act == 'atk':#IF action is attack, will deal X damage target
        #============================================
        if subjects[target]['class'] == 'rogue':
            if random.randint(0,9) <3:
                print('You evade the attack !')
            else:
                subjects[target]['hp'] -= mag
                print(target,'lost',mag,'health')
        #==============================================
        elif subjects[target]['guard'] == True:
            subjects[target]['hp'] -= int(mag*(player_stats['level']/(player_stats['level']+3)))#x-=... and x+=... are equivalent to x=x+... or x=x-... they're just shorter
            subjects[target]['charge'] += mag*player_stats['level']
            print(target,'gain',mag,'charge')
        else:
            subjects[target]['hp'] -= mag
        subjects['player']['rage'] += 1
        print('Gained rage !')
    elif act == 'RAF':
        subjects[target]['hp'] -= mag
        print('Fired arrows at',target)
        
    
        print(target,'lost', mag, 'health',subjects[target]['hp'],'remain')
    elif act == 'strike':
        subjects[target]['hp'] -= mag
        print(target,'lost',mag,'health',subjects[target]['hp'],'remain')
    elif act == 'guard':
        subjects[subject]['guard'] = True
    elif act == 'fireball':
        subjects[target]['hp'] -= mag
        subjects[subject]['mp'] -= mag/2
        print('Fireball hits',target,'for',mag,'damage !')
        
        print('mana :',str(subjects[subject]['mp'])+'/'+str(subjects[subject]['mmp']))
    elif act == 'freeze':
        subjects[target]['frozen'] = True
        subjects[target]['frozenex'] = Fround + 1
        subjects[subject]['mp'] -= mag*2
        print('mana :',str(subjects[subject]['mp'])+'/'+str(subjects[subject]['mmp']))
        
        
    elif act == 'heal':#IF action is heal, will deal X damage target
        subjects[target]['hp'] += mag
        if subjects[target]['hp']>subjects[target]['mhp']:
            subjects[target]['hp'] = subjects[target]['mhp']
        print(target,'gain',mag,'health',subjects[target]['hp'],'remain')
    elif act == 'mana_restore':
        subjects[target]['mp'] += mag
        if subjects[target]['mp']>subjects[target]['mmp']:
            subjects[target]['mp'] = subjects[target]['mmp']
        print(target,'gain',mag,'mana',subjects[target]['mp'],'remain')
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
        delete.append(i)
    for i in delete:
        del subjects[i]
    delete=[]
def fight():#Fight module
    foenum = len(bteam)
    
    global dead
    global Fround
    while len(rteam) != 0 and len(bteam) != 0:
        print('===================Round',Fround,'=======================')
        
        for unit in subjects:#Rotate through dictionary for each subjects to be the 'subjects' of the turn
            if subjects[unit]['hp']<0:
                pass
            elif subjects[unit]['frozen'] == True:
                print('Target frozen ! Turn skipped !')
                if subjects[unit]['frozenex'] == Fround:
                    subjects[unit]['frozen'] = False
                if subjects[unit]['poison_counter'] == Fround:
                    subjects[unit]['poison_active'] = False
            else:
                print('turn',unit)#debugging 
                turn(unit)#It is now unit's turn. 
        print('===================END Round=======================')#When everyone has a go at a turn once the round ends and the fights starts again.
        Fround=Fround+1
        
        if subjects['player']['poison_active'] == True:
            poison_damage(True)
            if subjects['player']['poison_counter'] == 3:
                subjects['player']['poison_active'] = False
                subjects['player']['poison_counter'] = 0
                
                
        for i in subjects:
            print(i,'have',subjects[i]['hp'],'left.')
            if subjects[i]['hp']<=0:
                dead.append(i)
                print('=======',i,'Dead','=======')
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
    if len(bteam) > 0:
        print('Enemies win !')
        if bteam[0] == 'unkillable_boss':
            clear_dict()
            
            pass
        else:
            player_defeat()

    else:
        print('You win')
        player_stats['health'] = subjects['player']['hp']
        player_stats['experience'] += foenum*50
        print(foenum*50)
        clear_dict()
        level_up()
        #givexp
        #give stuff
