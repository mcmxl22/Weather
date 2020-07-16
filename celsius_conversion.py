#!/usr/bin/env python3

"""
celcius_conversion version 1.3
Python 3.7
"""


import sys


def to_fahrenheit():
    """Convert Celsius to Fahrenheit."""
    degree_sign = "\N{DEGREE SIGN}"

    try:
        fahrenheit_convert = int(input("Enter temperature in Fahrenheit. "))
    except ValueError:
        print("Please enter a number.")
        to_fahrenheit()
    else:
        conversion_formula = (fahrenheit_convert - 32) / 1.8
        print(
            f"{fahrenheit_convert}{degree_sign}F is {round(conversion_formula, 2)}{degree_sign}C."
        )


if __name__ == "__main__":
    sys.exit(to_fahrenheit())
