while True:
    print("1.playgame 2.instuctions 3.quit")
    try:
        a = int(input("enter a number 1 - 3: "))
        if a in [1, 2, 3]:
            print("let's go")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
