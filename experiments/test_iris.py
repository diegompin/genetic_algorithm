__author__ = 'diegopinheiro'


from genetic_algorithms.genetic_algorithm import GeneticAlgorithm
from stop_criterions.iteration import IterationStopCriterion
from common.set_reader import SetReader
from selection_strategies.fitness_proportionate import FitnessProportionate
from selection_strategies.tournament_selection import TournamentSelection
from selection_strategies.rank_selection import RankSelection
from crossover_strategies.single_point import SinglePoint
from crossover_strategies.two_point import TwoPoint
from fitness_fuctions.accuracy_set import AccuracySet
from initialization_strategies.random_initialization import RandomInitialization
from initialization_strategies.data_initialization import DataInitialization
from mutation_strategies.one_gene_mutation import OneGeneMutation
import random
from common.writer import  Writer
from common.attribute import Attribute
from common.attribute_converter import AttributeConverter
from common.float_converter_2 import FloatConverter2

import sys


def main(output_path):

    print("\r\n\r\n\r\n")
    print("######## Experiment: testIris ########")

    data_set_name = "iris"
    data_set_reader = SetReader(data_set_name)
    training_set = data_set_reader.read_train_set()
    test_set = data_set_reader.read_test_set()
    data_set_attributes = data_set_reader.attributes


    population_size = 100

    replacement_rate = 0.3

    max_number_iteration = 3000

    use_elitism = True
    use_default = True

    initial_number_rules = 4
    min_number_rules = 4
    max_number_rules = 4

    stop_criterion = IterationStopCriterion(max_number_iteration=max_number_iteration)
    selection_strategy = FitnessProportionate()
    # selection_strategy = TournamentSelection(probability=0.7)
    # selection_strategy = RankSelection()
    # crossover_strategy = TwoPoint()
    crossover_strategy = SinglePoint()
    fitness_function = AccuracySet(min_number_rules=min_number_rules, max_number_rules=max_number_rules, dataset=training_set)
    initialization_strategy = DataInitialization(data_set=training_set)
    mutation_strategy = OneGeneMutation()




    # TODO remove fixed seed
    # random.seed(0)


    for rule in [2,3,4]:
        for mutation_rate in [.01, .05, .1, .2, .5]:
            print("rule:%d mutation:%.2f" % (rule, mutation_rate) )
            for run in range(0,30):
                initial_number_rules = rule


                genetic_algorithm = GeneticAlgorithm(population_size=population_size,
                                                     replacement_rate=replacement_rate,
                                                     mutation_rate=mutation_rate,
                                                     use_elitism=use_elitism,
                                                     use_default=use_default,
                                                     initial_number_rules=initial_number_rules,
                                                     stop_criterion=stop_criterion,
                                                     selection_strategy=selection_strategy,
                                                     crossover_strategy=crossover_strategy,
                                                     fitness_function=fitness_function,
                                                     initialization_strategy=initialization_strategy,
                                                     mutation_strategy=mutation_strategy,
                                                     attributes=data_set_attributes,

                                                     test_set=test_set)


                dimensions = genetic_algorithm.calculate_rule_size() * initial_number_rules
                writer = Writer('ga_iris_%d_%d_%d_%s_%s_%.2f_%.2f_%d.with_positions' % (population_size, dimensions, initial_number_rules,
                                                                           str.lower(selection_strategy.__class__.__name__),
                                                                           str.lower(crossover_strategy.__class__.__name__),
                                                                                        mutation_rate,
                                                                                        replacement_rate,
                                                                                        run))



                genetic_algorithm.writer = writer

                genetic_algorithm.training_set = training_set
                genetic_algorithm.learn()
                accuracy_training_set = genetic_algorithm.calculate_accuracy(training_set)
                accuracy_test_set = genetic_algorithm.calculate_accuracy(test_set)

                print(genetic_algorithm.get_best_individual().print_individual())
                print("Accuracy Training Set: " + str(accuracy_training_set))
                print("Accuracy Test Set: " + str(accuracy_test_set))



if __name__ == "__main__":
    output_path = sys.argv[1]

    main(output_path )
