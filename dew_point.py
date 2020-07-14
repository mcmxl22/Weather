#!/usr/bin/env python3

"""
dew_point version 1.3
Python 3.7
"""

import logging
import sys


logging.basicConfig(filename="dew_point.log", level=logging.DEBUG)


def dew_point(temperature):
    """Calculate the dew point."""
    degree_sign = "\N{DEGREE SIGN}"
    temperature = int(input("Enter the temperature in Celsius. "))
    relative_humidity = int(input("Enter the relative humidity. "))
    logging.debug(temperature)
    logging.debug(relative_humidity)

    try:
        formula = temperature - ((100 - relative_humidity) / 5)
        result = f"The dew point is {formula}{degree_sign}C."
        print(result)
        logging.debug(result)
    except ValueError as error:
        logging.debug(error)
        print("Entry must be a number")


if __name__ == "__main__":
    sys.exit(dew_point("temperature"))
