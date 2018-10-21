#!/usr/bin/env python 
'''By Micah M. 2018
   Weather version 10
   Python 3.7
   Requires forecast.py, cloud_types.py, entry_log.py'''

import subprocess
import sys
import entry_log

DEGREE_SIGN = u'\N{DEGREE SIGN}'

def dew_point():
    '''Calculate the dew point.'''
    temperature = input('\nEnter the temperature in Celsius. ')
    relative_humidity = input('\nEnter the relative humidity ')
    dew_point_formula = (int(temperature) - ((100 - int(relative_humidity)) / 5))
    print(f'\nThe dew point is {int(dew_point_formula)} degrees Celsius.\n')

def cloud_base():
    '''Calculate the height of the clouds.'''
    temperature = input('Enter the temperature in celsius. ')
    dew_pnt = input('Enter dew point in celsius. ')
    spread = int(temperature) - int(dew_pnt)
    cloud_ceiling_formula = int(spread) / 2.5 * 1000
    print(f'''The cloud ceiling is
              \r{int(cloud_ceiling_formula)} feet above the ground.\n''')


def celsius():
    '''Convert fahrenheit to celsius.'''
    celsius_convert = input('\nEnter temperature in Celsius. ')
    conversion_formula = int(celsius_convert) * 1.8 + 32
    print(f'''{celsius_convert}{DEGREE_SIGN} Celsius is
              \r{int(conversion_formula)}{DEGREE_SIGN} Fahrenheit.\n''')


def fahrenheit():
    '''Convert celsius to fahrenheit.'''
    fahrenheit_convert = input('\nEnter the temperature in Fahrenheit. ')
    conversion_formula = (int(fahrenheit_convert) - 32) / 1.8
    print(f'''{fahrenheit_convert}{DEGREE_SIGN} Fahrenheit is 
              \r{int(conversion_formula)}{DEGREE_SIGN} Celsius.\n''')


def wind_speed():
    '''Convert knots to MPH'''
    wind_convert = input('\nEnter wind speed in knots. ')
    conversion_formula = ((int(wind_convert) * 6067) / 5280)
    print(f'{wind_convert} knots = {round(conversion_formula, 2)} MPH.\n')


def prompt():
    '''Prompt user to choose from list, and log choice.'''
    while True:
        prompt_options = [
            '1 Convert to celsius ', '2 Convert to fahrenheit ',
            '3 Find dew point', '4 Weather forcast', '5 Find cloud ceiling',
            '6 Convert knots to MPH', '7 Cloud types', '8 Exit']
        print('\n'.join(prompt_options))
        prompt_choice = input('\nChoose an option. ')
        entry_log.entry(prompt_choice)

        if prompt_choice == '1':
            fahrenheit()
        elif prompt_choice == '2':
            celsius()
        elif prompt_choice == '3':
            dew_point()
        elif prompt_choice == '4':
            forecast = [sys.executable, 'forecast.py']
            subprocess.run(forecast)
        elif prompt_choice  == '5':
            cloud_base()
        elif prompt_choice  == '6':
            wind_speed()
        elif prompt_choice  == '7':
            cloud_types = [sys.executable, 'cloud_types.py']
            subprocess.run(cloud_types)
        elif prompt_choice  == '8':
            raise SystemExit
        else:
            print('\nInvalid Entry\n')



if __name__ == "__main__":
    prompt()
