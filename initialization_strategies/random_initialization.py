__author__ = 'diegopinheiro'

from initialization_strategies.initialization_strategy import InitializationStrategy
from genetic_algorithms.individual import Individual
from genetic_algorithms.rule import Rule
from common.attribute import Attribute
from common.float_converter_2 import FloatConverter2
import random
from common.attribute_converter import AttributeConverter


class RandomInitialization(InitializationStrategy):

    def __init__(self):
        InitializationStrategy.__init__(self)

    def get_initial_population(self, genetic_algorithm):
        initial_population = list()
        for i in range(0, genetic_algorithm.population_size):
            bit_string = self.get_bit_string(genetic_algorithm)
            new_individual = Individual(input_attributes=genetic_algorithm.input_attributes,
                                        output_attributes=genetic_algorithm.output_attributes,
                                        bit_string=bit_string,
                                        rule_size=genetic_algorithm.rule_size)
            initial_population.append(new_individual)
        return initial_population

    def get_bit_string(self, genetic_algorithm):
        rules_bit_string = list()
        number_rules = genetic_algorithm.initial_number_rules
        for i in range(0, number_rules):
            while True:
                bit_string = (self.get_random_bits(genetic_algorithm))
                rule = Rule(genetic_algorithm.input_attributes,
                            genetic_algorithm.output_attributes,
                            bit_string)
                if rule.is_valid():
                    rules_bit_string.extend(bit_string)
                    break
        return rules_bit_string

    def get_random_bits(self, genetic_algorithm):
        bits = list()
        for attribute in genetic_algorithm.input_attributes:
            if attribute.type == Attribute.TYPE_DISCRETE:
                low_genes = [0] * AttributeConverter.get_number_representation()
                size = len(attribute.categories)
                for i in range(0, size):
                    if random.random() < 0.5:
                        low_genes[0] = 1
                bits.extend(low_genes)

            elif attribute.type == Attribute.TYPE_CONTINUOUS:
                low_random = random.random()
                high_random = random.random()
                low_genes = FloatConverter2.get_genes(low_random)
                high_genes = FloatConverter2.get_genes(high_random)
                bits.extend(low_genes)
                bits.extend(high_genes)

        for attribute in genetic_algorithm.output_attributes:
            size = len(attribute.categories)-1
            random_class = int(random.random() * len(attribute.categories))
            genes = str(random_class) + ":" + str(size)
            bits.append(genes)
        return bits
