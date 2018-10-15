#!/usr/bin/env python3
'''By Micah M. 2018
   Weather version 1.9
   Python 3.7
   Requires forecast.py, cloud_types.py, entry_log.py'''

import subprocess
import sys
import entry_log

def dew_point():
    '''Calculate the dew point.'''
    temperature = input('\nEnter temperature in Celsius.\n> ')
    relative_humidity = input('\nEnter relative humidity\n> ')
    dew_point_formula = (int(temperature) - ((100 - int(relative_humidity)) / 5))
    print(f'\nThe dew point is {int(dew_point_formula)} degrees Celsius.\n')


def cloud_base():
    '''Calculate the height of the clouds.'''
    temperature = input('Enter temperature in celsius.\n> ')
    dew = input('Enter dew point in celsius.\n> ')
    spread = int(temperature) - int(dew)  # Difference between temperature and dew point.
    cloud_ceiling_formula = int(spread) / 2.5 * 1000
    print(f'The cloud ceiling is {int(cloud_ceiling_formula)} feet above the ground.\n')


def celsius():
    '''Convert fahrenheit to celsius.'''
    convert = input('\nEnter temperature in Celsius.\n> ')
    formula = int(convert) * 1.8 + 32  # Formula for celsius to fahrenheit.
    print(f'{convert} degrees Celsius is {int(formula)} degrees Fahrenheit.\n')


def fahrenheit():
    '''Convert celsius to fahrenheit.'''
    convert = input('\nEnter the temperature in Fahrenheit.\n> ')
    formula = (int(convert) - 32) / 1.8  # Formula for fahrenheit to celsius
    print(f'{convert} degrees Fahrenheit is {int(formula)} degrees Celsius.\n')


def wind_speed():
    '''Convert knots to MPH'''
    convert = input('Enter wind speed in knots.\n ')
    formula = ((int(convert) * 6067) / 5280)
    print(f'{convert} knots is {round(formula, 3)} MPH.\n')



def prompt():
    '''Prompt user to choose from list, and log choice.'''
    while True:
        prompt_options = [
            '1 Convert from Fahrenheit', '2 Convert from Celsius',
            '3 Find Dew Point', '4 Weather Forcast', '5 Cloud Ceiling',
            '6 Convert knots to MPH', '7 Cloud Types', '8 Exit']
        print('\n'.join(prompt_options))
        prompt_choice = input('\nChoose an option.\n> ')
        entry_log.entry_log(prompt_choice)

        if prompt_choice == '1':
            fahrenheit()
        elif prompt_choice == '2':
            celsius()
        elif prompt_choice == '3':
            dew_point()
        elif prompt_choice == '4':
            forecast = [sys.executable, 'forecast.py']
            subprocess.call(forecast)
        elif prompt_choice  == '5':
            cloud_base()
        elif prompt_choice  == '6':
            wind_speed()
        elif prompt_choice  == '7':
            cloud_types = [sys.executable, 'cloud_types.py']
            subprocess.call(cloud_types)
        elif prompt_choice  == '8':
            raise SystemExit
        else:
            print('\nInvalid Entry\n')



if __name__ == "__main__":
    prompt()
