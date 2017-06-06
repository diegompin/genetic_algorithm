Diego Pinheiro Silva
PhD Student in Computer Sciences
Florida Institute of Technology


****************** TO RUN ******************

To run the requested test scripts:

- Get into the Homework4 directory and execute the following command

python gui/run_tests.py

********************************************

****************** OPTIONAL ******************
Get into the Homework4 directory and execute the following command

export PYTHONPATH=$PYTHONPATH:.

**********************************************


****************** CONTENTS ******************

- common: common package
----- attribute.py: encapsulates the concept of Attribute to be reused by other modules
----- attribute_converter.py: encapsulates the 1-of-n representation of discrete attributes
----- float_converter_2.py: converts floats and genes and otherwise
----- criteria.py: encapsulates a search criteria in order to filter a data set
----- my_data_set.py: object data set implementation of set.py
----- set.py: base class to be implemented by data set providers
----- set_reader: reads attributes and data from training and test sets
-----
- crossover_strategies: crossover package
----- crossover_strategy.py: base class for crossover strategy
----- single_point.py: implements single point crossover
----- two_point.py: implements two point crossover
- data_files: contains the data files for all experiments
- experiments: experiments package
----- test_iris.py: describes the experiment testIris
----- test_tennis.py: describes the experiment testTennis
----- test_iris_replacement: describes the experiment testIrisReplacement
----- test_iris_selection: describes the experiment testIrisSelection
- fitness_function: fitness functions package
----- fitness_function: base class for all fitness functions
----- accuracy_set: implements fitness of an individual based on its rules
- genetic_algorithms: genetic_algorithm main package
----- genetic_algorithm: represents the main class where the operators are called
----- individual: encapsulates an chromosome with bitstring and set of rules
----- rule: represents the antecedents and consequents of a biststring
----- rule_set: represents a set of rules of an individual
- gui: graphical user interface package
----- run_tests.py: script that runs all experiments in experiments package
- initialization_strategies: initialization strategies package
-----
- stop_conditions: stop condition package
----- iteration: stop condition for fixed max iteration number
----- stop_condition: base class for all stop condition

**********************************************