#!/bin/python3
"""
pressure_conversion version 1.1
Python 3.7
"""

def convert_millibars(millibar_convert):
    """Convert millibars to inches of mercury."""
    millibar_convert = int(input("Enter pressure in millibars. "))
    conversion_formula = millibar_convert / 33.864
    print(f"""{millibar_convert} millibars is
          \r{round(conversion_formula, 2)} inches of mercury.""")

if __name__ == "__main__":
    convert_millibars("millibar_convert")
