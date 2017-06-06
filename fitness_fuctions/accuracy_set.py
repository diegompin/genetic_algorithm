__author__ = 'diegopinheiro'

from fitness_fuctions.fitness_function import FitnessFunction
from genetic_algorithms.individual import Individual
from common.set import Set
import math


class AccuracySet(FitnessFunction):

    def __init__(self,
                 min_number_rules=2,
                 max_number_rules=100,
                 dataset=Set()):
        FitnessFunction.__init__(self)
        self.min_number_rules = min_number_rules
        self.max_number_rules = max_number_rules
        self.dataset = dataset

    def calculate_fitness(self, individual):
        data_size = self.dataset.size()
        number_rules = len(individual.rule_set.rules)

        """
        prevent
        """

        individual_fitness = self.calculate_accuracy(individual)

        # if number_rules < self.min_number_rules or number_rules > self.max_number_rules:
        #     return 1
        #
        # rules_covers_correct = [0] * number_rules
        #
        # for register in self.dataset.get_data():
        #     for j in range(0, number_rules):
        #         rule = individual.rule_set.rules[j]
        #         if rule.is_antecedents_match(register):
        #             attributes_output = rule.consequents
        #             if not attributes_output is None:
        #                 corrected_classified = True
        #                 for p in range(0, len(individual.output_attributes)):
        #                     output_attribute = individual.output_attributes[p]
        #                     desired = register[output_attribute.index]
        #                     output = attributes_output[output_attribute]
        #                     if desired != output:
        #                         corrected_classified = False
        #                         break
        #                 if corrected_classified:
        #                     # rule.accuracy += 1
        #                     rules_covers_correct[j] += 1
        #                     break
        #                 else:
        #                     break
        #
        #
        # individual_fitness = 2
        # a = float(sum(rules_covers_correct))
        # r = float(number_rules)

        # individual_fitness += a * (1 + a / (r + r/(r+1) + a/(a+1)))

        return individual_fitness

    def calculate_accuracy(self, individual):
        correct_classifications = 0.0
        for register in self.dataset.get_data():
            attributes_output = individual.rule_set.classify(register)
            if not attributes_output is None:
                corrected_classified = True
                for i in range(0, len(individual.output_attributes)):
                    output_attribute = individual.output_attributes[i]
                    desired = register[output_attribute.index]
                    output = attributes_output[output_attribute]
                    if desired != output:
                        corrected_classified = False
                        break
                if corrected_classified:
                    correct_classifications += 1
        accuracy = correct_classifications / float(len(self.dataset.get_data()))
        return accuracy