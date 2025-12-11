# Set examples
A = set()  # Σύνολο από τους φυσικούς αριθμούς 0-100
B = set()  # Σύνολο από τους άρτιους αριθμούς 0-100
C = set()  # Σύνολο από τους περιττούς αριθμούς 0-100
D = set()  # Πολλαπλάσια του 3 από 0-100
E = set()  # πρώτων από 0 έως 100


def is_prime(n):  # Check a number f is prime
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(101):
    A.add(i)
    if i % 2 == 0:
        B.add(i)
    else:
        C.add(i)
    if i % 3 == 0:
        D.add(i)
    if is_prime(i):
        E.add(i)
print(f"Αριθμοί από 1 εως 100: {A}")
print(f"Σύνολο από τους άρτιους αριθμούς 0-100: {B}")
print(f"Σύνολο από τους περιττούς αριθμούς 0-100: {C}")
print(f"Πολλαπλάσια του 3 από 0-100: {D}")
print(f"# πρώτων από 0 έως 100: {E}")


print(f"B ∩ D: {B.intersection(D)}")
print(f"C ∩ E: {C.intersection(E)}")
print(f"E - C: {E.difference(C)}")
print(f"C ^ E: {C.symmetric_difference(E)}")
