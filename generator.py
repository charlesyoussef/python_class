"""
Create a generator primes(max_value) that yields all the
prime numbers between 1 and the given max_value.
"""


def main():
    for number in primes(1000):
        print(number)

def primes(maximum):
    i = 2
    while i < maximum:
        if is_prime(i):
            yield i
        i += 1

def is_prime(number: int) -> bool:
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()

"""
if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	return False
    return True
	        
"""