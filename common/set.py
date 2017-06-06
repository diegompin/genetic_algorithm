__author__ = 'diegopinheiro'

from common.filter import Filter
from common.attribute import Attribute


class Set:

    def __init__(self):
        self.filters = []

    def size(self):
        pass

    def get_data(self):
        pass

    def find(self, criteria=Filter()):
        pass

    def subset(self, filter=Filter()):
        pass

    def get_thresholds(self, attribute=Attribute(), target_attribute=Attribute()):
        pass

    def calculate_set_target_distribution(self):
        pass

    def remove(self, index):
        pass

    def add_noise(self, level):
        pass
