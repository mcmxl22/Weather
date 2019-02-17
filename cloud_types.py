#!/usr/bin/env python
"""By Micah M. 2019
   cloud_types version 1.4
   Python 3.7.1"""

import webbrowser


def clouds(options):
    """View information on cloud types."""
    cloud_types = ['1 Cumulus', '2 Stratus', '3 Cumulonimbus', '4 Cirrus']
    cloud_options = ['1 Cloud descriptions', '2 Cloud images']
    print('\n'.join(cloud_options))
    options = input('Choose an option. ')

    if options in '1':

        print('\n'.join(cloud_types))
        description = input('Choose an option. ')

        if description in '1':
            url = 'https://en.wikipedia.org/wiki/Cumulus_cloud'
            webbrowser.open(url)
        elif description in '2':
            url = 'https://en.wikipedia.org/wiki/Stratus_cloud'
            webbrowser.open(url)
        elif description in '3':
            url = 'https://en.wikipedia.org/wiki/Cumulonimbus_cloud'
            webbrowser.open(url)
        elif description in '4':
            url = 'https://en.wikipedia.org/wiki/Cirrus_cloud'
            webbrowser.open(url)
        else:
            print('Invalid Answer.')

    elif options in '2':

        print('\n'.join(cloud_types))
        img = input('Choose an option. ')

        if img in '1':
            url = 'https://bit.ly/2xH55Er'
            webbrowser.open(url)
        elif img in '2':
            url = 'https://bit.ly/2xxD42N'
            webbrowser.open(url)
        elif img in '3':
            url = 'https://bit.ly/2Nwns9V'
            webbrowser.open(url)
        elif img in '4':
            url = 'https://bit.ly/2xMDgKG'
            webbrowser.open(url)

        else:
            print('Invalid Answer.')

    else:
        print('Invalid Answer.')


if __name__ == "__main__":
    clouds('options')
