__author__ = 'diegopinheiro'

from common.attribute_converter import AttributeConverter
from common.attribute import Attribute
from common.float_converter_2 import FloatConverter2


class Rule():

    def __init__(self,
                 input_attributes=list(),
                 output_attributes=list(),
                 bit_string=list()):
        self.input_attributes = input_attributes
        self.output_attributes = output_attributes
        self.bit_string = bit_string
        self.antecedents = dict()
        self.consequents = dict()
        self.accuracy = 0
        self.coverage = 0
        self.initialize_rule()

    def initialize_rule(self):
        attribute_index = 0
        antecedents = dict()
        for attribute in self.input_attributes:
            antecedent = list()
            if attribute.type == Attribute.TYPE_DISCRETE:
                attribute_number_bits = AttributeConverter.get_number_representation(attribute)
                attribute_bits = self.bit_string[attribute_index:attribute_index+attribute_number_bits]
                for bit_position in range(0, len(attribute_bits)):
                    if attribute_bits[bit_position] == 1:
                        category_bits = [0] * len(attribute_bits)
                        category_bits[bit_position] = 1
                        antecedent.append(AttributeConverter.get_attribute_category(attribute,category_bits))
                antecedents[attribute] = antecedent
                attribute_index += attribute_number_bits

            elif attribute.type == Attribute.TYPE_CONTINUOUS:
                attribute_number_bits = FloatConverter2.get_number_representation()
                attribute_bits_low = FloatConverter2.get_value(self.bit_string[attribute_index:attribute_index+attribute_number_bits])
                attribute_bits_high = FloatConverter2.get_value(self.bit_string[attribute_index+attribute_number_bits:attribute_index+2*attribute_number_bits])

                antecedents[attribute] = [attribute_bits_low, attribute_bits_high]
                attribute_index += 2 * attribute_number_bits

        consequents = dict()
        for attribute in self.output_attributes:
            # attribute_number_bits = AttributeConverter.get_number_representation(attribute)
            attribute_bits = int(self.bit_string[attribute_index][0])
            # for bit_position in range(0, len(attribute_bits)):
            #     if attribute_bits[bit_position] == 1:
            #         consequents[attribute] = AttributeConverter.get_attribute_category(attribute, attribute_bits)
                    # break
            consequents[attribute] = attribute.categories[attribute_bits]
            attribute_index += 1


        self.antecedents = antecedents
        self.consequents = consequents

    def is_valid(self):
        if len(self.consequents.keys()) != len(self.output_attributes) or len(self.antecedents.keys()) != len(self.input_attributes):
            return False

        is_valid = True
        for a in self.antecedents.keys():
            if a.type == Attribute.TYPE_DISCRETE:
                if len(self.antecedents[a]) == 0:
                    is_valid = False
                    break
            elif a.type == Attribute.TYPE_CONTINUOUS:
                low_boundary = self.antecedents[a][0]
                high_boundary = self.antecedents[a][1]
                if low_boundary == float("Nan") or high_boundary == float("Nan"):
                    is_valid = False
                    break

                if low_boundary > high_boundary:
                    is_valid = False
                    break

        return is_valid

    def is_antecedents_match(self, register):
        is_applied = True
        for attribute in self.antecedents.keys():
            value = self.antecedents[attribute]
            if attribute.type == Attribute.TYPE_DISCRETE:
                if not value.__contains__(register[attribute.index]):
                    is_applied = False
                    break
            elif attribute.type == Attribute.TYPE_CONTINUOUS:
                low_boundary = value[0]
                high_boundary = value[1]
                desired = float(register[attribute.index])
                if not low_boundary <= desired <= high_boundary:
                    is_applied = False
                    break
        return is_applied

    def print_rule(self):
        rule_string = ""
        for attribute in self.antecedents:
            rule_string = rule_string.replace("?", "^")
            if attribute.type == Attribute.TYPE_DISCRETE:
                rule_string += attribute.name + " in " + str(self.antecedents[attribute]) + " ? "
            elif attribute.type == Attribute.TYPE_CONTINUOUS:
                rule_string += str(self.antecedents[attribute][0]) + " <= " + attribute.name + " <= " + str(self.antecedents[attribute][1]) + " ? "
        rule_string = rule_string.replace("?", "=>")

        for attribute in self.consequents:
            rule_string = rule_string.replace("?", "^")
            if attribute.type == Attribute.TYPE_DISCRETE:
                rule_string += attribute.name + " = " + str(self.consequents[attribute]) + " "
            elif attribute.type == Attribute.TYPE_CONTINUOUS:
                rule_string += str(self.consequents[attribute][0]) + " <= " + attribute.name + " <= " + str(self.consequents[attribute][1]) + " ? "
        # rule_string = rule_string.replace("?", "=>")


        # rule_string += " " + str(self.target_distribution)
        return rule_string





