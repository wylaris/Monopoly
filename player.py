class Player:
    name = ""
    id = None
    space = 0
    balance = 1500
    properties = []


    def __init__(self, name, id):
        self.name = name
        self.id = id

    
    def __str__(self):
        return f"{self.name}\n\r Space: {self.space}\n Balance: ${self.balance}\n Properties: {self.properties}"