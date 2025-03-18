# 18.03.2025
# Funkcja sprawdzająca, czy liczba jest pierwsza
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generowanie listy liczb pierwszych do sortowania
def generate_primes(limit):
    primes = []
    num = 2
    while len(primes) < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Funkcja sortowania bąbelkowego
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Porównywanie sąsiednich elementów
            if arr[j] > arr[j+1]:
                # Zamiana miejscami, jeśli są w złej kolejności
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generowanie 10 pierwszych liczb pierwszych
primes = generate_primes(10)
print("Liczby pierwsze przed sortowaniem:", primes)

# Sortowanie liczb pierwszych
bubble_sort(primes)
print("Liczby pierwsze po sortowaniu:", primes)