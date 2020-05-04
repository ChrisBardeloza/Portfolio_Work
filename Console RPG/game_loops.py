# game engine for Console RPG
from Town_Class import town
from Character import Character
from Towns import *
from Combat_Class_Dict import *
# Character sheet
from Character import Character
def create_character():
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
    elif index[3]== 'mage':
        from Combat_Class_Dict import mage
    elif index[3]== 'ranger':
        from Combat_Class_Dict import ranger



def main_loop():
    #while character is alive or game isn't finished we are going to do stuff
        #if a person chooses town you're going to use town_loop
    Britanica= town('Britanica','Miranda', 'Bank of Britanica', 'Wolves Den', 'Daxos', True)
    current_town=Britanica
    print('You are just outside of '+ current_town.name)
    action=input('Would you like to enter?:')
    if action == 'yes':
        town_loop(current_town) 
    
    
def town_loop(town):
    is_in_town=True
    while is_in_town== True:
        print('Welcome to '+ town.name)
        action=input('Where do you want to go?:')
        print(action)
        if action=='got to vendor':
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
        
main_loop()
       
       
        
