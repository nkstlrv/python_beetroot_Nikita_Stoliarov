
class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return f"{__class__.__name__} says woof, woof" 


class Cat(Animal):
    def talk(self):
        return f"{__class__.__name__} says meow"



c_1 = Dog().talk()
c_2 = Cat().talk()

def talking_func(animal):
    if animal == "Cat":
        return c_2
    elif animal == "Dog":
        return c_1
    elif animal == "Cat, Dog":
        return c_2, c_1
    else:
        return "There is no such option"
    
print(talking_func("Cat, Dog"))

