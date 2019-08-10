#!/usr/bin/env python3
"""
dew_point version 1.1
Python 3.7
"""

import logging


logging.basicConfig(filename="dew_point.log", level=logging.DEBUG)


def dew_point(temperature):
    """Calculate the dew point."""
    degree_sign = "\N{DEGREE SIGN}"
    temperature = input("Enter the temperature in Celsius. ")
    relative_humidity = input("Enter the relative humidity. ")
    logging.debug(temperature)
    logging.debug(relative_humidity)

    try:
        formula = int(temperature) - ((100 - int(relative_humidity)) / 5)
        result = f"\nThe dew point is {int(formula)}{degree_sign}C."
        print(result)
        logging.debug(result)

    except ValueError as error:
        logging.debug(error)
        print("Entry must be a number")


if __name__ == "__main__":
    dew_point("temperature")
