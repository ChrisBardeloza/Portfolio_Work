class quest:
    def __init__(self, prompt, name, objective, reward, is_accepted):
        self.prompt=prompt
        self.name=name
        self.objective=objective
        self.reward=reward
        self.is_accepted=is_accepted

    # def openingDialogue():
    #     print('') # do nothing; this is a base class -- let subclasses override
    def promptPlayerToAccept(self):
        print('.') # do nothing; this is a base class -- let subclasses override
    # def doQuest():
    #     return false # do nothing; this is a base class -- let subclasses override



