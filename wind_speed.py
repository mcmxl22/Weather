#!/usr/bin/env python3

"""
wind_speed version 1.5
Python 3.7
"""

import sys


def wind():
    """Convert knots to MPH"""
    try:
        convert_wind = int(input("Enter wind speed as knots. "))
        conversion_formula = ((float(convert_wind)) * 6067) / 5280
        result = f"{convert_wind} knots is {round(conversion_formula, 2)} MPH."
        print(result)
    except ValueError as error:
        print("Entry must be a number")
        wind()


if __name__ == "__main__":
    sys.exit(wind())
