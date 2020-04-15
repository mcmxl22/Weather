#!/bin/python3
"""
fahrenheit_conversion version 1.1
Python 3.7
"""

def to_celsius(celsius_convert):
    """Convert Fahrenheit to Celsius."""
    degree_sign = u'\N{DEGREE SIGN}'
    celsius_convert = int(input('Enter temperature in Celsius. '))
    conversion_formula = celsius_convert * 1.8 + 32
    print(f'''{celsius_convert}{degree_sign}C is
          \r{conversion_formula}{degree_sign}F.''')

if __name__ == "__main__":
    to_celsius('celsius_convert')
