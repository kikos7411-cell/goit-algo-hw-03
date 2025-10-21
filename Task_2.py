import random

def get_numbers_ticket(min, max, quantity):
    if not(1 <= min <= max <= 1000) or not (1 <= quantity <= max) \
        or not ((max - min + 1) >= quantity):
        return []
    return sorted(random.sample(range(min, max + 1), quantity))


lottery_numbers = get_numbers_ticket(980, 999, 11)
print("Лоторейні номера:", lottery_numbers)