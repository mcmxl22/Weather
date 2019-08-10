#!/usr/bin/env python3
"""
cloud_base version 1.1
Python 3.7
"""

import logging


logging.basicConfig(filename="cloud_base.log", level=logging.DEBUG)


def base(temperature):
    """Calculate the altittude of the clouds."""
    temperature = input("Enter temperature in Celsius. ")
    enter_dew_point = input("Enter dew point in Celsius. ")

    try:
        spread = int(temperature) - int(enter_dew_point)
        formula = int(spread) / 2.5 * 1000
        print(f"The cloud ceiling is {int(formula)}' above the ground.")

    except ValueError as error:
        logging.debug(error)
        print("Entry must be a number.")


if __name__ == "__main__":
    base("temperature")
