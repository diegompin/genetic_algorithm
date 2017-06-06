__author__ = 'diegopinheiro'

from common.attribute import Attribute


class Criteria:

    def __init__(self,
                 attribute=Attribute(),
                 value=None):
        self.attribute = attribute
        self.value = value