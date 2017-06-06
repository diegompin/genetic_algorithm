__author__ = 'diegopinheiro'

from selection_strategies.selection_strategy import SelectionStrategy
from operator import attrgetter
import random


class RankSelection(SelectionStrategy):

    def __init__(self):
        SelectionStrategy.__init__(self)
        self.name = "RankSelection"

    def select_individual(self, genetic_algorithm):
        selected_individual = None
        sorted_population = sorted(genetic_algorithm.population, reverse=False, key=attrgetter("fitness"))
        size = len(sorted_population)
        max = size * (size + 1)/2
        pick = random.uniform(0, max)
        current = 0
        for i in range(0, size):
            rank = size - i
            individual = sorted_population[rank-1]
            current += rank
            if current > pick:
                selected_individual = individual
                break

        if selected_individual is None:
            selected_individual_index = int(random.random() * genetic_algorithm.population_size)
            selected_individual = genetic_algorithm.population[selected_individual_index]

        return selected_individual
