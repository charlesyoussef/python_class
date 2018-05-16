"""
def filter(func, collec):
    for i in collec:
        if func(number=i):
            yield i


def is_divisible(number=0, dividend=1):
    return number % dividend == 0

def main():
    numbers = [2,5,7,9]

    print(list(filter(is_divisible(dividend=5), numbers)))

"""

def filter(func, collec):
    for i in collec:
        if func(i):
            yield i


def is_divisible(number):
    return number % 3 == 0

def main():
    numbers = [2,5,7,9]

    print(list(filter(is_divisible, numbers)))

if __name__ == '__main__':
    main()
