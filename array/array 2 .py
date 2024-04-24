numbers = [10, 20, 30, 40, 50]

def check(numbers):
    for num in numbers:
        if num > 30:
            print(f"{num} is greater than 30")
        else:
            print(f"{num} is not greater than 30")

check(numbers)
