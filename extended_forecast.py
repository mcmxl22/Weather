#!/usr/bin/env python
"""By Micah M. 2018
   extended_forecast version 1.1
   Python 3.7.1"""

from weather import Weather, Unit

DEGREE_SIGN = u'\N{DEGREE SIGN}'


def forecast(city):
    """Give an extended forecast based on location."""
    city = input('Enter your location. ')

    weather = Weather(unit=Unit.FAHRENHEIT)

    location = weather.lookup_by_location(city)
    forecasts = location.forecast

    for forecast in forecasts:
        print(f'\n{forecast.date}')
        print(forecast.text)
        print(f'{forecast.high}{DEGREE_SIGN}F High')
        print(f'{forecast.low}{DEGREE_SIGN}F Low\n')


if __name__ == "__main__":
    forecast('city')
