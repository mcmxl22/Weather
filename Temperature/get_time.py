#!/usr/bin/env python3
from datetime import datetime


def get_time():
    """Gets time of day."""
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


if __name__ == "__main__":
    get_time()
