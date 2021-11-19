#!/usr/bin/env python3

"""
dew_point version 1.5
Python 3.7
"""

class Air:
    
    def compute_dew_point(self, temperature, humidity):
        dew_point = int(temperature) - ((100 - int(humidity)) / 5)
        return dew_point


def main():
    """
    Calculate the dew point.
    """
    degree_sign = "\N{DEGREE SIGN}"
    temperature = input("Enter temperature: ")
    humidity = input("Enter humidity: ")

    x = Air()

    result = x.compute_dew_point(temperature, humidity)
    print(f"The dew point in {result}{degree_sign}F")


if __name__ == "__main__":
    exit(main())
