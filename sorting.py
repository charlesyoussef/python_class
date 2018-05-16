"""
Part 1. Sort the following list of names, using the last name.
(Assume that names only contain one space.)
"""

data = ['Matthew Thorpe', 'Eve Rhodes', 'Clement Green', 'Camilla Tailer']

def get_last_name(name):
    return name.split()[1]

data2 = sorted(data, key=get_last_name)
data2 = sorted(data, key=lambda name: name.split()[1])


# Part 2: Write a function that sorts the following list of
#         words, alphabetically, but case insensitive.

list_of_words = """Macros can also be used to achieve some of the
effects of higher order functions. However, macros cannot
easily avoid the problem of variable capture; they may
also result in large amounts of duplicated code, which
can be more difficult for a compiler to optimize. Macros
are generally not strongly typed, although they may produce
strongly typed code.
D""".split()

def to_lower(text):
    return text.lower()

sorted(list_of_words, key=lambda text: text.lower())
sorted(list_of_words, key=to_lower)
sorted(list_of_words, key=str.lower)
