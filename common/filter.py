__author__ = 'diegopinheiro'

from common.criteria import Criteria

class Filter:

    def __init__(self):
        self.criterias = []

    def add_criteria(self, criteria=Criteria()):
        self.criterias.append(criteria)