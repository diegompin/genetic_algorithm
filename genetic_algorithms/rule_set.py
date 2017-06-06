__author__ = 'diegopinheiro'

from operator import attrgetter
from genetic_algorithms.rule import Rule


class RuleSet:

    def __init__(self,
                 input_attributes,
                 output_attributes,
                 rule_size,
                 bit_string):
        self.input_attributes = input_attributes
        self.output_attributes = output_attributes
        self.rule_size = rule_size
        self.bit_string = bit_string
        self.rules = list()
        self.default_classification = None
        self.initialize()

    def initialize(self):
        # for bit_string in self.__bit_string__:
        rules_bit_string = list(self.bit_string[i:i+self.rule_size] for i in range(0, len(self.bit_string), self.rule_size))
        for rule_bit_string in rules_bit_string:
            rule = Rule(input_attributes=self.input_attributes,
                        output_attributes=self.output_attributes,
                        bit_string=rule_bit_string)
            self.rules.append(rule)

    def classify(self, example):
        classification = None
        for rule in self.rules:
            if rule.is_antecedents_match(example):
                classification = rule.consequents
                break
        if classification is None:
            classification = self.default_classification
        return classification

    def is_valid(self):
        is_valid = True
        for rule in self.rules:
            if not rule.is_valid():
                is_valid = False
                break
        return is_valid

    def print_rules(self):
        rules_print = ""
        for rule in self.rules:
            rules_print += rule.print_rule() + "\r\n"
        if not self.default_classification is None:
            rules_print += "Default rule => " + str(self.default_classification.values())
        return rules_print