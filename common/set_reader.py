__author__ = 'diegopinheiro'

from common.my_data_set import MyDataSet
from common.attribute import Attribute


class SetReader:

    PATH = "../data_files/"
    CONTINUOUS = "continuous"

    def __init__(self, name):
        self.name = name
        self.attributes = self.get_attributes()

    def read_train_set(self):
        return self.read_set("train")

    def read_test_set(self):
        return self.read_set("test")

    def read_set(self, type):
        f = open(name=self.PATH + self.name + "-" + type + ".txt")
        train_set = MyDataSet(self.attributes)
        for line in f:
            words = line.split()
            train_set.data.append(words)
        return train_set

    def get_attributes(self):
        attributes = []
        f = open(name=self.PATH + self.name + "-attr.txt")
        is_target_attribute_line = False
        attribute_index = 0
        attribute_type = Attribute.TYPE_DISCRETE
        for line in f:
            if line == "\n":
                is_target_attribute_line = True
                continue
            words = line.split()
            attribute_name = words[0]
            if words[1] == self.CONTINUOUS:
                attribute_type = Attribute.TYPE_CONTINUOUS
                categories = list([True, False])
            else:
                attribute_type = Attribute.TYPE_DISCRETE
                categories = []
                for word in words[1:]:
                    categories.append(word)

            attribute = Attribute(name=attribute_name,
                                  type=attribute_type,
                                  is_target=is_target_attribute_line,
                                  index=attribute_index,
                                  categories=categories)
            attributes.append(attribute)
            attribute_index += 1

        return attributes

