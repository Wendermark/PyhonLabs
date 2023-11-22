class Animal:
    def __init__(self, breed, price):
        self.breed = breed
        self.price = price

    def move(self):
        pass

class Fish(Animal):

    def move(self):
        return "Рыба плавает"

class Bird(Animal):

    def move(self):
        return "Птица летит"

class PetShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_most_expensive(self):
        if not self.animals:
            return "В магазине нет животных."
        
        most_expensive_animal = max(self.animals, key = lambda x: x.price)

        return f"Самая дорогая порода: {most_expensive_animal.breed}, стоимость: {most_expensive_animal.price}"

    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(f"Порода: {animal.breed}, Стоимость: {animal.price}\n")

pet_shop = PetShop()

pet_shop.add_animal(Fish("Золотая рыбка", 20))
pet_shop.add_animal(Fish("Гуппи", 10))
pet_shop.add_animal(Bird("Попугай", 50))
pet_shop.add_animal(Bird("Канарейка", 30))

expensive_breed_info = pet_shop.get_most_expensive()
print(expensive_breed_info)

pet_shop.write_to_file("animal_info.txt")