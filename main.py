from ecosystem import Organism
from population import Population
from population import Ecosystem

eco = Ecosystem()

rabbits = Population("Зайцы")

rabbit1 = Organism("Заяц 1", 20)
rabbit2 = Organism("Заяц 2", 15)

rabbits.add_organism(rabbit1)
rabbits.add_organism(rabbit2)

eco.add_population(rabbits)

eco.simulate_day()