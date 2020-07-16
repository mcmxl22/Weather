#!/usr/bin/env python3
"""
fahrenheit_conversion version 1.4
Python 3.7
"""


import sys


def to_celsius():
    """Convert Fahrenheit to Celsius."""
    degree_sign = "\N{DEGREE SIGN}"

    try:
        celsius_convert = int(input("Enter temperature in Celsius. "))
    except ValueError:
        print("Entry must be a number!")
    else:
        conversion_formula = celsius_convert * 1.8 + 32
        print(f"{celsius_convert}{degree_sign}C is {round(conversion_formula, 2)}{degree_sign}F.")


if __name__ == "__main__":
    sys.exit(to_celsius())
