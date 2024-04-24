options = [
    [0, "DT", "118"],
    [1, "Product design", "61"],
    [2, "Art", "20"],
    [3, "Food", "30"],
    [4, "Engineering", "27"]
]

def capacity(subject):
    total_students = 0
    for course in options:
        if course[1] == subject:
            total_students += int(course[2])

    return total_students

def room(subject):
    class_size = capacity(subject)
    if class_size > 25:
        return "D1 (smaller room)"
    else:
        return "D2 (larger room)"

print("Room for DT class: ", room("DT"))
print("Room for Product design class: ", room("Product design"))
print("Room for Art class: ", room("Art"))
print("Room for Food class: ", room("Food"))
print("Room for Engineering class: ", room("Engineering"))