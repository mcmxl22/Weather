"""
Author: M. McConnaughey
pressure_forecast version 2.1
Date: 12/08/2023
Python 3.7
"""

def make_menu():
    """Make a list of menu items"""
    trend_options_list = ["1 Rising", "2 Falling", "3 Steady"]
    for i in trend_options_list:
        print(i)

def get_forecast():
    """Get forecasts based on barometric pressure trends"""
    forecast_dict = {
        1: "Fairer weather on the way.",
        2: "Poorer weather on the way.",
        3: "No significant change.",
    }
    return forecast_dict

def get_input():
    """Get input from user"""
    forecast = get_forecast()
    while True:
        try:
            pressure_trend_input = int(input("\nChoose a trend (or enter 4 to exit): "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if pressure_trend_input == 4:
            break

        if pressure_trend_input not in forecast:
            print(f"Option {pressure_trend_input} is not valid.")
            continue

        print(forecast[pressure_trend_input])
        break

if __name__ == "__main__":
    make_menu()
    get_input()
