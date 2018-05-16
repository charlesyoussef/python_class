"""
Make the following code work.
"""

# Use a `@classmethod` to create this alternative constructor.
# p = Person.from_full_name('John Doe', birth_year=1980)
# print(p.last_name)  # Should print 'Doe'
# print(p)  # Should print "Person(first_name='John', last_name='Doe', birth_year=1980)"

import datetime

class Person:
    def __init__(self, first_name='', last_name='', birth_year=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

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

def main():
    p = Person(first_name='John', last_name='Doe', birth_year=1960)
    # q = Person
    # print(q.__dict__)
    print(p.__dict__)
    print(p.first_name)
    print(p.last_name)
    print(p.get_full_name())
    print(p.get_age())  # This should be a method call. (Return years).
    print(p)
    q = Person.from_full_name('Paul Smith', 1980)
    print (q.first_name)

if __name__ == '__main__':
    main()