import random

a = (random.randint(1,6))
b = (random.randint(1,6))
c = (random.randint(1,6))
if a == b == c:
    score = a + b + c
    print (score)
elif a == b == c:
    score = a + b + c
    print(score)

elif a == b or a == c or b == c:
    score = 2 * (a + b + c - max(a, b, c))
    print(score)

else:
    score = a + b + c - max(a, b, c)
    print(score)
