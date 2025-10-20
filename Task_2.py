import random

def get_numbers_ticket(min, max, quantity):
    if not(1 <= min <= max <= 1000) or not (1 <= quantity <= max):
        return []
    else:
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(random.randint(min, max))
        return sorted(numbers)


lottery_numbers = get_numbers_ticket(15, 49, 6)
print("Лоторейні номера:", lottery_numbers)