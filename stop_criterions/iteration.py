__author__ = 'diegopinheiro'

from stop_criterions.stop_condition import StopCriterion
from genetic_algorithms.genetic_algorithm import GeneticAlgorithm


class IterationStopCriterion(StopCriterion):

    def __init__(self,
                 max_number_iteration=0):
        StopCriterion.__init__(self)
        self.max_number_iteration = max_number_iteration

    def has_finished(self, genetic_algorithm):
        return not genetic_algorithm.learning_iteration < self.max_number_iteration

    def use_validation(self):
        return False