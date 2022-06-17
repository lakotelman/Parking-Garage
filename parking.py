

class Kiosk: 
    def __init__(self):
        self.available_spaces = []
        self.tickets = [] 
        self.currentticket = {"price": 5.00, "paid": False}

    def take_ticket(self): 
        pass
        #decreases the amount of tickets and spaces by 1

#*When this changes to true it would open the garage and let them know they have 15mins to leave 
currentticket = { "price": 5, "paid": False} 
