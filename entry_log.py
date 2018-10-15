#!/usr/bin/env python3
'''By Micah M. 2018
   entry_log version 1.1
   Python 3.7'''

import os

def entry(unit_choice):
    '''Log user entry and indicate most common entry.'''
    log_entry = unit_choice
    file = open('promptLog.txt', 'a')
    file.write(log_entry)
    read_log = open('promptLog.txt').read()
    if os.stat('promptLog.txt').st_size == 0:
        print('No choices made yet.')
    else:
        most_common = max(read_log, key=read_log.count) # Finds most common entry.
        print(f'\nYour most common choice: {most_common}.')
    file.close()


if __name__ == "__main__":
    entry(unit_choice)
