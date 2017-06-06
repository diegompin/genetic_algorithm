__author__ = 'diegopinheiro'

from common.attribute import Attribute
import math
import numpy


class AttributeConverter:

    @staticmethod
    def get_representation(attribute=Attribute(), category=None):
        number_representation = AttributeConverter.get_number_representation(attribute=attribute)
        category_index = attribute.categories.index(category)
        category_position = int(math.pow(2, category_index))
        return [int(bit) for bit in list(numpy.binary_repr(category_position, width=number_representation))]

    @staticmethod
    def get_number_representation(attribute=Attribute()):
        return len(attribute.categories)

    @staticmethod
    def get_attribute_category(attribute=Attribute,
                               representation=None):
        representation = "".join([str(i) for i in representation])
        category_position = int(representation, 2)
        category_index = 0
        if category_position == 1:
            category_position = 0
        if category_position != 0:
            category_index = int(math.log(category_position, 2))
        return attribute.categories[category_index]