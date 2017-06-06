__author__ = 'diegopinheiro'

from crossover_strategies.crossover_strategy import CrossoverStrategy
import random


class TwoPoint(CrossoverStrategy):

    def __init__(self):
        CrossoverStrategy.__init__(self)

    def get_offspring(self, parents, rule_size):
        offspring = list()

        first_parent_bit_string = parents[0]
        second_parent_bit_string = parents[1]

        first_parent_first_point = 0
        first_parent_second_point = 0

        leftmost_rule_distance = 0
        rightmost_rule_distance = 0

        while True:
            random_numbers = [random.random(), random.random()]

            first_parent_first_point = int(min(random_numbers) * len(first_parent_bit_string))
            first_parent_second_point = int(max(random_numbers) * len(first_parent_bit_string))

            leftmost_rule_distance = first_parent_first_point % rule_size
            rightmost_rule_distance = first_parent_second_point % rule_size

            if leftmost_rule_distance <= rightmost_rule_distance:
                break

        allowed_points = self.__calculate_allowed_points__(leftmost_rule_distance,
                                                           rightmost_rule_distance,
                                                           second_parent_bit_string,
                                                           rule_size)

        chosen_points = allowed_points[int(len(allowed_points) * random.random())]

        second_parent_first_point = chosen_points[0]
        second_parent_second_point = chosen_points[1]

        first_child = first_parent_bit_string[0:first_parent_first_point] + second_parent_bit_string[second_parent_first_point:second_parent_second_point] + first_parent_bit_string[first_parent_second_point:len(first_parent_bit_string)]
        second_child = second_parent_bit_string[0:second_parent_first_point] + first_parent_bit_string[first_parent_first_point:first_parent_second_point] + second_parent_bit_string[second_parent_second_point:len(second_parent_bit_string)]

        offspring.append(first_child)
        offspring.append(second_child)

        return offspring

    def __calculate_allowed_points__(self, leftmost_rule_distance, rightmost_rule_distance, second_parent, rule_size):
        allowed_points = list()
        i = leftmost_rule_distance
        j = rightmost_rule_distance
        while i <= len(second_parent):
            while j < len(second_parent):
                allowed_points.append([i, j])
                j += rule_size
            i += rule_size
            j = i + (rightmost_rule_distance-leftmost_rule_distance)
        return allowed_points