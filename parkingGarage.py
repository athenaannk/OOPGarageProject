# Start Your Code here

# Should have the following methods:
# Take a Ticket
# Decrease the amount of tickets available by 1
# Decrease the amount of parking spaces available by 1
# Pay for parking
# Display an input that waits for an amount from the user and stores it as a variable
# If the payment variable is not empty (meaning the ticket has been paid) then dispay a message to the user that their ticket has been paid and they have 15 min to leave
# This should update the "current ticket" DICTIONARY key "paid" to True
# leave garage
# If the ticket has been paid, display a messsage of "Thank you, have a nice day!"
# If the ticket has not been paid, display an input prompt for payment
# Once paid, display message, "Thank you, have a nice day!"
# Update parking spaces LIST to increase by 1 (meaning add to the parking spaces LIST
# tickets >> LIST     parking spaces >> LIST     current ticket >> DICTIONARY


class Car:
    def __init__(self, license_plate, model, color):
        self.license_plate = license_plate
        self.model = model
        self.color = color

class Garage:
    def __init__(self):
        self.cars_added = []
        self.spots = 5
        self.ticket_info = {}
        self.pay = 0

    def spots_available(self):
        return self.spots

    def add_car(self, car):
        self.ticket = ['S1', 'S2', 'S3', 'S4', 'S5']
        if self.spots > 0:
            self.cars_added.append(str(car).split(', '))
            self.spots -= 1
            self.car_info = {'code': [], 'license plate': [], 'Model': [], 'Color': [] }

    def remove_car(self, given_code, bill_hours):
        past_len = len(self.car_info['code'])
        
        if given_code not in self.car_info['code']:
            print ('Your car could not be found. Are you sure you parked here?')

        else:
            for index, value in enumerate(self.car_info['code']):
                if value == given_code:
                    print("Your car's license plate is:", self.car_info['license plate'][index])
                    print("Your car's model is:", self.car_info['Model'][index])
                    print("Your car's color is:", self.car_info['color'][index])
                    
                    removed_car_index = self.car_info['code'].pop(index)
                    self.car_info['license plate'].pop(index)
                    self.car_info['Model'].pop(index)
                    self.car_info['color'].pop(index)

                    self.spots += 1


        if len(self.car_info['code']) < past_len:
            while True:
                if bill_hours.isnumeric():
                    list_of_time_and_code = [bill_hours, removed_car_index]
                    break