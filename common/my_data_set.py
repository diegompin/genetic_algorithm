__author__ = 'diegopinheiro'

from operator import itemgetter
import random
import copy
from common.set import Set
from common.filter import Filter
from common.attribute import Attribute
from common.criteria import Criteria


class MyDataSet(Set):

    def __init__(self, attributes):
        Set.__init__(self)
        self.data = list()
        self.attributes = attributes

    def size(self):
        return float(len(self.data))

    def get_data(self):
        return self.data

    def find(self, filter=Filter()):
        data_found = []
        for register in self.data:
            include_register = True
            for criteria in filter.criterias:
                if criteria.attribute.type == Attribute.TYPE_DISCRETE:
                    if not register[criteria.attribute.index] == criteria.value:
                        include_register = False
                        break
                elif criteria.attribute.type == Attribute.TYPE_CONTINUOUS:
                    if not (float(register[criteria.attribute.index]) < criteria.attribute.thereshold) == criteria.value:
                        include_register = False
                        break
            if include_register:
                data_found.append(register)
        return data_found

    def subset(self, filter=Filter()):
        subset = MyDataSet(self.attributes)
        subset_data = self.find(filter)
        subset.data = subset_data
        return subset

    def get_thresholds(self, attribute=Attribute(), target_attribute=Attribute()):
        sorterd_data = sorted(self.data, key=itemgetter(attribute.index, target_attribute.index))
        thresholds = []
        previous_value = 0.0
        previous_target = sorterd_data[0][target_attribute.index]
        for register in sorterd_data:
            current_value = float(register[attribute.index])
            current_target = register[target_attribute.index]
            if not current_target == previous_target and not current_value == previous_value:
                thresholds.append((current_value + previous_value) / 2)
            previous_value = current_value
            previous_target = current_target
        return thresholds

    def calculate_set_target_distribution(self):
        target_attribute = self.attributes[len(self.attributes) - 1]
        target_distribution = []
        set_count = self.size()
        for target_class in target_attribute.categories:
            proportion = 0
            filter = Filter()
            criteria = Criteria(attribute=target_attribute,
                                value=target_class)
            filter.add_criteria(criteria)
            data_found = float(len(self.find(filter)))
            if not set_count == 0:
                proportion = data_found/set_count
            target_distribution.append(proportion)
        return target_distribution

    def remove(self, index):
        self.data.pop(index)

    def add_noise(self, percentage):
        corrupted_registers_number = percentage * len(self.data)
        random.seed(0)
        while corrupted_registers_number > 0:
            index = int(random.random() * len(self.data))
            corrupted_register = self.data[index]
            corrupter_category = self.get_corrupted_category(corrupted_register)
            corrupted_register[len(self.attributes) - 1] = corrupter_category
            corrupted_registers_number -= 1

    def get_corrupted_category(self, register):
        possible_categories = copy.copy(self.attributes[len(self.attributes) - 1].categories)
        register_category = register[len(self.attributes) - 1]
        possible_categories.remove(register_category)
        index = int(random.random() * len(possible_categories))
        return possible_categories[index]