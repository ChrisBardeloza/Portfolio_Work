#this is the main game and file to run
from game_loops import *

print('Create a Character')
Character1=Character(
    input('What is your Name?:'),
    input('Choose a Race:'),
    input('Choose a Gender:'),
    input('Choose a Combat class:'),
)

print('Hello '+Character1.name+ ' Welcome to a new game') 
print('you have choosen to be a '+Character1.combat_class)

if Character1.combat_class== 'warrior':
    from Combat_Class_Dict import warrior
    Character1.combat_class=warrior
elif Character1.combat_class== 'mage':
    from Combat_Class_Dict import mage
    Character1.combat_class=mage
elif Character1.combat_class== 'ranger':
    from Combat_Class_Dict import ranger

quest1_loop()

