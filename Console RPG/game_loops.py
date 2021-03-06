# game engine for Console RPG
from Town_Class import town
from Character import Character
from Towns import *
from Monsters import *
from monster_class import monster
from quests import *

def Main_loop():
    creating_character=True
    while creating_character== True:
        print('Create a Character')
        Character1=Character(
            input('What is your Name?:'),
            input(' -Human\n -Elf\n -Dwarf\nChoose a Race:'),
            input('(M/F)\nChoose a Gender: '),
            input(' -warrior\n -mage\n -ranger\nChoose a Combat class:'),
        )

        print('Hello '+Character1.name+ ' Welcome to a new game') 
        print(Character1.race+'s are very useful around here.')

        if Character1.race=='human':
            from Races import human
            Character1.race=human()
        elif Character1.race== 'elf':
            from Races import elf
            Character1.race=elf()
        elif Character1.race== 'dwarf':
            from Races import dwarf
            Character1.race=dwarf()
        
        print('you have choosen to be a '+Character1.combat_class)

        if Character1.combat_class== 'warrior':
            from Combat_Class_Dict import warrior
            Character1.combat_class=warrior()
        elif Character1.combat_class== 'mage':
            from Combat_Class_Dict import mage
            Character1.combat_class=mage()
        elif Character1.combat_class== 'ranger':
            from Combat_Class_Dict import ranger
            Character1.combat_class=ranger()

        print('You can you use these skills :\n' 
        +Character1.combat_class.skill1.name+'\n' 
        +Character1.combat_class.skill2.name+'\n' 
        +Character1.combat_class.skill3.name+'' 
        )
        return Character1
        break


    # if (current_town.quest.is_accepted == true)
        # print(quest1.objective)
        # combat_loop()

def town_loop(Character1,town):
    is_in_town=True
    while is_in_town== True:
        print('Welcome to '+ town.name)
        action=input('Where do you want to go?:')

        if action=='go to vendor':
            print('Visits '+town.vendor)
            if town==Britanica and town.quest=='quest1':
                current_monster=monster('Pract',goblin('goblin'))
                print(quest1.prompt)
                quest1.promptPlayerToAccept()
                if quest1.is_accepted==True:
                    print('Leaves Town')
                    is_in_town=False
                    print(quest1.objective)
                    print('Attack to start combat')
                    combat_loop(current_monster,Character1)
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


def combat_loop(current_monster,Character1):

    # Character1.deal_damage(goblin)
        # if character uses attack skill use deal_damage funtion
            # if current monster use deal_damage function
                
    is_in_combat=True
    while is_in_combat==True:
        turn = 1
        print(f'Round {turn}')
       
        action= input('Use a skill:')
        if action == Character1.combat_class.skill1.name:
            print(Character1.combat_class.skill1.description)
            Character1.combat_class.executeskill(Character1,current_monster)
            if Character1.combat_class.skill1.is_attack_skill==True:
                Character1.do_damage(current_monster)
            elif Character1.combat_class.skill1.is_attack_skill!=True:
                print(Character1.combat_class.skill1.description)

        elif action == Character1.combat_class.skill2.name:
            Character1.combat_class.executeskill(Character1,current_monster)
            print(Character1.combat_class.skill2.description)
            if Character1.combat_class.skill2.is_attack_skill==True:
                Character1.do_damage(current_monster)
            elif Character1.combat_class.skill2.is_attack_skill!=True:
                Character1.combat_class.skill2.description
        
        elif action == Character1.combat_class.skill3.name:
            Character1.combat_class.executeskill(Character1,current_monster)
            print(Character1.combat_class.skill3.description)
            if Character1.combat_class.skill3.is_attack_skill==True:
                Character1.do_damage(current_monster)
            elif Character1.combat_class.skill3.is_attack_skill!=True:
                Character1.combat_class.skill3.description

        if current_monster.monster_class.hp <= 0:
            print('You Win!!!')
            is_in_combat=False
            break
        elif current_monster.monster_class.hp >= 0 and turn%3==1:
            monster_action=current_monster.monster_class.skill1
            if monster_action==current_monster.monster_class.skill1:
                print(current_monster.monster_class.skill1.description)
                current_monster.monster_class.executeskill(current_monster,Character1)
                if current_monster.monster_class.skill1.is_attack_skill==True:
                    current_monster.do_damage(Character1)
                turn+=1
        elif current_monster.monster_class.hp >= 0 and turn%3==2:
            monster_action=current_monster.monster_class.skill2
            if monster_action==current_monster.monster_class.skill2:
                print(current_monster.monster_class.skill2.description)
                current_monster.monster_class.executeskill(current_monster,Character1)
                if current_monster.monster_class.skill2.is_attack_skill==True:
                    current_monster.do_damage(Character1)
                turn+=1
        elif current_monster.monster_class.hp >= 0 and turn%3==0:
            monster_action=current_monster.monster_class.skill3
            if monster_action==current_monster.monster_class.skill3:
                print(current_monster.monster_class.skill3.description)
                current_monster.monster_class.executeskill(current_monster,Character1)
                if current_monster.monster_class.skill3.is_attack_skill==True:
                    current_monster.do_damage(Character1)
                turn+=1
            
        if Character1.combat_class.hp <=0:
            print('You Lose :( Try again')
            combat_loop(current_monster,Character1)
        elif Character1.combat_class.hp>=1 and is_in_combat==False:
            break
            

                

def quest1_loop(Character1):
    # while character is alive or game isn't finished we are going to do stuff
        # if a person chooses town you're going to use town_loop
    current_town=Britanica
    current_quest=quest1
    print('You are just outside of '+ current_town.name)
    action=input('Would you like to enter?:')
    if action == 'yes':
        town_loop(Character1,current_town)
        print(current_town.vendor+' has trouble to disscuss')





