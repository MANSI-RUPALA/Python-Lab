import random

random = [random.randint(-15, 15) for _ in range(10)]
squared = list(map(lambda x: x ** 2, random))

print("Random Numbers:", random)
print("Squared Numbers:", squared)
