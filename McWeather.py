#!/usr/bin/env python3
"""
index version 10.5
Python 3.7
"""

from beaufort import scale_wind
from celsius_conversion import to_fahrenheit
from cloud_base import base
from cloud_types import clouds
from dew_point import dew_point
from mcweather_entry_log import entry
from fahrenheit_conversion import to_celsius
from forecast import forecast
from pressure_conversion import convert_millibars
from wind_speed import wind


def prompt(prompt_choice):
    """Prompt user to choose from list."""
    while True:
        prompt_options = [
            'Convert to Celsius', 'Convert to Fahrenheit',
            'Find dew point', 'Weather forecast', 'Find cloud ceiling',
            'Convert knots to MPH', 'Cloud types', 'Beaufort scale',
            'Convert pressure', 'Exit']

        for index, prompt in enumerate(prompt_options, start=1):
            print(index, prompt)
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
