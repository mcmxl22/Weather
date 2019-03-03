#!/bin/python3
"""celcius_conversion version 1
   Python 3.7.2"""


def to_fahrenheit(fahrenheit_convert):
    """Convert Celsius to Fahrenheit."""
    degree_sign = u'\N{DEGREE SIGN}'
    fahrenheit_convert = input('Enter the temperature in Fahrenheit. ')
    conversion_formula = (int(fahrenheit_convert) - 32) / 1.8
    print(f'''{fahrenheit_convert}{degree_sign}F is
          \r{int(conversion_formula)}{degree_sign}C.''')

if __name__ == "__main__":
    to_fahrenheit('fahrenheit_convert')
