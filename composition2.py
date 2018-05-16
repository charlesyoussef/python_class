import datetime
from typing import Optional

class Address:
    def __init__(self, street='', number=0, city=''):
        self.street = street
        self.number = number
        self.city = city

class Person:
    """

    """
    def __init__(self, first_name:str='', last_name:str='', birth_year:int=0, address: Optional[Address]):
        if address is None:
            address = Address()

        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

        self.street = ''
        self.city = ''
        self.address = address  #  type:  Optional[Address]

    @classmethod
    def from_full_name(cls, full_name, birth_year):
        first, last = full_name.split(maxsplit=1)
        return cls(first, last, birth_year)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
        #return '{} {}'.format(self.first_name, self.last_name)
        #return '%s %s' % (self.first_name, self.last_name)
        #return self.first_name + ' ' + self.last_name

    def get_age(self):
        return datetime.datetime.now().year - self.birth_year

    def __repr__(self):
        return 'Person(first_name=%r, last_name=%r, birth_year=%r)' % (
            self.first_name, self.last_name, self.birth_year
        )