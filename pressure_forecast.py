#!/bin/python3
"""pressure_forecast version 1.3
   Python 3.7.2"""


def forecast(trend):
    """Forecasts based on barometric pressure trends"""
    trend_options = ['1. Rising', '2. Falling', '3. Steady']
    print('\n'.join(trend_options))
    trend = input('\nChoose a trend. ')

    if trend in '1':
        print('Fairer weather on the way.')
    elif trend in '2':
        print('Poorer weather on the way.')
    elif trend in '3':
        print('No significant change.\n')
    else:
        print('Invalid Entry!')
        forecast(trend)


if __name__ == "__main__":
    forecast('trend')
