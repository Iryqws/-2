class Dog:
 dogs = 0
 def __init__(self, size=100):
    self.size = size
    Dog.dogs += 1
 
dog_1 = Dog()
dog_2 = Dog(size=120)
cat_1 = Dog(size=150)
cat_2 = Dog(size=190)
print(dog_1.size)
print(dog_2.size)
print(cat_1.size)
print(cat_2.size)
print(Dog.dogs)



from random import*
class Student: 
    def __init__(self, hei=160):
         self.hei = hei
    def grow(self, hei):
         self.hei+=hei
nick = Student()
kate = Student(hei=170)
nick.grow(hei=randint(1, 10))
kate.grow(hei=randint(1, 10))
print(nick.hei)
print(kate.hei)
print()
kate.grow(hei=randint(1, 10))
nick.grow(hei=randint(1, 10))
print(nick.hei)
print(kate.hei)
print()
nick.grow(hei=randint(1, 10))
kate.grow(hei=randint(1, 10))
print(nick.hei)
print(kate.hei)
print()
kate.grow(hei=randint(1, 10))
nick.grow(hei=randint(1, 10))
print(nick.hei)
print(kate.hei)