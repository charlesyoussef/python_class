"""
Take the `Person` class from the previous exercise. Add an
`Address` class and extend it so that the following becomes
possible. "A Person has-an address".
"""


import datetime

class Person:
    def __init__(self, first_name='', last_name='', birth_year='0', address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.address = address

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
        # return f'{self.first_name} {self.last_name}'
        # return '{} {}'.format(self.first_name, self.last_name)
        # return '%s %s' % (self.first_name, self.last_name)


    def get_age(self):
        current_year = datetime.datetime.now().year
        age = current_year - self.birth_year
        return age

    def __repr__(self):
        return('Person %s %s is born in %r' % (self.first_name, self.last_name, self.birth_year))

    @classmethod
    def from_full_name(cls, complete_name, birth_year):
        first , last = complete_name.split(maxsplit=1)
        return cls(first, last, birth_year)

class Address:
    def __init__(self, street, number, city):
        self.street = street
        self.number = number
        self.city = city


def main():
    a = Address(street='De Kleetlaan', number=6, city='Diegem')
    p = Person('John', 'Doe', birth_year=1980, address=a)
    print(p.address.street)


if __name__ == '__main__':
    main()