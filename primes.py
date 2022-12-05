"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def primes(number_of_primes):
    if number_of_primes <1:
        raise ValueError
    prime=2
    count=0
    list = []
    while count<number_of_primes:
        isPrime=True
        for x in range(2, int(math.sqrt(prime)+1)):
            if prime%x==0:
                isPrime=False
                break
        if isPrime:
            list.append(prime)
            count+=1
        prime+=1
    return list
