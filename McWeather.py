#!/usr/bin/env python
'''By Micah M. 2018
   McWeather version 10.2
   Python 3.7.1'''

import cloud_types
import entry_log
import forecast


DEGREE_SIGN = u'\N{DEGREE SIGN}'


def dew_point():
    '''Calculate the dew point.'''
    temperature = input('Enter the temperature in Celsius. ')
    relative_humidity = input('Enter the relative humidity. ')
    dew_point_formula = (int(temperature) - ((100 - int(relative_humidity)) / 5))
    print(f'\nThe dew point is {int(dew_point_formula)}{DEGREE_SIGN}C.')


def cloud_base():
    '''Calculate the height of the clouds.'''
    temperature = input('Enter the temperature in Celsius. ')
    enter_dew_point = input('Enter dew point in Celsius. ')
    spread = int(temperature) - int(enter_dew_point)
    cloud_ceiling_formula = int(spread) / 2.5 * 1000
    print('The cloud ceiling is')
    print(f'{int(cloud_ceiling_formula)}\' above the ground. ')


def celsius():
    '''Convert Fahrenheit to Celsius.'''
    celsius_convert = input('Enter temperature in Celsius. ')
    conversion_formula = int(celsius_convert) * 1.8 + 32
    print(f'{celsius_convert}{DEGREE_SIGN}C is')
    print(f'{int(conversion_formula)}{DEGREE_SIGN}F.')


def fahrenheit():
    '''Convert Celsius to Fahrenheit.'''
    fahrenheit_convert = input('Enter the temperature in Fahrenheit. ')
    conversion_formula = (int(fahrenheit_convert) - 32) / 1.8
    print(f'{fahrenheit_convert}{DEGREE_SIGN}F is')
    print(f'{int(conversion_formula)}{DEGREE_SIGN}C.')


def wind_speed():
    '''Convert knots to MPH'''
    wind_convert = input('Enter wind speed in knots. ')
    conversion_formula = ((int(wind_convert) * 6067) / 5280)
    print(f'{wind_convert} knots = {round(conversion_formula, 2)} MPH.')


def prompt():
    '''Prompt user to choose from list, and log choice.'''
    while True:
        prompt_options = [
            '1 Convert to Celsius ', '2 Convert to Fahrenheit ',
            '3 Find dew point', '4 Weather forecast', '5 Find cloud ceiling',
            '6 Convert knots to MPH', '7 Cloud types', '8 Exit']

        print(' \n'.join(prompt_options))
        prompt_choice = input('\nChoose an option. ')
        entry_log.entry(prompt_choice)

        if prompt_choice in '1':
            fahrenheit()
        elif prompt_choice in '2':
            celsius()
        elif prompt_choice in '3':
            dew_point()
        elif prompt_choice in '4':
            forecast.forecast(prompt_choice)
        elif prompt_choice in '5':
            cloud_base()
        elif prompt_choice in '6':
            wind_speed()
        elif prompt_choice in '7':
            cloud_types.clouds(prompt_choice)
        elif prompt_choice in '8':
            raise SystemExit
        else:
            print('\nInvalid Entry')



if __name__ == "__main__":
    prompt()
