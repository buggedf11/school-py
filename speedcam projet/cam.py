#vehicle_plate_numbers: List to store the number plates of identified vehicles. String
#distance_between_sensors: Constant representing the known distance between the two sensors. Integer
#average_speeds: List to store the calculated average speeds of vehicles. Integer
#speed_limit: Constant representing the legal speed limit. Integer
#speeding_vehicles: List or counter to keep track of instances where vehicles exceed the speed limit. String

average_speeds = []
speeding_vehicles = []
vehicle_plate_numbers = []
speed_limit = 70
distance_between_sensors = 100 

entry = float(input("Enter the time the vehicle entered: "))
speed = (distance_between_sensors / entry )

if (speed > speed_limit):
    print("Speed over limit")
    speeding_vehicles.append(speed)
else:
    print("Within speed limit")

vehicle_plate_numbers.append(input("Enter the number plate of the identified vehicle: "))
average_speeds.append(speed)
