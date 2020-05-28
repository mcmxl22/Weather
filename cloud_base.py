#!/usr/bin/env python3

"""
cloud_base version 1.2
Python 3.7
"""


def base(temperature):
    """Calculate the altittude of the clouds."""
    temperature = int(input("Enter temperature in Celsius. "))
    enter_dew_point = int(input("Enter dew point in Celsius. "))

    try:
        spread = temperature - enter_dew_point
        formula = spread / 2.5 * 1000
        print(f"The cloud ceiling is {formula}' above the ground.")
    except ValueError:
        print("Entry must be a number.")


if __name__ == "__main__":
    base("temperature")
