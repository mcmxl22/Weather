#!/usr/bin/env python3

"""
Author: M. McConnaughey
pressure_forecast version 1.8
Python 3.7
Date: 07/09/2021
"""

from numli import add_numbers


def make_menu():
    """
    Make a list of menu items.
    """
    trend_options = ["Rising", "Falling", "Steady"]
    menu = add_numbers(trend_options)
    return menu
    
    
def get_forecast():
    """
    Get forecasts based on barometric pressure trends.
    """
    forecast_dict = {
        1: "Fairer weather on the way.",
        2: "Poorer weather on the way.",
        3: "No significant change.",
    }

    try:
        pressure_trend = int(input("\nChoose a trend. "))
    except ValueError:
        print("Please enter a number.")
        get_forecast()
    else:
        print(forecast_dict.get(pressure_trend))


def main():
    make_menu()
    get_forecast()


if __name__ == "__main__":
    main()
