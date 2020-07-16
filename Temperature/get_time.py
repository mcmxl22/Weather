#!/usr/bin/env python3

"""
get_time.py version 1.1
Python 3.7
"""

import sys
from datetime import datetime


def get_time():
    """Gets time of day."""
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


if __name__ == "__main__":
    sys.exit(get_time())
