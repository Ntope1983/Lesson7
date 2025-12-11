import random


def create_random_integer_1to19():
    return random.randint(10, 19)


def create_random_integer_20to39():
    return random.randint(20, 39)


def create_random_even_1to10():
    even_number = [number for number in range(1, 10) if number % 2 == 0]  # Λίστα με άρτιους απο 1-10
    return random.choice(even_number)


def create_random_odd_40to49():
    odd_numbers = [number for number in range(40, 50) if number % 2 != 0]  # Λίστα με άρτιους απο 1-10
    return random.choice(odd_numbers)


def create_10_6_numbers_lotto():
    total = []
    for i in range(10):
        total.append(create_6_numbers_lotto())
    return total


def create_6_numbers_lotto():  # Δημιουργία 6 αριθμών σε ένα σύνολο
    total_6_numbers = set()
    total_6_numbers.add(create_random_integer_1to19())  # Εισαγωγή 1ου αριθμού από 1-19
    temp = create_random_integer_1to19()  # Εισαγωγή 2ου αριθμού
    while temp in total_6_numbers:  # Εισαγωγή 2ου αριθμού από 1-19 όσο υπάρχει στο σύνολο total_6_numbers
        temp = create_random_integer_1to19()
    total_6_numbers.add(temp)
    total_6_numbers.add(create_random_integer_20to39())  # Εισαγωγή 3ου αριθμού από 20-39
    temp = create_random_integer_20to39()
    while temp in total_6_numbers:  # Εισαγωγή 4ου αριθμού από 20-39 όσο υπάρχει στο σύνολο total_6_numbers
        temp = create_random_integer_20to39()
    total_6_numbers.add(temp)
    total_6_numbers.add(create_random_odd_40to49())  # Εισαγωγή 5ου αριθμού από 40-49
    temp = create_random_even_1to10()
    while temp in total_6_numbers:  # Εισαγωγή 6ου περιττού από 1-10 όσο υπάρχει στο σύνολο total_6_numbers
        temp = create_random_even_1to10()
    total_6_numbers.add(temp)

    return total_6_numbers


print(create_10_6_numbers_lotto())
