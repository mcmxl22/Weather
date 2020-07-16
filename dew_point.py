#!/usr/bin/env python3

"""
dew_point version 1.4
Python 3.7
"""

import sys


def find_dew_point():
    """Calculate the dew point."""
    degree_sign = "\N{DEGREE SIGN}"

    try:
        temperature = int(input("Enter the temperature in Celsius. "))
        relative_humidity = int(input("Enter the relative humidity. "))
    except ValueError as error:
        print("Entry must be a number")
    else:
        formula = temperature - ((100 - relative_humidity) / 5)
        result = f"The dew point is {formula}{degree_sign}C."
        print(result)


if __name__ == "__main__":
    sys.exit(find_dew_point())
