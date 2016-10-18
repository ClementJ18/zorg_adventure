import random
subjects_list = ['player','goblin','mark','gobking']
rteam = ['player','mark']
bteam = ['goblin','gobking']
subjects = {'player':{'hp':100},'goblin':{'hp':30},'mark':{'hp':100},'gobking':{'hp':30}}
dead=[]
global dead
com_list=['atk','heal']
sup_com=['heal']
atk_com=['atk']


def turn(subject):#Function which determines the action that a subjects is going to perform
    if subject == 'player':#If the subject is the player, player choose his action. He can use any action with anyone even if it makes no sense
        #eg. attack his teammates or himself/heal his enemies maybe to allow strategic advantage such as rage build up in warrior
        subject_input = (input('(combat)>')).split()#takes a sentence, separate to action - target
        action = subject_input[0]
        target = subject_input[1]

        print('use',action,'on',target)#debugging 
        
    elif subject in rteam and subject != 'player':#IF the subject is in your team but not you, the action is determined by random numbers
        
        if len(bteam)>0:
            action = com_list[random.randint(0,1)] #Your teammates determined which skill to use randomly
        else:
            action = 'heal'
        if action in atk_com:#IF the action he uses is a form of attack. . . 
            target = bteam[random.randint(0,len(bteam)-1)]#He will aim at enemies 
        elif action in sup_com:#IF the action he uses is a support skill. . .
            target = rteam[random.randint(0,len(rteam)-1)]#He will use it on his team
        print('use',action,'on',target)#debugging
        
    elif subject in bteam: #If the subject is the enemies, action also determined by random numbers
        if len(rteam)>0:
            action = com_list[random.randint(0,1)]
        else:
            action = 'heal'
        if action in atk_com:
            target = rteam[random.randint(0,len(rteam)-1)]
        elif action in sup_com:
            target = bteam[random.randint(0,len(bteam)-1)]#Essentially the same as your teammate's behaviour except the enemies will harm you and heal their 

        print('use',action,'on',target)#debugging 
    
        
    act(action,subject,target)#Takes 3 parameters : action(what to do) subject(who do it) and target(do to who ?)



def act(act,subject,target):
    
    if act == 'atk':#IF action is attack, will deal X damage target
        subjects[target]['hp'] -= 5#x-=... and x+=... are equivalent to x=x+... or x=x-... they're just shorter
        print(target,'lost 5 health',subjects[target]['hp'],'remain')
        
    elif act == 'heal':#IF action is heal, will deal X damage target
        subjects[target]['hp'] += 3
        print(target,'gain 3 health',subjects[target]['hp'],'remain')

    
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
    else:
        print('u win')
            
            
                    
                
            

    
