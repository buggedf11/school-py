#vehicle_plate_numbers: List to store the number plates of identified vehicles. String
#distance_between_sensors: Constant representing the known distance between the two sensors. Integer
#average_speeds: List to store the calculated average speeds of vehicles. Integer
#speed_limit: Constant representing the legal speed limit. Integer
#speeding_vehicles: List or counter to keep track of instances where vehicles exceed the speed limit. String


camdist = float(input("input distance beetween sensors"))
entry = float(input("enter the time it entered"))
speed = (camdist / entry * 2.237)

if speed > 70:
    print("speed over limit")
print("print speed under")
