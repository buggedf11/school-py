import random

with open("/workspaces/school-py/quote/q.txt", "r") as file:
    quotes = file.readlines()

random_index = random.randint(0, len(quotes) - 1)
random_quote = quotes[random_index].strip()

print(random_quote)
