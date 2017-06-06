__author__ = 'diegopinheiro'

from crossover_strategies.crossover_strategy import CrossoverStrategy
import random


class SinglePoint(CrossoverStrategy):

    def __init__(self):
        CrossoverStrategy.__init__(self)

    def get_offspring(self, parents=list(), rule_size=0):
        offspring = list()
        first_parent = parents[0]
        second_parent = parents[1]

        #TODO check
        crossover_point = int(random.random() * len(first_parent))

        first_child = first_parent[0:crossover_point] + second_parent[crossover_point:len(second_parent)]
        second_child = second_parent[0:crossover_point] + first_parent[crossover_point:len(first_parent)]

        offspring.append(first_child)
        offspring.append(second_child)

        return offspring