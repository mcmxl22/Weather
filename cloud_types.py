#!/usr/bin/env python3

"""
Author: M McConnaughey
cloud_types version 1.7
Requires numli.py
Python 3.7
Date: 07/12/2022
"""

import webbrowser

def make_menu():
    """Make a menu of cloud types."""
    cloud_types = ["Cumulus", "Stratus", "Cumulonimbus", "Cirrus"]
    for c, value in enumerate(cloud_types, 1):
            print(c, value)


def view_clouds():
    """view images of cloud types"""
    make_menu()
    img_dict = {
        1: "https://bit.ly/2xH55Er",
        2: "https://bit.ly/2xxD42N",
        3: "https://bit.ly/2Nwns9V",
        4: "https://bit.ly/2xMDgKG",
    }

    try:
        view = int(input("Choose an option. "))
    except ValueError:
        print("Please enter a number.")
        view_clouds()
    else:
        webbrowser.open(img_dict.get(view))


def get_cloud_information():
    """Get informayion about cloud tyoes."""
    make_menu()
    cloud_descriptions = {
        1: "https://en.wikipedia.org/wiki/Cumulus_cloud",
        2: "https://en.wikipedia.org/wiki/Stratus_cloud",
        3: "https://en.wikipedia.org/wiki/Cumulonimbus_cloud",
        4: "https://en.wikipedia.org/wiki/Cirrus_cloud",
    }

    try:
        description = int(input("Choose an option. "))
    except ValueError:
        print("Please enter a number.")
        get_cloud_information()
    else:
        webbrowser.open(cloud_descriptions.get(description))


def cloud_main():
    """Explore the clouds."""
    cloud_choices = ["View clouds", "Cloud information"]
    for c, value in enumerate(cloud_choices, 1):
        print(c, value)
    choice = int(input("Choose an option. "))

    if choice == 1:
        view_clouds()
    elif choice == 2:
        get_cloud_information()
    else:
        print("Please enter a number.")
        cloud_main()


if __name__ == "__main__":
    cloud_main()
