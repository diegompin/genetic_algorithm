__author__ = 'diegopinheiro'

from selection_strategies.selection_strategy import SelectionStrategy
from genetic_algorithms.genetic_algorithm import GeneticAlgorithm
import random


class FitnessProportionate(SelectionStrategy):

    def __init__(self):
        SelectionStrategy.__init__(self)
        self.name = "FitnessProportionate"


    def select_individual(self, genetic_algorithm):
        selected_individual = None
        max = sum([individual.fitness for individual in genetic_algorithm.population])

        pick = random.uniform(0, max)
        current = 0
        for individual in genetic_algorithm.population:
            current += individual.fitness
            if current > pick:
                selected_individual = individual
                break

        if selected_individual is None:
            selected_individual_index = int(random.random() * genetic_algorithm.population_size)
            selected_individual = genetic_algorithm.population[selected_individual_index]

        return selected_individual

