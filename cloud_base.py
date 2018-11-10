#!/usr/bin/env python
"""By Micah M. 2018
   cloud_base version 1
   Python 3.7.1"""


def cloud_base(temperature):
    """Calculate the height of the clouds."""
    temperature = input('Enter the temperature in Celsius. ')
    enter_dew_point = input('Enter dew point in Celsius. ')
    spread = int(temperature) - int(enter_dew_point)
    cloud_ceiling_formula = int(spread) / 2.5 * 1000
    print('The cloud ceiling is')
    print(f'{int(cloud_ceiling_formula)}\' above the ground.\n')

    if __name__ == "__main__":
        cloud_base('temperature')
