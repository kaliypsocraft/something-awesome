from sympy import primefactors

c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e = 65537

import math

def trial_division_factorization(n):
    # List to store factors
    factors = []
    
    # Check divisibility by 2 first
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # Check for odd factors from 3 onwards
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    
    # If n is still greater than 2, then n itself is a prime number
    if n > 2:
        factors.append(n)
    
    return factors

# Example usage with a small number for demonstration (use small primes for testing)
n = 769457290801263793712740792519696786147248001937382943813345728685422050738403253
factors = trial_division_factorization(n)
print(factors)
