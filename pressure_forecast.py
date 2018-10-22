#!/usr/bin/env python
'''By Micah M. 2018
   pressure_forecast version 1.2
   Python 3.7'''


def forecast():
    '''Forecasts based on barometric pressure trends'''
    trend_options = ['1 Rising', '2 Falling', '3 Steady']
    print('\n'.join(trend_options))
    trend = input('\nChoose a trend.\n> ')

    if trend == '1':
        print('\nFairer weather on the way.\n')
    elif trend == '2':
        print('\nPoorer weather on the way.\n')
    elif trend == '3':
        print('\nNo significant change.\n')
    else:
        print('Invalid Entry!\n')
        forecast()


if __name__ == "__main__":
    forecast()
