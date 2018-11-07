#!/usr/bin/env python
"""By Micah M. 2018
   forecast version 1.3
   Python 3.7.1"""

import extended_forecast
import pressure_forecast


def forecast(forecast_choice):
    """Weather forecasts"""
    forecast_options = ['1 Pressure trend based', '2 Extended']
    print('\n'.join(forecast_options))
    forecast_choice = input('Choose a forecast. ')

    if forecast_choice in '1':
        pressure_forecast.forecast(forecast_choice)
    elif forecast_choice in '2':
        extended_forecast.forecast(forecast_choice)
    else:
        print('Invalid Entry!')
        forecast(forecast_choice)


if __name__ == "__main__":
    forecast('forecast_choice')
