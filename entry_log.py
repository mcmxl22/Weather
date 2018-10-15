#!/usr/bin/env python3
'''By Micah M. 2018
   entry_log version 1
   Python 3.7'''

import os

def entry_log(unit_choice):
   '''Log user entry and sugest most common entry.'''
    log_entry = unit_choice  # Logs choice.
    file = open('promptLog.txt', 'a')
    file.write(log_entry)  # Writes log to file.
    read_log = open('promptLog.txt').read()  # Reads log from file.
    if os.stat('promptLog.txt').st_size == 0:
        print('No choices made yet.')
    else:
        most_common = max(read_log, key=read_log.count) # Finds most common entry.
        print(f'\nYour most common choice: {most_common}.')
    file.close()


if __name__ == "__main__":
    entry_log()
