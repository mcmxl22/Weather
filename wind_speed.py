#!/usr/bin/env python3

"""
wind_speed version 1.6
Python 3.7
"""


class Wind:
    """Convert wind speeds."""
    def convert_to_mph(speed):
        mph_conversion_formula = ((float(speed)) * 1.151)
        mph_result = mph_conversion_formula
        return mph_result
    
    def convert_to_knots(speed):
        knots_conversion_formula = ((float(speed)) / 1.151)
        knots_result = knots_conversion_formula
        return knots_result
    
    def convert_to_kilometers(speed):
        kilometers_conversion_formula = ((float(speed)) * 0.6214)
        kilometers_result = kilometers_conversion_formula
        return kilometers_result


class Menu:
    """Prepare a menu."""
    def add_numbers(num):
        """Add numbers to the menu list."""
        for c, value in enumerate(num, 1):
            print(c, value)


    def list_choices():
        """Give user a choice of actions."""
        choose_conversion = ["Miles to Knots", "Knots to Miles", "Miles to Kilometers", "Exit"]
        return Menu.add_numbers(choose_conversion)


def main():
    list_choices = Menu.list_choices()
    error = "Please enter a valid speed."

    while True:
        list_choices
        action_choice = input("What do you want to do? ")
        
        if action_choice == '1':
            try:
                enter_speed = int(input(f"Enter wind speed as MPH. "))
                conversion_result = round(Wind.convert_to_knots(enter_speed), 2)
                print(f"{enter_speed} MPH is {conversion_result} Knots.")

            except ValueError:
                print(error)
                main()
        
        elif action_choice == '2':
            try:
                enter_speed = int(input(f"Enter wind speed as knots. "))
                conversion_result = round(Wind.convert_to_mph(enter_speed), 2)
                print(f"{enter_speed} knots is {conversion_result} MPH.")

            except ValueError:
                print(error)
                main()

        elif action_choice == '3':
            try:
                enter_speed = int(input(f"Enter wind speed as MPH. "))
                conversion_result = round(Wind.convert_to_kilometers(enter_speed), 2)
                print(f"{enter_speed} MPH is {conversion_result} KPH.")

            except ValueError:
                print(error)
                main()

        elif action_choice == '4':
            quit()


if __name__ == "__main__":
    main()
