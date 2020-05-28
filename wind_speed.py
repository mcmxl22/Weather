#!/usr/bin/env python3

"""
wind_speed version 1.3
Python 3.7
"""

import logging


logging.basicConfig(filename="wind_speed.log", level=logging.DEBUG)


def wind(convert_wind):
    """Convert knots to MPH"""
    convert_wind = input("Enter wind speed as knots. ")
    logging.debug(convert_wind)

    try:
        conversion_formula = ((float(convert_wind)) * 6067) / 5280
        result = f"{convert_wind} knots is {round(conversion_formula, 2)} MPH."
        logging.debug(result)
        print(result)
    except ValueError as error:
        logging.debug(error)
        print("Entry must be a number")
        wind(convert_wind)


if __name__ == "__main__":
    wind("convert_wind")
