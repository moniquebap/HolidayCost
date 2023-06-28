# This program calculates a user's holiday cost including: the plane cost, hotel cost, and car rental cost.
print("======= Holiday costs =======")


# This function calculates the total cost for the hotel stay
def hotel_cost(num_nights):
    total_hotel = num_nights * 100
    return total_hotel


# This function calculates the cost for the flight
def plane_cost(city_flight):
    total_flight = 0
    if city_flight == "1":
        city = "Paris"
        total_flight = 110
    elif city_flight == "2":
        total_flight = 120
        city = "Rome"
    elif city_flight == "3":
        total_flight = 130
        city = "Barcelona"
    elif city_flight == "4":
        total_flight = 140
        city = "Lisbon"
    return total_flight, city


# This function calculates the total cost of the car rental
def car_rental(rental_days):
    total_car = rental_days * 50
    return total_car


# This function calculates the total cost of the holiday adding the values of the other functions: hotel_cost,
# plane_cost, car_rental
def holiday_cost(hotel_cost, plane_cost, car_rental):
    total = hotel_cost + plane_cost[0] + car_rental
    return total


# Validate the city_flight input
total_flight = []
city = []
while True:
    try:
        city_flight = input(
            "Cities:\n 1 - Paris \n 2 - Rome \n 3 - Barcelona \n 4 - Lisbon \nChoose the number of the city you wish "
            "to fly to: ")
        if city_flight not in ["1", "2", "3", "4"]:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please choose a number from 1 to 4.")

# Validate the num_nights input
while True:
    try:
        num_nights = int(input("How many nights you wish to stay in the hotel? "))
        if num_nights < 1:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer value for the number of nights.")

# Validate the rental_days input
while True:
    try:
        rental_days = int(input("How many days are going to be hiring a car for? "))
        if rental_days < 1:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer value for the number of rental days.")

hotel = hotel_cost(num_nights)
plane = plane_cost(city_flight)
car = car_rental(rental_days)

total_holiday = holiday_cost(hotel, plane, car)

print(
    f"For {plane[1]}, your flight cost is £{plane[0]}, hotel cost is £{hotel} and car rental is £{car}. \nTherefore, "
    f"the total cost for your holiday will be £{total_holiday}.")