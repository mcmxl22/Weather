#!/usr/bin/env python3
"""
cloud_types version 1.4
Python 3.7
"""

import numli
import webbrowser


def clouds(options):
    """View information on cloud types."""

    cloud_types = ["Cumulus", "Stratus", "Cumulonimbus", "Cirrus"]
    cloud_options = ["Cloud descriptions", "Cloud images"]
    invalid = "Invalid Answer!"
    numli.addnum(cloud_options)
    cloud_options = input("Choose an option. ")

    if cloud_options in "1":
        numli.addnum(cloud_types)
        description = input("Choose an option. ")

        description_dict = {
            "1": "https://en.wikipedia.org/wiki/Cumulus_cloud",
            "2": "https://en.wikipedia.org/wiki/Stratus_cloud",
            "3": "https://en.wikipedia.org/wiki/Cumulonimbus_cloud",
            "4": "https://en.wikipedia.org/wiki/Cirrus_cloud"
        }

        if description in description_dict:
            webbrowser.open(description_dict[description])

        else:
            print(invalid)


    elif cloud_options in "2":
        numli.addnum(cloud_types)
        img_choice = input("Choose an option. ")

        img_dict = {
            "1": "https://bit.ly/2xH55Er",
            "2": "https://bit.ly/2xxD42N",
            "3": "https://bit.ly/2Nwns9V",
            "4": "https://bit.ly/2xMDgKG"
        }

        if img_choice in img_dict:
            webbrowser.open(img_dict[img_choice])

        else:
            print(invalid)

    else:
        print(invalid)


if __name__ == "__main__":
    clouds("options")
