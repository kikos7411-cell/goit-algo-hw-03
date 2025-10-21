import random

def get_numbers_ticket(min, max, quantity):
    if not(1 <= min <= max <= 1000) or not (1 <= quantity <= max) \
        or not ((max - min + 1) >= quantity):
        return []
    else:
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(random.randint(min, max))
        return sorted(numbers)


lottery_numbers = get_numbers_ticket(980, 999, 11)
print("Лоторейні номера:", lottery_numbers)