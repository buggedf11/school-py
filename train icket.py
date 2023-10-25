num_adults = int(input("How many adults are traveling? "))
num_children = int(input("How many children are traveling? "))
stations = int(input("How many stations are you traveling? "))

time = int(input("What time is it (24-hour clock)? "))

base_cost = stations * 20

if 6 <= time < 9:
    # Add the extra charge of £5 per station between 6 am and 9 am
    total_cost = base_cost + stations * 5
else:
    total_cost = base_cost

child_discount = 0.5  # Half price for children
total_cost = (num_adults * total_cost) + (num_children * child_discount * total_cost)

print("The total cost of the tickets is £" + str(total_cost))
