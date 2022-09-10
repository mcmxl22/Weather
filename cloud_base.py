#!/usr/bin/env python3

"""
Author: M McConnaughey
cloud_base version 1.6
Python 3.7
Date: 08/09/2022
"""


def find_base():
    """
    Calculate the altittude of the clouds.
    """
    spread = get_temperature() - get_dewpoint()
    formula = spread / 2.5 * 1000
    return formula


def get_dewpoint():
    enter_dew_point = int(input("Enter dew point in Celsius. "))
    return enter_dew_point


def get_temperature():
    temperature = int(input("Enter temperature in Celsius. "))
    return temperature


if __name__ == "__main__":
    base = find_base()
    print(f"The cloud ceiling is {base} feet above the ground.")
