"""
Author: M. McConnaughey
wind_speed version 1.8
Date: 08/14/2023
Python 3.7
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class ConversionCoefficients:
    """Conversion Coefficients."""
    mph_to_knots: float = 0.868976242
    knots_to_mph: float = 1.1507794480235425
    mph_to_kph: float = 1.60934


def mph_to_knots(mph: float) -> float:
    """Convert miles per hour to knots per hour."""
    return mph * ConversionCoefficients.mph_to_knots

def knots_to_mph(knots: float) -> float:
    """Convert knots per hour to miles per hour."""
    return knots * ConversionCoefficients.knots_to_mph

def mph_to_kph(mph: float) -> float:
    """Convert miles per hour to kilometers per hour."""
    return mph * ConversionCoefficients.mph_to_kph

def add_numbers(num):
    """Add numbers to the menu list."""
    for c, value in enumerate(num, 1):
        print(c, value)

def list_choices():
    """Give user a choice of actions."""
    choose_conversion = ["Miles to Knots", "Knots to Miles", "Miles to Kilometers", "Exit"]
    return add_numbers(choose_conversion)

def main():
    """main function"""
    error = "Please enter a valid speed."

    while True:
        list_choices()
        choice = input("What do you want to do? ")

        if choice == '1':
            try:
                speed = int(input("Enter wind speed in MPH. "))
            except ValueError:
                print(error)
            else:
                result = mph_to_knots(speed)
                print(f"{speed} MPH is {round(result, 2)} Knots.")

        elif choice == '2':
            try:
                enter_speed = int(input(f"Enter wind speed as knots. "))
                result = round(knots_to_mph(enter_speed), 2)
                print(f"{enter_speed} knots is {round(result, 2)} MPH.")

            except ValueError:
                print(error)

        elif choice == '3':
            try:
                enter_speed = int(input(f"Enter wind speed as MPH. "))
                result = round(mph_to_kph(enter_speed), 2)
                print(f"{enter_speed} MPH is {round(result, 2)} KPH.")

            except ValueError:
                print(error)

        elif choice == '4':
            break

if __name__ == "__main__":
    main()
