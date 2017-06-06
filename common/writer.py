


class Writer(object):


    def __init__(self, name):
        self.file = open(name, 'w')

    def close(self):
        self.file.close()

    def write(self, iteration, best_fitness_train, best_fitness_test, individuals):
        it = "it:#%d %.2f %.2f" % (iteration, best_fitness_train, best_fitness_test)
        self.file.write(it)
        self.file.write("\n")
        self.file.write("velocities:#%d " % iteration)
        for i in individuals:
            for bit in i.bit_string:
                if type(bit) == str:
                    bit = bit.split(":")[0]
                self.file.write("%s " % bit)
        self.file.write("\n")
