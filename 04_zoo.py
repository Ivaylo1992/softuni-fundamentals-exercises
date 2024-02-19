
class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammal = []
        self.fish = []
        self.bird = []
        
    def add_animal(self, species, name):

        if species == 'mammal':
            self.mammal.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.bird.append(name)

        Zoo.__animals += 1

    def get_info(self, species):

        if species == 'mammal':
            return f"Mammals in {self.name}: {', '.join(self.mammal)}\nTotal animals: {Zoo.__animals}"
        elif species == 'fish':
            return f"Fishes in {self.name}: {', '.join(self.fish)}\nTotal animals: {Zoo.__animals}"
        elif species == 'bird':
            return f"Birds in {self.name}: {', '.join(self.bird)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    species, name = input().split()
    zoo.add_animal(species, name)

info = input()

print(zoo.get_info(info))
