
class GarageTicket: 
    def __init__(self): 
        self.currentticket = {"price": 5.00, "paid": False, "ingarage": True, "spacetype": None}

class Kiosk: 
    def __init__(self):
        self.available_spaces = ["Accessible", "Compact 1", "Compact 2", "Oversize 1", "Oversize 2"]
        self.occupied =[]
        self.tickets = [] 
        

    def take_ticket(self):
        if len(self.available_spaces) > 0: 
            for spaces in self.available_spaces: 
                print(f" - {spaces}")
            spotchoice = input("Which space would you like?")
            self.occupied.append(self.available_spaces.pop(self.available_spaces.index(spotchoice)))
            print(self.occupied) #TODO - delete later
            print(self.available_spaces) #TODO - delete later
        else: #(there are no spots available)
            print("There aren't any spots left. Outta luck. Come back later")


    def leave_garage(self): 
        pass

    def run(self): 
        start = True 
        while True: 
            startprompt = input("What would you like to do? Print a ticket or pay and leave? [print/pay] ").lower()
            if startprompt == "print": 
                self.take_ticket()
            elif startprompt == "pay": 
                self.leave_garage()


        

#*When this changes to true it would open the garage and let them know they have 15mins to leave 
currentticket = { "price": 5, "paid": False} 


test1 = Kiosk()
test1.run()