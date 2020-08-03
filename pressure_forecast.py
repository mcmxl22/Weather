#!/usr/bin/env python3

"""
pressure_forecast version 1.7
Python 3.7
"""

import sys
from numli import add_numbers


def get_forecast():
    """Get forecasts based on barometric pressure trends."""
    trend_options = ["Rising", "Falling", "Steady"]
    add_numbers(trend_options)

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


if __name__ == "__main__":
    sys.exit(get_forecast())
