__author__ = 'diegopinheiro'

from crossover_strategies.two_point import TwoPoint

crossover = TwoPoint()
parents = list()
rule_size = 5

parents.append([1,0,0,1,1,1,1,1,0,0])
parents.append([0,1,1,1,0,1,0,0,1,0])

offspring = crossover.get_offspring(parents, rule_size)

for child in offspring:
    print(child)

