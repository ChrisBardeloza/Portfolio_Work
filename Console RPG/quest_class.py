class quest:
    def __init__(self, is_accepted, name, objective, reward):
        self.is_accepted=is_accepted
        self.name=name
        self.objective=objective
        self.reward=reward


# for action in town_loop(current_town):
#         if action=='go to vendor':
#             print('Hello '+Character1.name+' I am '+current_town.vendor+'.  There is a group of Goblins messing with my supply routes. I need you to help me out and deal with them.')
#             quest1= input('Will you help?:')
#             if quest1== 'yes':
#                 monster.name=goblin
#                 print('Defeat the Goblins')
#                 combat_loop()
#             elif quest1== 'no': 
#                 town_loop(current_town)