#!/bin/python3
"""dew_point version 1
   Python 3.7.2"""


def dew_point(temperature):
    """Calculate the dew point."""
    degree_sign = u'\N{DEGREE SIGN}'
    temperature = input('Enter the temperature in Celsius. ')
    relative_humidity = input('Enter the relative humidity. ')
    dew_point_formula = (int(temperature) - ((100 - int(relative_humidity)) / 5))
    result = f'\nThe dew point is {int(dew_point_formula)}{degree_sign}C.'
    print(result)

if __name__ == "__main__":
    dew_point('temperature')
