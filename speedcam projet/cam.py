speed_limit = 70 # Speed limit in km/h
distance = 100 # Distance between the two cameras

while True:
    
    while True:
        try:
            time = float(input("Enter the time the vehicle entered: "))
            break
        except ValueError:
            print("Invalid input")

    speed = (distance / time)

    if speed > speed_limit:
        print("Speed over limit")
    
        with open("/workspaces/school-py/plates.txt", "a") as f:
            while True:
                plate = input("Enter the plate number: ")
                if len(plate) == 7 and plate[:2].isalpha() and plate[2:4].isdigit() and plate[4:].isalpha():
                    f.write(str(plate) + "\n")
                    break
                else:
                    print("Invalid plate number format. Please try again.")


    else:
        print("Within speed limit")
