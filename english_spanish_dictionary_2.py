

"""
Implement the missing 'reverse_dictionary' function.
It should reverse the given default dictionary of translations.
The outcome will also be another dictionary where the keys
are strings and the values are lists of strings (some
Spanish words have multiple English translations).

When this works, check out Python's defaultdict to make the
code easier to read.
"""


def main():
    english_to_spanish = {
        'one': ['uno'],
        'two': ['dos'],
        'three': ['tres'],
        'trio': ['tres'],
        'free': ['libre', 'gratis'],
    }

    print(reverse_dictionary(english_to_spanish))
""" 
def reverse_dictionary(en_to_es_dict: dict):
    es_dict = {};
    for i in en_to_es_dict:
        es_list = en_to_es_dict[i]
        for j in es_list:
            if not (j in es_dict):
                es_dict.
                es[j].append(i)
    return es
"""

from collections import defaultdict

def reverse_dictionary(translations):
    result = defaultdict(list)

    for source, destinations in translations.items():
        for dest in destinations:
            result[dest].append(source)

    return result

if __name__ == '__main__':
    main()