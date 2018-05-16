"""
Look at the following two functions (create_sum_table
and create_product_table). There is a lot of code
duplication between these functions.

Rewrite the code to get rid of this duplication.
(Usually, when two functions are very similar,
 except for a very small part, this part needs
 to be extracted out of the function.) In this
exercise, the common part is a calculation, so figure
out how to extract that.
"""

def create_sum_table(width, height):
    """
    Create a table (list of lists) with the given dimensions
    where each cell is populated with the sum of the coordinates.
    """
    result = []
    for i in range(width):
        row = []
        for j in range(height):
            row.append(i + j)
        result.append(row)
    return result


def create_product_table(width, height):
    """
    Create a table (list of lists) with the given dimensions
    where each cell is populated with the product of the coordinates.
    """
    result = []
    for i in range(width):
        row = []
        for j in range(height):
            row.append(i * j)
        result.append(row)
    return result

def addition(a, b):
    return a + b

def multiply(a, b):
    return a * b

def create_table(width, height, expression):
    result = []
    for i in range(width):
        row = []
        for j in range(height):
            row.append(expression(i, j))
        result.append(row)
    return result

def print_table(table):
    for row in table:
        for value in row:
            print(value, ' ', end='')
        print()
    print()


def main():
    print_table(create_table(4, 4, addition))
    print_table(create_table(4, 4, multiply))

    print_table(create_table(4, 4, lambda a, b: a + b))
    print_table(create_table(4, 4, lambda a, b: a * b))

def create_table(width, height, expression):
    result = []
    for i in range(width):
        row = []
        for j in range(height):
            row.append(i * j)
        result.append(row)
    return result

def print_table(table):
    for row in table:
        for value in row:
            print(value, ' ', end='')
        print()
    print()


def main():
    print_table(create_sum_table(4, 4))
    print_table(create_product_table(4, 4))


if __name__ == '__main__':
    main()