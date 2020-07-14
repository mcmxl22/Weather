#!/usr/bin/env python3

"""
pressure_conversion version 1.2
Python 3.7
"""

import sys


def convert_millibars(millibar_convert):
    """Convert millibars to inches of mercury."""
    try:
        millibar_convert = int(input("Enter pressure in millibars. "))

    except ValueError:
        print("Entry must be a number")

    else:
        conversion_formula = int(millibar_convert) / 33.864
        return f"{millibar_convert} millibars is {round(conversion_formula, 2)} inches of mercury."


if __name__ == "__main__":
    sys.exit(convert_millibars("millibar_convert"))
