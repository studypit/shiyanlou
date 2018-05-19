#!/usr/bin/env python3

class Animal:
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError

cat = Animal()
# cat.age = 'h'
cat.age = 3
print(cat.age)
