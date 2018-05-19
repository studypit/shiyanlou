#!/usr/bin/env python3

class Shiyanlou:
    __private_name = 'shiyanlou'
    def __get_private_name(self):
        return self.__private_name

s = Shiyanlou()
# s.__private_name
# s.__get_private_name()

print(s._Shiyanlou__private_name)
print(s._Shiyanlou__get_private_name())

class Animal(object):
    owner = 'jack'
    def __init__(self, name):
        self._name = name
    @classmethod
    def get_owner(cls):
        return cls.owner
    def get_name(self):
        return self._name
    def set_name(self, value):
        self._name = value
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound wang wang wang...')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound miu miu miu...')

"""
dog = Dog('wangcai')
cat = Cat('Kitty')
dog.make_sound()
cat.make_sound()

animals = [Dog('WangCai'), Cat('Kitty'), Dog('LaiFu'), Cat('Betty')]
for animal in animals:
    animal.make_sound()
"""

print(Animal.owner)
print(Cat.owner)

print(Animal.get_owner())
print(Cat.get_owner())
