#!/usr/bin/env python
'''By Micah M. 2018
   McWeather version 10.4
   Python 3.7.1'''

from beaufort import scale_wind
from celsius_conversion import to_fahrenheit
from cloud_base import base
from cloud_types import clouds
from dew_point import dew_point
from entry_log import entry
from fahrenheit_conversion import to_celsius
from forecast import forecast
from pressure_conversion import convert_millibars
from wind_speed import wind


def prompt(prompt_choice):
    '''Prompt user to choose from list, and log choice.'''
    while True:
        prompt_options = ['1 Convert to Celsius ', '2 Convert to Fahrenheit ',
            '3 Find dew point', '4 Weather forecast', '5 Find cloud ceiling',
            '6 Convert knots to MPH', '7 Cloud types', '8 Beaufort scale',
            '9 Convert pressure', '10 Exit']

        print('\n'.join(prompt_options))
        prompt_choice = input('\nChoose an option. ')
        entry(prompt_choice)

        if prompt_choice in '1':
            to_celsius(prompt_choice)
        elif prompt_choice in '2':
            to_fahrenheit('prompt_choice')
        elif prompt_choice in '3':
            dew_point(prompt_choice)
        elif prompt_choice in '4':
            forecast(prompt_choice)
        elif prompt_choice in '5':
            base(prompt_choice)
        elif prompt_choice in '6':
            wind(prompt_choice)
        elif prompt_choice in '7':
            clouds(prompt_choice)
        elif prompt_choice in '8':
            scale_wind(prompt_choice)
        elif prompt_choice in '9':
            convert_millibars(prompt_choice)
        elif prompt_choice in '10':
            raise SystemExit
        else:
            print('\nInvalid Entry')



if __name__ == "__main__":
    prompt('prompt_choice')
