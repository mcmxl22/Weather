#!/usr/bin/env python3

"""
pressure_forecast version 1.4
Python 3.7
"""

from numli import add_numbers


def forecast(pressure_trend):
    """Forecasts based on barometric pressure trends"""
    trend_options = ["Rising", "Falling", "Steady"]
    addnum(trend_options)
    pressure_trend = input("\nChoose a trend. ")
    invalid = "Invalid Entry!"

    forecast_dict = {
        "1": "Fairer weather on the way.",
        "2": "Poorer weather on the way.",
        "3": "No significant change."
    }

    if pressure_trend in forecast_dict:
        print(forecast_dict[pressure_trend])
    else:
        print(invalid)
        forecast(trend)


if __name__ == "__main__":
    forecast('pressure_trend')
