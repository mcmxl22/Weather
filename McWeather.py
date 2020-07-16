#!/usr/bin/env python3

"""
index version 10.6
Python 3.7
"""

import sys
from beaufort import scale_wind
from celsius_conversion import to_fahrenheit
from cloud_base import find_base
from cloud_types import main
from dew_point import find_dew_point
from fahrenheit_conversion import to_celsius
from pressure_conversion import convert_millibars
from wind_speed import wind
from numli import add_numbers
from pressure_forecast import get_forecast


def main():
    """Prompt user to choose from list."""
    while True:
        weather_options = [
            "Convert to Celsius",
            "Convert to Fahrenheit",
            "Find dew point",
            "Find cloud ceiling",
            "Convert knots to MPH",
            "Cloud types",
            "Beaufort scale",
            "Forcast",
            "Convert pressure",
            "Exit",
        ]

        add_numbers(weather_options)

        choice_dic = {
            1: to_celsius,
            2: to_fahrenheit,
            3: find_dew_point,
            4: find_base,
            5: wind,
            6: main,
            7: scale_wind,
            8: get_forecast,
            9: convert_millibars,
        }

        try:
            weather_choice = int(input("\nChoose an option. "))
        except ValueError:
            print("Please enter a number.")

        if weather_choice == 10:
            sys.exit(0)
        else:
            print(f"\n{choice_dic[weather_choice]()}\n")


if __name__ == "__main__":
    sys.exit(main())
