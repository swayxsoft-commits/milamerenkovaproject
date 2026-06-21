class Organism:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def eat(self, amount):
        self.energy += amount

    def is_alive(self):
        return self.energy > 0