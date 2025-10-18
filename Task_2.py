import random

def get_numbers_ticket(min, max, quantity):
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min,max))
    return (numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Лоторейні номера:", lottery_numbers)