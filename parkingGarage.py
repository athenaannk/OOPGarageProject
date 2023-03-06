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


class Car:
    def __init__(self, license_plate, make, model, color):
        self.license_plate = license_plate
        self.make = make
        self.model = model
        self.color = color

class Garage:
    def __init__(self):
        self.cars_added = []
        self.spots = 5
        self.ticket_info = {}
        self.pay = 5

    def spots_available(self):
        return self.spots
    
# The split() method splits a string into a list. 
# Dictionary to store car info 
# list available spots subtract one available spot

    def add_car(self, car):
        self.ticket = ['S1', 'S2', 'S3', 'S4', 'S5']

        if self.spots > 0:
            self.cars_added.append(str(car).split(', '))
            self.spots -= 1
            self.car_info = {'code': [], 'license plate': [], 'make': [], 'model': [], 'color': []}

#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object. 
#append the garage code to key index. need index for added cars and removed cars
        for index, i in enumerate(self.cars_added):
                self.car_info['code'].append(self.ticket[index])
                self.car_info['license plate'].append([0])
                self.car_info['make'].append([1])
                self.car_info['model'].append([2])
                self.car_info['color'].append([3])
                return "Please take your ticket and enter the garage."
        
    def remove_car(self, garage_code, pay):
        past_len = len(self.car_info['code'])

        for index, value in enumerate(self.car_info['code']):
                if value == garage_code:
                    print("license plate:", self.car_info['license plate'][index])
                    print("make:", self.car_info['make'][index])
                    print("model:", self.car_info['model'][index])
                    print(" color:", self.car_info['color'][index])
                    
                    removed_car_index = self.car_info['code'].pop(index)
                    self.car_info['license plate'].pop(index)
                    self.car_info['make'].pop(index)
                    self.car_info['model'].pop(index)
                    self.car_info['color'].pop(index)
                    self.spots += 1
#removed car allows another spot to become available

#removed car count has to be greater than cars currently parked if the length of current car is less than the past length
        if len(self.car_info['code']) < past_len:
            pay = input("Are you read to pay and exit the garage? 'Yes' or 'No'")
            if pay == 'Yes':
               print("Your total is $5. Thank you for your payment. You have 15 minutes to exit the garage.")
            else:
                print("Feel free to stay as long as you'd like!")
        

 # displayes all cars in garage
    def cars_in_garage(self):
            for i in self.car_info.items():
                print(i)



our_garage = Garage()
print(our_garage.spots_available())
our_garage.add_car(Car('BG789', 'Civic', 'Honda', 'Black'))
our_garage.add_car(Car('TG908', 'Camry', 'Toyota', 'Blue'))
our_garage.add_car(Car('YN987', 'Wrangler' ,'Jeep', 'White'))
our_garage.cars_in_garage()
print(our_garage.remove_car('S1', 'S5'))
print(our_garage.spots_available())