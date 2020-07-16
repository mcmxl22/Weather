#!/usr/bin/env python3

"""
cloud_base version 1.4
Python 3.7
"""

import sys


def find_base():
    """Calculate the altittude of the clouds."""
    try:
        temperature = int(input("Enter temperature in Celsius. "))
        enter_dew_point = int(input("Enter dew point in Celsius. "))
    except ValueError:
        print("Entry must be a number.")
    else:
        spread = temperature - enter_dew_point
        formula = spread / 2.5 * 1000
        print(f"The cloud ceiling is {formula}' above the ground.")


if __name__ == "__main__":
    sys.exit(find_base())
