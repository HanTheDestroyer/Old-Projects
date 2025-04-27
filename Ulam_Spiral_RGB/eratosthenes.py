import numpy as np


def sieve_of_eratosthenes(upper_limit):
    sieve = np.ones(upper_limit, dtype=bool)
    sieve[0:2] = False
    for i in np.arange(0, int(upper_limit ** 0.5) + 1):
        if sieve[i]:
            sieve[2 * i: upper_limit: i] = False
    return np.where(sieve)[0]


if __name__ == '__main__':
    print(sieve_of_eratosthenes(200000000))

