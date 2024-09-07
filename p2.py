
class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return f"Обєкт класу людина з ім'ям {self.name} "

    def __int__(self):
        return self.age

    def say_hi(self):
        print(f'Привіт! Мене звуть {self.name}! Мені {self.age} років')

    def birthday(self,years):
        self.age += years

class Auto:
    def __init__(self, brand, max_passengers=5):
        self.brand = brand
        self.max = max_passengers

        self.passengers = []
    def add_passengers(self, *new_passengers):
        for passenger in new_passengers:
            if len(self.passengers) >= self.max:
                print('Авто вже зайняте іди на вулицю!')
            else:
                self.passengers.append(passenger)
    def print_all_passengers(self):
        if len(self.passengers) >= self.max:
            print(f'Авто {self.brand} порожнє!')
        else:
            print(f'Список пассажирів {self.brand}: ')
            for passengers in self.passengers:
                passengers.say_hi()




bob = Human("Боб", 17, 186)

bob.say_hi()

alice = Human("Аліса", 25, 150)

alice.name = "Аліса"
alice.age = 25
alice.height = 150

alice.say_hi()

print(alice)
print(bob)

bmw = Auto('BMW')
tesla = Auto('Tesla')

tesla.add_passengers(bob, alice)

bmw.print_all_passengers()
tesla.print_all_passengers()