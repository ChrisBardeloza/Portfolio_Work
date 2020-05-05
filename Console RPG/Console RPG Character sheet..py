# Character sheet
from Character import Character

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

