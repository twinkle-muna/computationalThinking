burgers = []
drinks= []

for _ in range (3):
    burgers.append(int(input()))

for _ in range (2):
    drinks.append(int(input()))

print((min(burgers)+ min(drinks)) - 50)