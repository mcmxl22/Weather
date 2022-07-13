#!/usr/bin/env python3

"""
Author: M. McConnaughey
get_time.py version 1.2
Date: 07/13/2022
Python 3.7+
"""

from datetime import datetime


def get_time():
    """Get time of day."""
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


if __name__ == "__main__":
    get_time()
