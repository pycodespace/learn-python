## Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure software programs.

### Key Concepts

1. **Class**: A blueprint for creating objects. Defines a set of attributes and methods that the created objects will have.
2. **Object**: An instance of a class. It is a specific realization of the class with actual values.

### Defining a Class
```python
class MyClass:
    pass  # An empty class
```

### Creating an Object
```python
obj = MyClass()
```

### Class Attributes and Methods
- **Attributes**: Variables that belong to a class.
- **Methods**: Functions that belong to a class.

### Example
```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
```

### Creating an Object and Accessing Attributes/Methods
```python
my_dog = Dog("Buddy", 3)

print(my_dog.name)          # Output: Buddy
print(my_dog.age)           # Output: 3
print(my_dog.description()) # Output: Buddy is 3 years old
print(my_dog.speak("Woof")) # Output: Buddy says Woof
```

### Inheritance
Inheritance allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        return f"{self.name} says {sound}"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

my_cat = Cat("Whiskers", "Siamese")
print(my_cat.name)        # Output: Whiskers
print(my_cat.breed)       # Output: Siamese
print(my_cat.speak("Meow")) # Output: Whiskers says Meow
```

### Encapsulation
Encapsulation restricts access to certain attributes and methods, making the internal representation of an object hidden from the outside.

```python
class Person:
    def __init__(self, name, age):
        self._name = name     # Protected attribute
        self.__age = age      # Private attribute

    def get_age(self):
        return self.__age

person = Person("John", 30)
print(person._name)       # Output: John (accessible, but should be treated as protected)
print(person.get_age())   # Output: 30
```

### Polymorphism
Polymorphism allows different classes to be treated as instances of the same class through inheritance.

```python
class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Chirp"

class Parrot(Bird):
    def speak(self):
        return "Squawk"

class Penguin(Bird):
    def speak(self):
        return "Honk"

def make_bird_speak(bird):
    print(bird.speak())

parrot = Parrot("Polly")
penguin = Penguin("Pingu")

make_bird_speak(parrot)  # Output: Squawk
make_bird_speak(penguin) # Output: Honk
```

### Abstraction
Abstraction hides the complex implementation details and shows only the essential features of the object.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

my_car = Car()
my_car.start_engine()  # Output: Car engine started
```

### Special Methods (Magic Methods)
Special methods in Python start and end with double underscores (`__`). They allow you to define the behavior of objects for built-in operations.

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return len(self.title)

book = Book("1984", "George Orwell")
print(str(book))   # Output: '1984' by George Orwell
print(len(book))   # Output: 4
```

 