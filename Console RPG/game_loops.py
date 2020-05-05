# game engine for Console RPG
from Town_Class import town
from Character import Character
from Towns import *
from Monsters import *
from monster_class import monster

Character1=Character(
    input('What is your Name?:'),
    input('Choose a Race:'),
    input('Choose a Gender:'),
    input('Choose a Combat class:'),
)

print('Hello '+Character1.name+ ' Welcome to a new game') 
print('you have choosen to be a '+Character1.combat_class)

for index in range(Character1):

    if index[3]== 'warrior':
        from Combat_Class_Dict import warrior
        Character1.combat_class=warrior
    elif index[3]== 'mage':
        from Combat_Class_Dict import mage
        Character1.combat_class=mage
    elif index[3]== 'ranger':
        from Combat_Class_Dict import ranger
        Character1.combat_class=ranger


main_loop()
def main_loop():
    #while character is alive or game isn't finished we are going to do stuff
        #if a person chooses town you're going to use town_loop
    Britanica= town('Britanica','Miranda', 'Bank of Britanica', 'Wolves Den', 'Daxos', True)
    current_town=Britanica
    print('You are just outside of '+ current_town.name)
    action=input('Would you like to enter?:')
    if action == 'yes':
        town_loop(current_town) 
    print(current_town.vendor+' has trouble to disscuss')
   
    for action in town_loop(current_town):
        if action=='go to vendor':
            print('Hello '+Character1.name+' I am '+current_town.vendor+'.  There is a group of Goblins messing with my supply routes. I need you to help me out and deal with them.')
            quest1= input('Will you help?:')
            if quest1== 'yes':
                monster.name=goblin
                print('Defeat the Goblins')
                combat_loop()
            elif quest1== 'no': 
                town_loop(current_town)
                



    
    
def town_loop(town):
    is_in_town=True
    while is_in_town== True:
        print('Welcome to '+ town.name)
        action=input('Where do you want to go?:')
        
        if action=='go to vendor':
            print('Visits '+town.vendor)
        elif action=='go to stash':
            print('Visits '+town.stash)
        elif action=='go to inn':
            print('Visits '+town.inn)
        elif action=='go to healer':
            print('Visits '+town.healer)
        elif action=='leaves town':
            is_in_town = False
            print('Leaves '+ town.name)


def combat_loop():
    
    is_in_combat=True
    while is_in_combat==True:

        print('Defeat the '+monster.name)

        
main_loop()
       
       
        
