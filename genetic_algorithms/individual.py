__author__ = 'diegopinheiro'

from common.attribute_converter import AttributeConverter
from genetic_algorithms.rule import Rule
from genetic_algorithms.rule_set import RuleSet
import random
import copy


class Individual():
    def __init__(self,
                 input_attributes,
                 output_attributes,
                 bit_string,
                 rule_size):
        self.fitness = 0
        self.input_attributes = input_attributes
        self.output_attributes = output_attributes
        self.bit_string = bit_string
        self.rule_size = rule_size
        self.rule_set = RuleSet(input_attributes=self.input_attributes,
                                output_attributes=self.output_attributes,
                                rule_size=self.rule_size,
                                bit_string=self.bit_string)

    def set_bit_string(self, bit_string):
        self.bit_string = bit_string
        self.rule_set = RuleSet(input_attributes=self.input_attributes,
                                output_attributes=self.output_attributes,
                                rule_size=self.rule_size,
                                bit_string=self.bit_string)

    def print_individual(self):
        return self.rule_set.print_rules()