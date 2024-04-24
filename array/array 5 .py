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

    max_class_size = 20
    num_classes = total_students // max_class_size
    if total_students % max_class_size > 0:
        num_classes += 1

    return num_classes

print("Number of classes needed for DT: ", capacity("DT"))
print("Number of classes needed for Product design: ", capacity("Product design"))
print("Number of classes needed for Art: ", capacity("Art"))
print("Number of classes needed for Food: ", capacity("Food"))
print("Number of classes needed for Engineering: ", capacity("Engineering"))