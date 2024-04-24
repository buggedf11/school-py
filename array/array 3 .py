options = [
    [0, "DT", "118"],
    [1, "Product design", "61"],
    [2, "Art", "20"],
    [3, "Food", "30"],
    [4, "Engineering", "27"]
]

total_students = 0
for course in options:
    total_students += int(course[2])

print("The total number of students enrolled in optional courses is:", total_students)