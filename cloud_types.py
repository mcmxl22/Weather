#!/usr/bin/env python3

"""
Author: M McConnaughey
cloud_types version 1.8
Python 3.7
Date: 5/21/2024
"""

import webbrowser

def make_menu(cloud_types):
    """Display a menu of cloud types."""
    for c, value in enumerate(cloud_types, 1):
        print(f"{c}. {value}")

def view_clouds():
    """View images of cloud types."""
    cloud_types = ["Cumulus", "Stratus", "Cumulonimbus", "Cirrus"]
    make_menu(cloud_types)
    img_dict = {
        1: "https://bit.ly/2xH55Er",
        2: "https://bit.ly/2xxD42N",
        3: "https://bit.ly/2Nwns9V",
        4: "https://bit.ly/2xMDgKG",
    }

    try:
        view = int(input("Choose an option (1-4): "))
        if view in img_dict:
            webbrowser.open(img_dict[view])
        else:
            print("Invalid option. Please choose a number between 1 and 4.")
            view_clouds()
    except ValueError:
        print("Invalid input. Please enter a number.")
        view_clouds()

def get_cloud_information():
    """Get information about cloud types."""
    cloud_types = ["Cumulus", "Stratus", "Cumulonimbus", "Cirrus"]
    make_menu(cloud_types)
    cloud_descriptions = {
        1: "https://en.wikipedia.org/wiki/Cumulus_cloud",
        2: "https://en.wikipedia.org/wiki/Stratus_cloud",
        3: "https://en.wikipedia.org/wiki/Cumulonimbus_cloud",
        4: "https://en.wikipedia.org/wiki/Cirrus_cloud",
    }

    try:
        description = int(input("Choose an option (1-4): "))
        if description in cloud_descriptions:
            webbrowser.open(cloud_descriptions[description])
        else:
            print("Invalid option. Please choose a number between 1 and 4.")
            get_cloud_information()
    except ValueError:
        print("Invalid input. Please enter a number.")
        get_cloud_information()

def cloud_main():
    """Explore the clouds."""
    cloud_choices = ["View clouds", "Cloud information"]
    for c, value in enumerate(cloud_choices, 1):
        print(f"{c}. {value}")
    
    try:
        choice = int(input("Choose an option (1-2): "))
        if choice == 1:
            view_clouds()
        elif choice == 2:
            get_cloud_information()
        else:
            print("Invalid option. Please choose 1 or 2.")
            cloud_main()
    except ValueError:
        print("Invalid input. Please enter a number.")
        cloud_main()

if __name__ == "__main__":
    cloud_main()
