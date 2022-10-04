end = 100000
i = 0

def isprime(x):
    i = 3

    if x == 2:
        return 1
    elif x % 2 == 0 or x == 1:
        return 0
    else:
        while (i**2 <= x):
            if (x % i == 0):
                return 0
            i += 2
        return 1

while (end > i):
    if isprime(i) == 1:
        with open("./primes", "a") as f:
            f.write(f"\n{i}")
    i += 1