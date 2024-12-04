# a generator is a pre-built thing that allows you to create data

import string
import itertools

def nums():
    yield 1 
    yield 2
    yield 3

#for x in nums():
    #print(x)

def letters():
    
    for c in string.ascii_lowercase:
        yield c


#for letter in letters():
    #print(letter)

def prime_numbers():
    yield 2
    prime_cache = [2]

    for n in itertools.count(3,2):
        is_prime = True

        for p in prime_cache:
            if n % p == 0:
                is_prime = False
                break

        if is_prime:
            prime_cache.append(n)
            yield n

"""
for p in prime_numbers():
    print(p)
    if p > 100:
        break
"""

squres = (x**2 for x in itertools.count(1))

for x in squres:
    print(x)

    if x > 500:
        break