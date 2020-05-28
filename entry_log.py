#!/usr/bin/env python3

"""
entry_log version 1.6
Python 3.7
"""

import os


def entry(unit_choice):
    """Log user entry and indicate most common entry."""
    if unit_choice < '10':
        log_entry = unit_choice
        with open('prompt_log.txt', 'a') as f:
            f.write(log_entry)
            read_log = open('prompt_log.txt').read()
 
            if os.stat('prompt_log.txt').st_size == 0:
                print('No choices made.')
            else:
                most_common = max(read_log, key=read_log.count)
                print(f'\nYour most common choice: {most_common}.')


if __name__ == "__main__":
    entry(unit_choice)
