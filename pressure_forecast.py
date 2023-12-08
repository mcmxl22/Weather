"""
Author: M. McConnaughey
pressure_forecast version 1.9
Date: 12/07/2023
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

    try:
        pressure_trend = int(input("\nChoose a trend. "))
    except ValueError:
        print("Please enter a number.")
        get_forecast()
    else:
        print(forecast_dict.get(pressure_trend))


if __name__ == "__main__":
    make_menu()
    get_forecast()
