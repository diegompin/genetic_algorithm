__author__ = 'diegopinheiro'

from genetic_algorithms.individual import Individual
from stop_criterions.stop_condition import StopCriterion
from selection_strategies.selection_strategy import SelectionStrategy
from crossover_strategies.crossover_strategy import CrossoverStrategy
from fitness_fuctions.fitness_function import FitnessFunction
from initialization_strategies.initialization_strategy import InitializationStrategy
from mutation_strategies.mutation_strategy import MutationStrategy
from common.attribute_converter import AttributeConverter
from common.float_converter_2 import FloatConverter2
from genetic_algorithms.rule import Rule
from genetic_algorithms.rule_set import RuleSet
import random
from operator import attrgetter
from common.attribute import Attribute
from common.writer import  Writer


class GeneticAlgorithm:

    def __init__(self,
                 population_size=0,
                 replacement_rate=0,
                 mutation_rate=0,
                 use_elitism=0,
                 initial_number_rules=0,
                 use_default=True,
                 stop_criterion=StopCriterion(),
                 selection_strategy=SelectionStrategy(),
                 crossover_strategy=CrossoverStrategy(),
                 fitness_function=FitnessFunction(),
                 initialization_strategy=InitializationStrategy(),
                 mutation_strategy=MutationStrategy(),
                 attributes=list(),
                 writer=None,
                 test_set=None):
        self.learning_iteration = 0
        self.population_size = population_size
        self.replacement_rate = replacement_rate
        self.mutation_rate = mutation_rate
        self.use_elitism = use_elitism
        self.use_default_dafaut = use_default
        self.initial_number_rules = initial_number_rules
        self.stop_criterion = stop_criterion
        self.selection_strategy = selection_strategy
        self.crossover_strategy = crossover_strategy
        self.fitness_function = fitness_function
        self.initialization_strategy = initialization_strategy
        self.mutation_strategy = mutation_strategy
        self.attributes = attributes
        self.input_attributes = self.init_input_attributes(attributes)
        self.output_attributes = self.init_output_attributes(attributes)
        self.population = list()
        self.rule_size = self.calculate_rule_size()
        self.training_set = None
        self.test_set = test_set
        self.writer = writer

    def learn(self):
        print("Learning...")
        self.initialize()
        while not self.stop_criterion.has_finished(self):
            self.evaluate_fitness()
            self.learning_iteration += 1
            # print("Iteration: " + str(self.learning_iteration))
            # print("Population Size: " + str(len(self.population)))
            best_individual = self.get_best_individual()
            # print(best_individual.fitness)
            # print("Max rules: " + str(len(best_individual.rule_set.rules)))
            # print(self.calculate_accuracy(dataset=self.training_set))

            # print(best_individual.print_individual())
            new_generation = list()
            selection_rate = 1 - self.replacement_rate
            number_selected_individuals = int(round(selection_rate * self.population_size))
            if self.use_elitism:
                number_selected_individuals -= 1
            number_parents = int(round((self.replacement_rate * self.population_size)/2))
            number_mutated_population = int(self.mutation_rate * self.population_size)
            self.perform_selection(number_selected_individuals, new_generation)
            self.perform_crossover(number_parents, new_generation)
            self.perform_mutation(number_mutated_population, new_generation)
            if self.use_elitism:
                best_individual = self.get_best_individual()
                new_generation.append(best_individual)
            self.population = new_generation
            self.writer.write(self.learning_iteration, self.calculate_accuracy(self.training_set), self.calculate_accuracy(self.test_set), self.population)
        if self.use_default_dafaut:
            self.set_default_rule()
        self.writer.close()

    def set_default_rule(self):
        best_individual = self.get_best_individual()
        best_individual.rule_set.default_classification = best_individual.rule_set.rules[0].consequents

    # def perform_elitism(self, elite_number, new_generation):
    #     sorted_population = sorted(self.population, reverse=False, key=attrgetter("fitness"))
    #     for i in range(0, elite_number):
    #         elite_individual = sorted_population.pop()
    #         new_generation.append(elite_individual)

    def perform_selection(self, number_selected_individuals, new_generation):
        for i in range(0, number_selected_individuals):
            selected_individual = self.selection_strategy.select_individual(genetic_algorithm=self)
            new_generation.append(selected_individual)

    def perform_crossover(self, number_parents, new_generation):
        for i in range(0, number_parents):
            offspring_bit_string = list()
            parents = list()
            while True:
                parents = list()
                first_parent = self.selection_strategy.select_individual(genetic_algorithm=self).bit_string
                second_parent = None
                while True:
                    second_parent = self.selection_strategy.select_individual(genetic_algorithm=self).bit_string
                    if first_parent != second_parent:
                        break
                parents.append(first_parent)
                parents.append(second_parent)
                offspring_bit_string = self.crossover_strategy.get_offspring(parents, self.rule_size)
                valid_offspring = True
                for child_bitstring in offspring_bit_string:
                    rule_set = RuleSet(input_attributes=self.input_attributes,
                                       output_attributes=self.output_attributes,
                                       bit_string=child_bitstring,
                                       rule_size=self.rule_size)
                    if not rule_set.is_valid():
                        valid_offspring = False
                        break
                if valid_offspring:
                    break

            for child_bit_string in offspring_bit_string:
                new_generation.append(Individual(bit_string=child_bit_string,
                                                 input_attributes=self.input_attributes,
                                                 output_attributes=self.output_attributes,
                                                 rule_size=self.rule_size))

            # print("###################CROSSOVER #########################")
            # for parent in parents:
            #     individual = Individual(input_attributes=self.input_attributes,
            #                             output_attributes=self.output_attributes,
            #                             rule_size=self.rule_size,
            #                             bit_string=parent)
            #     print(individual.print_individual())
            #     print(self.fitness_function.calculate_fitness(individual))
            #
            # for child_bit_string in offspring_bit_string:
            #     child = Individual(bit_string=child_bit_string,
            #                        input_attributes=self.input_attributes,
            #                        output_attributes=self.output_attributes,
            #                        rule_size=self.rule_size)
            #     print(child.print_individual())
            #     print(self.fitness_function.calculate_fitness(child))

    def perform_mutation(self, number_mutated_population, new_generation):
        for i in range(0, number_mutated_population):
            while True:
                individual_index = int(random.random() * len(new_generation))
                individual = new_generation[individual_index]
                mutated_individual_bit_string = self.mutation_strategy.perform_mutation(individual)
                mutated_rule = RuleSet(input_attributes=self.input_attributes,
                                       output_attributes=self.output_attributes,
                                       bit_string=mutated_individual_bit_string,
                                       rule_size=self.rule_size)
                if mutated_rule.is_valid():
                    new_generation[individual_index] = Individual(input_attributes=self.input_attributes,
                                                                  output_attributes=self.output_attributes,
                                                                  bit_string=mutated_individual_bit_string,
                                                                  rule_size=self.rule_size)
                    break

    def evaluate_fitness(self):
        for individual in self.population:
            fitness = self.fitness_function.calculate_fitness(individual)
            individual.fitness = fitness

    def initialize(self):
        self.population = self.initialization_strategy.get_initial_population(genetic_algorithm=self)

    def init_input_attributes(self, attributes):
        non_target_attributes = list()
        for attribute in attributes:
            if not attribute.is_target:
                non_target_attributes.append(attribute)
        return non_target_attributes

    def init_output_attributes(self, attributes):
        output_attributes = list()
        for attribute in attributes:
            if attribute.is_target:
                output_attributes.append(attribute)
        return output_attributes

    def calculate_rule_size(self):
        rule_size = 0

        for attribute in self.input_attributes:
            attribute_number_bits = 0
            if attribute.type == Attribute.TYPE_DISCRETE:
                attribute_number_bits = AttributeConverter.get_number_representation(attribute)
            elif attribute.type == Attribute.TYPE_CONTINUOUS:
                # attribute_number_bits = 2
                attribute_number_bits = FloatConverter2.get_number_representation() * 2
            rule_size += attribute_number_bits
        rule_size += len(self.output_attributes)
        return rule_size

    def calculate_accuracy(self, dataset):
        correct_classifications = 0.0
        individual = self.get_best_individual()
        for register in dataset.get_data():
            attributes_output = individual.rule_set.classify(register)
            if not attributes_output is None:
                corrected_classified = True
                for i in range(0, len(individual.output_attributes)):
                    output_attribute = individual.output_attributes[i]
                    desired = register[output_attribute.index]
                    output = attributes_output[output_attribute]
                    if desired != output:
                        corrected_classified = False
                        break
                if corrected_classified:
                    correct_classifications += 1
        accuracy = correct_classifications / len(dataset.get_data())
        return accuracy

    def get_best_individual(self):
        sorted_population = sorted(self.population, reverse=False, key=attrgetter("fitness"))
        best_individual = sorted_population.pop()
        return best_individual
