#!/usr/bin/env python
'''By Micah M. 2018
   forecast version 1.3
   Python 3.7.1'''

import extended_forecast
import pressure_forecast
import subprocess
import sys


def forecast(forecast_choice):
    '''Weather forecasts'''
    forecast_options = ['1 Pressure trend based', '2 Extended']
    print('\n'.join(forecast_options))
    forecast_choice = input('Choose a forecast. ')

    if forecast_choice in '1':
        this_forecast = [sys.executable, 'pressure_forecast.py']
        subprocess.run(this_forecast)
    elif forecast_choice in '2':
        this_forecast = [sys.executable, 'extended_forecast.py']
        subprocess.run(this_forecast)
    else:
        print('Invalid Entry!')
        forecast()


if __name__ == "__main__":
    forecast()
