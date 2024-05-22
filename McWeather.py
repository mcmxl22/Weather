#!/usr/bin/env python3

"""
Author: M. McConnaughey
McWeather version 10.9
Date: 07/13.2022
Python 3.7
"""

from beaufort import scale_wind
from celsius_conversion import to_fahrenheit
from cloud_base import find_base
from cloud_types import cloud_main
from dew_point import calculate_dew_point
from fahrenheit_conversion import to_celsius
from pressure_conversion import convert_millibars
from wind_speed import main
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

        for c, value in enumerate(weather_options, 1):
            print(c, value)

        choice_dic = {
            1: to_celsius,
            2: to_fahrenheit,
            3: calculate_dew_point,
            4: find_base,
            5: main,
            6: cloud_main,
            7: scale_wind,
            8: get_forecast,
            9: convert_millibars,
        }

        try:
            weather_choice = int(input("\nChoose an option. "))
            if weather_choice == 10:
                exit()
            elif weather_choice > 10:
                print("Please enter correct number.")
            else:
                choice_dic[weather_choice]()

        except(ValueError, KeyError):
            print("Please enter a number.")
            main()


if __name__ == "__main__":
    main()
