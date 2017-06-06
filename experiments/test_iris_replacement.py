__author__ = 'diegopinheiro'

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


def run():

    print("\r\n\r\n\r\n")
    print("######## Experiment: testIrisReplacement ########")

    data_set_name = "iris"
    data_set_reader = SetReader(data_set_name)
    training_set = data_set_reader.read_train_set()
    test_set = data_set_reader.read_test_set()
    data_set_attributes = data_set_reader.attributes

    population_size = 50
    mutation_rate = 0.4
    max_number_iteration = 500
    initial_number_rules = 2
    use_elitism = True
    use_default = False

    min_number_rules = 2
    max_number_rules = 10

    stop_criterion = IterationStopCriterion(max_number_iteration=max_number_iteration)
    crossover_strategy = TwoPoint()
    fitness_function = AccuracySet(min_number_rules=min_number_rules, max_number_rules=max_number_rules, dataset=training_set)
    initialization_strategy = DataInitialization(data_set=training_set)
    mutation_strategy = OneGeneMutation()
    selection_strategy = FitnessProportionate()

    for i in range(1, 10):

        replacement_rate = float(i)/10.0

        print("######## Replacement rate: " + str(replacement_rate) + " ########")

        random.seed(0)
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
                                             attributes=data_set_attributes)
        genetic_algorithm.training_set = training_set
        genetic_algorithm.learn()
        accuracy_training_set = genetic_algorithm.calculate_accuracy(training_set)
        accuracy_test_set = genetic_algorithm.calculate_accuracy(test_set)

        print("Accuracy Training Set: " + str(accuracy_training_set))
        print("Accuracy Test Set: " + str(accuracy_test_set))