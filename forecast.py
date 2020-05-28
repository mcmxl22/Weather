#!/usr/bin/env python3

"""
forecast version 1.4
Python 3.7
"""

import pressure_forecast
from numli import addnum


def forecast(forecast_choice):
    """Weather forecasts"""
    forecast_options = ["Pressure trend based"]
    addnum(forcast_options)
    forecast_choice = input("Choose a forecast. ")

    if forecast_choice in "1":
        pressure_forecast.forecast(forecast_choice)
    else:
        print("Invalid Entry!")
        forecast(forecast_choice)


if __name__ == "__main__":
    forecast("forecast_choice")
