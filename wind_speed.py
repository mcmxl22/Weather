#!/bin/python3
"""wind_speed version 1
   Python 3.7.2"""


def wind(wind_convert):
    """Convert knots to MPH"""
    wind_convert = input('Enter wind speed in knots. ')
    conversion_formula = ((int(wind_convert) * 6067) / 5280)
    results = f'{wind_convert} knots is {round(conversion_formula, 2)} MPH.'
    print(results)


if __name__ == "__main__":
    wind('wind_convert')
