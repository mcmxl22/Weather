#!/usr/bin/env python3
"""beaufort version 1
   Python 3.7.2"""


SCALE = {'0': 'Calm', '1': 'Light air', '2': 'Light breeze',
         '3': 'Gentle breeze', '4': 'Moderate breeze',
         '5': 'Fresh Breeze', '6': 'Strong breeze',
         '7': 'Moderate gale', '8': 'Fresh gale',
         '9': 'Strong gale', '10': 'Whole gale', '11': 'Storm',
         '12': 'Hurricane force'}

def scale_wind(wind_speed):
    """Prints Beaufort scale description of wind speeds."""
    wind_speed = int(input('Enter wind speed. '))

    if wind_speed == 0:
        print(SCALE['0'])
    elif wind_speed in range(1, 4):
        print(SCALE['1'])
    elif wind_speed in range(4, 8):
        print(SCALE['2'])
    elif wind_speed in range(8, 13):
        print(SCALE['3'])
    elif wind_speed in range(13, 19):
        print(SCALE['4'])
    elif wind_speed in range(19, 25):
        print(SCALE['5'])
    elif wind_speed in range(25, 32):
        print(SCALE['6'])
    elif wind_speed in range(32, 39):
        print(SCALE['7'])
    elif wind_speed in range(39, 47):
        print(SCALE['8'])
    elif wind_speed in range(47, 55):
        print(SCALE['9'])
    elif wind_speed in range(55, 64):
        print(SCALE['10'])
    elif wind_speed in range(64, 73):
        print(SCALE['11'])
    elif wind_speed > 72:
        print(SCALE['12'])
    else:
        print('Invalid Entry!')

if __name__ == "__main__":
    scale_wind('wind_speed')
