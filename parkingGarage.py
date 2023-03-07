# Start Your Code here

# Should have the following methods:
# Take a Ticket //
# Decrease the amount of tickets available by 1 //
# Decrease the amount of parking spaces available by 1 //
# Pay for parking
# Display an input that waits for an amount from the user and stores it as a variable
# If the payment variable is not empty (meaning the ticket has been paid) then dispay a message to the user that their ticket has been paid and they have 15 min to leave
# This should update the "current ticket" DICTIONARY key "paid" to True
# leave garage
# If the ticket has been paid, display a messsage of "Thank you, have a nice day!"
# If the ticket has not been paid, display an input prompt for payment
# Once paid, display message, "Thank you, have a nice day!"
# Update parking spaces LIST to increase by 1 (meaning add to the parking spaces LIST //
# tickets >> LIST     parking spaces >> LIST     current ticket >> DICTIONARY


class Garage:
    def __init__(self):
        self.tickets = 5
        self.spots = 5
        self.activeTicket = {"paid": False}

# car enters, takes ticket, one less ticket, one less spot

    def newTicket(self):
        print("Please remember to take your ticket and please enter the garage.")
        self.tickets -= 1
        print(f"There are {self.tickets} tickets available in this garage.")
        self.spots -= 1
        print(
            f"There are {self.spots} parking spaces available in this garage.")


# pay ticket

    def pay(self):
        while True:
            payment = int(input("Please insert $100 and type 100 to confirm."))
            if payment == 100:  # parking is 10 dollars
                print(
                    "Your payment has been accepted. You have 15 minutes to leave or payment will triple. You will be taken back to the main menu now.")
                self.activeTicket["paid"] = True
                break
            else:
                print("SHOW ME THE MONEY!")

# leave garage
    def exitGarage(self):
        if self.activeTicket["paid"] == True:
            print("Thank you, have a nice day!")
            self.tickets += 1
            print(
                f"There are {self.tickets} tickets available in this garage.")
            self.spots += 1
            print(
                f"There are {self.spots} parking spaces available in this garage.")

        else:
            while True:
                exiting = int(input("You still owe $100. Insert $100 and type 100 to confirm."))
                if exiting == 100:
                    print("Thank you, have a nice day!")
                    break
                else:
                    print("You did not show me the money. You live here now.")


def scenario():
    while True:
        new = int(input("\nPlease select from the following options:\n Select 1 to Print Ticket and Enter Garage\n Select 2 to Pay for Parking \n Select 3 to Leave Garage\n"))

        if new == 1:
            fellsPoint.newTicket()
        elif new == 2:
            fellsPoint.pay()
        elif new == 3:
            fellsPoint.exitGarage()
            break


fellsPoint = Garage()
scenario()
