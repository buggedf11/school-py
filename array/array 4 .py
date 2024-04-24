options = [
    [0, "DT", "118"],
    [1, "Product design", "61"],
    [2, "Art", "20"],
    [3, "Food", "30"],
    [4, "Engineering", "27"]
]

def demand_level(num_students):
    if num_students >= 100:
        return "High"
    elif num_students >= 50:
        return "Medium"
    else:
        return "Low"

for course in options:
    num_students = int(course[2])
    demand = demand_level(num_students)
    print(f"Subject: {course[1]}, Demand: {demand}")