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



    # if (current_town.quest.is_accepted == true)
        # print(quest1.objective)
        # combat_loop()

def town_loop(town):
    is_in_town=True
    while is_in_town== True:
        print('Welcome to '+ town.name)
        action=input('Where do you want to go?:')

        if action=='go to vendor':
            print('Visits '+town.vendor)
            if town==Britanica and town.quest=='quest1':
                
                print(quest1.prompt)
                quest1.promptPlayerToAccept()
                if quest1.is_accepted==True:
                    print('Leaves Town')
                    is_in_town=False
                    combat_loop()
        # if town.quest != null
            # town.quest.openingDialogue()
            # town.quest.promptPlayerToAccept()
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
        # if character uses attack skill use deal_damage funtion
            # if current monster use deal_damage function
                # 
    is_in_combat=True
    while is_in_combat==True:
        print(quest1.objective)
        action= input('')

def quest1_loop():
    # while character is alive or game isn't finished we are going to do stuff
        # if a person chooses town you're going to use town_loop
    current_town=Britanica
    current_monster=goblin
    current_quest=quest1
    print('You are just outside of '+ current_town.name)
    action=input('Would you like to enter?:')
    if action == 'yes':
        town_loop(current_town)
        print(current_town.vendor+' has trouble to disscuss')





