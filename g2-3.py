import timeit
from math import sqrt

def znajdz_dzielnik1(n: int) -> list[int]:
    """Find the divisors of a given number"""
    return [i for i in range(1, n + 1) if n % i == 0]

def znajdz_dzielnik2(n: int) -> list[int]:
    """Find the divisors of a given number"""
    return [i for i in range(1, (n // 2) + 1) if n % i == 0]
    
def znajdz_dzielnik3(n: int) -> list[int]:
    """Find the divisors of a given number"""
    return sorted(set([i for i in range(1, int(sqrt(n)) + 1) if n % i == 0 for i in (i, n // i)]))

def czy_liczba_pierwsza(n: int) -> bool:
    """Check if a given number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def znajdz_najwiekszy_dzielnik(n: int) -> int:
    """Find the largest divisor of a given number (excluding the number itself)"""
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i

n = 10 ** 6
print("1. Naiwne znajdowanie dzielnika: ", timeit.timeit(lambda: znajdz_dzielnik1(n), number=1), "sekundy")
print("2. Znajdowanie dzielnika do połowy liczby: ", timeit.timeit(lambda: znajdz_dzielnik2(n), number=1), "sekundy")
print("3. Znajdowanie dzielnika za pomocą pierwiastka: ", timeit.timeit(lambda: znajdz_dzielnik3(n), number=1), "sekundy")
print("4. Znajdowanie największego dzielnika: ", timeit.timeit(lambda: znajdz_najwiekszy_dzielnik(n), number=1), "sekundy")



