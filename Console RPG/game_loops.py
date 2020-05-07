# game engine for Console RPG
from Town_Class import town
from Character import Character
from Towns import *
from Monsters import *
from monster_class import monster
from quests import *

# def character_loop():
#     creating_character=True
#     if creating_character is True:
        # print('Create a Character')
        # Character1=Character(
        #     input('What is your Name?:'),
        #     input('Choose a Race:'),
        #     input('Choose a Gender:'),
        #     input('Choose a Combat class:'),
        # )

        # print('Hello '+Character1.name+ ' Welcome to a new game') 
        # print('you have choosen to be a '+Character1.combat_class)

        # if Character1.combat_class== 'warrior':
        #     from Combat_Class_Dict import warrior
        #     Character1.combat_class=warrior
        # elif Character1.combat_class== 'mage':
        #     from Combat_Class_Dict import mage
        #     Character1.combat_class=mage
        # elif Character1.combat_class== 'ranger':
        #     from Combat_Class_Dict import ranger
    
def quest1_loop():
    #while character is alive or game isn't finished we are going to do stuff
        #if a person chooses town you're going to use town_loop
    Britanica= town('Britanica','Miranda', 'Bank of Britanica', 'Wolves Den', 'Daxos', True)
    current_town=Britanica
    monster.monster_class=goblin
    print('You are just outside of '+ current_town.name)
    action=input('Would you like to enter?:')
    if action == 'yes':
        print(current_town.vendor+' has trouble to disscuss')
        town_loop(current_town) 
    
    for action in town_loop(town):
        if action=='go to vendor':
            break
            print('Hello traveler I am '+current_town.vendor+'.  There is a group of Goblins messing with my supply routes. I need you to help me out and deal with them.') 
            input(quest1.is_accepted)
        
        if quest1.is_accepted=='yes':
            quest1.is_accepted=True

            while quest1.is_accepted== True:
                print(quest1.objective)
        
        combat_loop()
                   

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
    # Character1.deal_damage(goblin)
    is_in_combat=True
    while is_in_combat==True:
        print('Defeat the '+monster.monster_class)

        

       
       
        
