class Population:
    def __init__(self, species):
        self.species = species
        self.organisms = []

    def add_organism(self, organism):
        self.organisms.append(organism)