from operator import attrgetter

__author__ = 'diegopinheiro'

from selection_strategies.selection_strategy import SelectionStrategy
import random
from operator import attrgetter


class TournamentSelection(SelectionStrategy):

    def __init__(self,
                 probability):
        SelectionStrategy.__init__(self)
        self.probability = probability
        self.name = "TournamentSelection"

    def select_individual(self, genetic_algorithm):
        selected_individual = None
        first_index = int(random.random() * genetic_algorithm.population_size)
        second_index = int(random.random() * genetic_algorithm.population_size)

        first_individual = genetic_algorithm.population[first_index]
        second_individual = genetic_algorithm.population[second_index]

        individuals = list()
        individuals.append(first_individual)
        individuals.append(second_individual)

        individuals = sorted(individuals, key=attrgetter("fitness"))

        if random.random() < self.probability:
            selected_individual = individuals[1]
        else:
            selected_individual = individuals[1]

        return selected_individual