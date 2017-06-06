__author__ = 'diegopinheiro'

from initialization_strategies.initialization_strategy import InitializationStrategy
from common.attribute import Attribute
from common.attribute_converter import AttributeConverter
from common.float_converter_2 import FloatConverter2
from genetic_algorithms.individual import Individual
import random


class DataInitialization(InitializationStrategy):

    def __init__(self, data_set):
        InitializationStrategy.__init__(self)
        self.data_set = data_set

    def get_initial_population(self, genetic_algorithm):
        initial_population = list()
        for i in range(0, genetic_algorithm.population_size):
            bit_string = self.get_bit_string_from_data(genetic_algorithm)
            new_individual = Individual(input_attributes=genetic_algorithm.input_attributes,
                                        output_attributes=genetic_algorithm.output_attributes,
                                        bit_string=bit_string,
                                        rule_size=genetic_algorithm.rule_size)
            initial_population.append(new_individual)
        return initial_population

    def get_bit_string_from_data(self, genetic_algorithm):
        bit_string = list()
        for i in range(0, genetic_algorithm.initial_number_rules):
            random_data_index = int(random.random() * len(self.data_set.get_data()))
            random_data = self.data_set.get_data()[random_data_index]
            data_bit_string = self.get_data_bit_string(genetic_algorithm, random_data)
            bit_string.extend(data_bit_string)
        return bit_string

    def get_data_bit_string(self, genetic_algorithm, random_data, output_marker=True):
        data_bit_string = list()
        for attribute in genetic_algorithm.input_attributes:
            if attribute.type == Attribute.TYPE_DISCRETE:
                attribute_bits = AttributeConverter.get_representation(attribute=attribute,
                                                                       category=random_data[attribute.index])
                data_bit_string.extend(attribute_bits)
            elif attribute.type == Attribute.TYPE_CONTINUOUS:
                value = float(random_data[attribute.index])
                low = FloatConverter2.get_genes(float(value))
                high = FloatConverter2.get_genes(float(value))

                data_bit_string.extend(low)
                data_bit_string.extend(high)

        for attribute in genetic_algorithm.output_attributes:
            # attribute_bits = AttributeConverter.get_representation(attribute=attribute,
            #                                                        category=random_data[attribute.index])
            attribute_bits = attribute.categories.index(random_data[attribute.index])
            gene = str(attribute_bits) + ":" + str(len(attribute.categories)-1)
            data_bit_string.append(gene)
        return data_bit_string

