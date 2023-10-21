#!/usr/bin/env python3

"""
Author: M McConnaughey
dew_point version 1.6
Python 3.7
Date: 10/21/2023
"""


def calculate_dew_point(temperature, humidity) -> float:
    """
    define the dew point formula.
    """
    dew_point = temperature - ((100 - humidity) / 5)

    return dew_point


def main():
    """
    Calculate the dew point.
    """
    degree_sign = "\N{DEGREE SIGN}"

    try:
        temperature = int(input("Enter temperature: "))
        humidity = int(input("Enter humidity: "))
    except ValueError:
        print("Please enter a number.")

    result = calculate_dew_point(temperature, humidity)
    print(f"The dew point in {result}{degree_sign}F")


if __name__ == "__main__":
    main()
