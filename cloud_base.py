#!/bin/python3
"""cloud_base version 1
   Python 3.7.2"""


def base(temperature):
    """Calculate the height of the clouds."""
    temperature = input('Enter the temperature in Celsius. ')
    enter_dew_point = input('Enter dew point in Celsius. ')
    spread = int(temperature) - int(enter_dew_point)
    cloud_ceiling_formula = int(spread) / 2.5 * 1000
    print(f'''The cloud ceiling is
          \r{int(cloud_ceiling_formula)}\' above the ground.''')


if __name__ == "__main__":
    base('temperature')
