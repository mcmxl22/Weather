"""
Author: M. McConnaughey
pressure_forecast version 2.0
Date: 12/08/2023
Python 3.7
"""


def make_menu():
    """Make a list of menu items."""
    trend_options = ["1 Rising", "2 Falling", "3 Steady"]
    for i in trend_options:
        print(i)

def get_forecast():
    """Get forecasts based on barometric pressure trends."""
    forecast_dict = {
        1: "Fairer weather on the way.",
        2: "Poorer weather on the way.",
        3: "No significant change.",
    }
    return forecast_dict

def get_input():
    forecast = get_forecast()
    while True:
        try:
            pressure_trend = int(input("\nChoose a trend (or enter 4 to exit): "))
            if pressure_trend not in forecast:
                if pressure_trend == 4:
                    break
                print(f"Option {pressure_trend} is not valid.")
                continue
            print(forecast[pressure_trend])
            break
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    make_menu()
    get_input()
