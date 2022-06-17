class GarageTicket:
    def __init__(self):
        self.currentticket = {"price": "5.00", "paid": False, "ingarage": True, "spacetype": None}


class Kiosk:
    def __init__(self):
        self.available_spaces = ["Accessible", "Compact 1", "Compact 2", "Oversize 1", "Oversize 2"]
        self.occupied = []
        self.tickets = []

    def take_ticket(self):
        if len(self.available_spaces) > 0:
            for spaces in self.available_spaces:
                print(f" - {spaces}")
            spotchoice = input("Which space would you like? ").title()
            self.occupied.append(self.available_spaces.pop(self.available_spaces.index(spotchoice)))
            self.printedticket = GarageTicket()
            self.printedticket.currentticket["spacetype"] = spotchoice
            print(f'You got the {self.printedticket.currentticket["spacetype"]} space. Please go park your car.')
            print(self.occupied)  # TODO - delete later
            print(self.available_spaces)  # TODO - delete later
        else:  # (there are no spots available)
            print("There aren't any spots left. Outta luck. Come back later")

    def leave_garage(self):
        print("Occupied Spaces")
        for spaces in self.occupied:
            print(f" - {spaces}")
        insertticket = input("What spot did you just leave? ").title()
        self.available_spaces.append(insertticket)
        print(f'You owe {self.printedticket.currentticket["price"]}')
        payment = input(f'How would you like to pay? Cash or Card? {self.printedticket.currentticket["price"]}: ').title()
        if payment == "Cash" or payment == "Card":
            self.printedticket.currentticket ["paid"] = True
            print("Payment successful, thank you! Have a nice day! You have 15 minutes to leave.")
        else:
            print("Pay up! Or we will call 911.")

    def run(self):
        start = True
        while start == True:
            startprompt = input("What would you like to do? Print a ticket or pay and leave? [print/pay] Press Q to turn off the kiosk: ").lower()
            if startprompt == "print":
                self.take_ticket()
            elif startprompt == "pay":
                self.leave_garage()
            elif startprompt == "q":
                print("Powering down...")
                start = False


test1 = Kiosk()
test1.run()
