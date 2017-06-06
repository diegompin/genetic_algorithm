__author__ = 'diegopinheiro'

import math


class FloatConverter2:

    number_digits_integers = 1
    number_digits_decimals = 1

    @staticmethod
    def get_number_representation():
        return 1 + FloatConverter2.number_digits_integers + FloatConverter2.number_digits_decimals


    @staticmethod
    def get_genes(value):
        number_digits_decimals = FloatConverter2.number_digits_decimals
        number_digits_integers = FloatConverter2.number_digits_integers

        positive_signal = 1 if value > 0 else 0
        unsigned_value = math.fabs(value)
        int_value = int(unsigned_value)
        decimal_value = int(round((unsigned_value - int_value) * math.pow(10, number_digits_decimals)))

        size = len(str(int_value))
        integer_digits = str(int_value)[size-number_digits_integers:size].zfill(number_digits_integers)
        decimal_digits = str(decimal_value)[0:number_digits_decimals].zfill(number_digits_decimals)

        representation = "".join(integer_digits+decimal_digits)

        genes = [positive_signal] + [float(i) for i in representation]

        return genes

    @staticmethod
    def get_value(genes):

        number_digits_decimals = FloatConverter2.number_digits_decimals
        number_digits_integers = FloatConverter2.number_digits_integers

        positive_signal = genes[0]
        integer_digits = genes[1:1+number_digits_integers]
        decimal_digits = genes[len(genes) - number_digits_decimals:len(genes)]

        integer_value = float("".join([str(int(i)) for i in integer_digits]))
        decimal_value = float("".join([str(int(i)) for i in decimal_digits])) / math.pow(10, number_digits_decimals)

        value = integer_value + decimal_value

        if not positive_signal:
            value *= -1

        return value