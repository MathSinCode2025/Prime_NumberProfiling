import math


def P(n):
    if n < 2:
        return 0  # Numbers less than 2 are not prime

    # Calculate the summation term
    summation = 0
    for d in range(2, n):  # Sum from d=2 to d=n-1
        numerator = d - (n % d)
        term = math.floor(numerator / d)
        summation += term

    # Calculate the final result
    numerator = n ** 2 - summation
    denominator = n ** 2
    result = math.floor(numerator / denominator)

    return result


def nth_prime(n):
    count = 0  # Count of primes found
    m = 2  # Start checking from m = 2

    while True:
        if P(m) == 1:  # If m is prime
            count += 1
            if count == n:  # If we've found the n-th prime
                return m
        m += 1

        # Safety check: Stop if m exceeds 2^n (though this is unlikely for small n)
        if m >= 2 ** n:
            raise ValueError(f"Could not find the {n}-th prime within the range m < 2^{n}.")


# Test the function
n_values = [800]
for n in n_values:
    print(f"The {n}-th prime is: {nth_prime(n)}")