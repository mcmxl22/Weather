#!/usr/bin/env python3

"""
Author: M McConnaughey
pressure_conversion version 1.3
Date: 07/13/2022
Python 3.7
"""


def convert_millibars():
    """Convert millibars to inches of mercury."""
    try:
        millibar_convert = int(input("Enter pressure in millibars. "))
    except ValueError:
        print("Entry must be a number")
    else:
        conversion_formula = int(millibar_convert) / 33.864
        print(f"{millibar_convert} millibars is {round(conversion_formula, 2)} inches of mercury.")


if __name__ == "__main__":
    convert_millibars()
