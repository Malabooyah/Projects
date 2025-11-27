import random

items = []

amount = int(input("How many items?: "))
for i in range(amount):
	item = input(f"Item {i+1}: ")
	items.append(item)

choice = random.choice(items)
print(f"\nYour random grocery pick is: {choice}")
