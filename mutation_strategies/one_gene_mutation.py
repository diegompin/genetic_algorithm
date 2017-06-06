__author__ = 'diegopinheiro'

from mutation_strategies.mutation_strategy import MutationStrategy
from genetic_algorithms.individual import Individual
import random
import copy
import math


class OneGeneMutation(MutationStrategy):

    def __init__(self):
        MutationStrategy.__init__(self)

    def perform_mutation(self, individual):
        mutated_bit_string = copy.copy(individual.bit_string)
        mutated_bit_position = int(random.random() * len(mutated_bit_string))
        current_value = mutated_bit_string[mutated_bit_position]
        mutated_value = 0
        if type(current_value) == int:
            mutated_value = current_value ^ 1
        elif type(current_value) == float:
            mutated_value = math.floor(random.random() * 10)
        elif type(current_value) == str:
            size = int(current_value.split(":")[1])
            mutated_value = str(int(random.random() * size)) + ":" + str(size)
        # elif type(current_value == list):
        #     size = len(current_value)
        #     random_bit = int(random.random() * size)
        #     mutated_value = [0] * size
        #     mutated_value[random_bit] = 1
        mutated_bit_string[mutated_bit_position] = mutated_value

        mutated_individual = Individual(input_attributes=individual.input_attributes,
                                        output_attributes=individual.output_attributes,
                                        rule_size=individual.rule_size,
                                        bit_string=mutated_bit_string)
        # print(individual.print_individual())
        # print("MUTATED " + str(current_value) + " " + str(mutated_value))
        # print(mutated_individual.print_individual())
        return mutated_bit_string

    def is_output_attribute(self, individual, mutated_bit_position):
        return (mutated_bit_position + 1) % individual.rule_size == 0