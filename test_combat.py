import random

mob={'gob':{'name':'goblin','hp':100,'level':5,'def'},
     'critgob':{'name':'red goblin','hp':10,'level':10}
     }


turn=[]

foe={}
foeHP={}
foedef={}
foelevel={}
foeeva={}
PP={}

PP1 = ['ZORG']
MP1 = ['gob','gob','gob','gob','critgob']

    #combat(PP1,MP1)
def combat(player_party,enemy_party):
    c=0
    for i in enemy_party:
        foe.update({c:i})
        foeHP.update({c:mob[i]['hp']})
        foedef.update({c:mob[i]['def']})
        foeeva.update({c:mob[i]['evasion']})
        c=c+1
    print(foe)
    c=0
   
        
    print(foeHP)
    
     
def DD(level):#damage dealt
    return level*2
def DDR(defense):#defense damage reduction
    return defense/(defense+100)
def EDR(evasion):#evasion damage reduction
    if random.randint(0, evasion) < evasion:
        print('EVADE !')
        return 0
    elif random.randint(0, evasion) < evasion*2:
        return 0.8
    else:
        return 1
    
def DT(level,defense,evasion):#Damage taken
    return DD(level)*DDR(defense)*EDR(evasion)
    
        


     
def turn(player):
    print('Choose : ATTACK - GUARD - MOVE - SKILL')
    command = input('>')
    command = command.split()
    if command[0] = 'attack':
        foeHP[command[1]] -= DT(player,foedef[command[1]],foeeva[command[1]])
        
    
        
    
    
