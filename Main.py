import json


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} питается.")


class Bird(Animal):
    def make_sound(self):
        return "Звук птиц: чирик, чирик"


class Mammal(Animal):
    def make_sound(self):
        return "Звук млекопитающих: рёв"


class Reptile(Animal):
    def make_sound(self):
        return "Звук пресмыкающихся: шипенье"


# Полиморфизм
def animal_sound(animalss):
    for animal in animalss:
        print(animal.make_sound())


# Композиция
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, возраст {animal.age} года (лет)")

    def list_staff(self):
        for staff in self.staff:
            print(f"{staff.name}, {staff.role}")

    def save_zoo_info(self, filename):
        zoo_info = {'animals': [vars(animal) for animal in self.animals],
                    'staff': [vars(staff) for staff in self.staff]}
        with open(filename, 'w') as file:
            json.dump(zoo_info, file)

    def load_zoo_info(self, filename):
        with open(filename, 'r') as file:
            zoo_info = json.load(file)
            for animal_data in zoo_info['animals']:
                animal = Animal(animal_data['name'], animal_data['age'])
                self.animals.append(animal)
            for staff_data in zoo_info['staff']:
                # Create staff objects based on the data
                pass


class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role


class ZooKeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Работник кормления животных")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


# Примеры
bird = Bird("Воробей", 2)
mammal = Mammal("Лев", 5)
reptile = Reptile("Змея", 3)

animals = [bird, mammal, reptile]
animal_sound(animals)

zoo = Zoo()

zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(ZooKeeper("Иван"))
zoo.add_staff(Veterinarian("Доктор Айболит"))

zoo.list_animals()
zoo.list_staff()

zk = ZooKeeper("Иван")
zk.feed_animal(bird)

vt = Veterinarian("Доктор Айболит")
vt.heal_animal(mammal)

zoo.save_zoo_info("zoo_info.json")
zoo.load_zoo_info("zoo_info.json")
