class Ecosystem:
    def __init__(self):
        self.populations = []

    def add_population(self, population):
        self.populations.append(population)

    def simulate_day(self):
        print("Симуляция дня")

        for population in self.populations:
            for organism in population.organisms:
                if organism.is_alive():
                    organism.eat(5)
                    print(
                        f"{organism.name}: "
                        f"энергия {organism.energy}"
                    )