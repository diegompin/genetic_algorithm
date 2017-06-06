__author__ = 'diegopinheiro'

class Attribute:

    TYPE_DISCRETE = 0
    TYPE_CONTINUOUS = 1

    def __init__(self,
                 name=None,
                 type=TYPE_CONTINUOUS,
                 is_target=False,
                 index=0,
                 categories=list([True, False]),
                 thereshold=0):
        self.name = name
        self.type = type
        self.is_target = is_target
        self.index = index
        self.categories = categories
        self.thereshold = thereshold