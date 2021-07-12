#!/usr/bin/env python3

"""
Author: M McConnaughey
cloud_base version 1.5
Python 3.7
Date: 07/12/2021
"""


def find_base():
    """
    Calculate the altittude of the clouds.
    """
    spread = get_temperature() - get_dewpoint()
    formula = spread / 2.5 * 1000
    print(f"The cloud ceiling is {formula} feet above the ground.")


def get_dewpoint():
    enter_dew_point = int(input("Enter dew point in Celsius. "))
    return enter_dew_point

def get_temperature():
    temperature = int(input("Enter temperature in Celsius. "))
    return temperature


def main():
    find_base()


if __name__ == "__main__":
    main()
