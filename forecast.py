#!/usr/bin/env python
'''By Micah M. 2018
   forecast version 1.3
   Python 3.7'''

import subprocess
import sys


def forecast():
    '''Weather forecasts'''
    forecast_options = ['1 Pressure trend', '2 Extended']
    print('\n'.join(forecast_options))
    forecast_choice = input('\nChoose a forecast.\n> ')

    if forecast_choice == '1':
        this_forecast = [sys.executable, 'pressure_forecast.py']
        subprocess.run(this_forecast)
    elif forecast_choice == '2':
        this_forecast = [sys.executable, 'extended_forecast.py']
        subprocess.run(this_forecast)
    else:
        print('Invalid Entry!\n')
        forecast()


if __name__ == "__main__":
    forecast()
