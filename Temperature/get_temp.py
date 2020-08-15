#!/usr/bin/env python3

"""
get_temp.py version 2.5
requires get_time.py
Python 3.7
"""

from bs4 import BeautifulSoup
from get_time import get_time
import requests
import time
from xlwt import Workbook
import sys


def get_temperature():
    """Gets temperature from the interwebs."""
    get_page = requests.get("http://bit.ly/3bqVxjP")
    soup = BeautifulSoup(get_page.content, "html.parser")
    get_temp = soup.find("p", {"class": "myforecast-current-lrg"})
    return get_temp


def format_temperature():
    """Formats temperature."""
    current_temp = "".join(get_temperature())
    temp = int(current_temp.strip("°F"))
    return temp


def main():
    """Writes temperature and time to .xls file at set interval."""
    seconds = 60
    col, row = 0, 0
    book = Workbook()
    sheet1 = book.add_sheet("Temperature")
    while True:
        this_time = get_time()
        print(f"Temperature recorded at: {this_time}", end="\r")

        try:
            sheet1.write(row, col, format_temperature())
            sheet1.write(row, col + 1, this_time)
            book.save("Temp.xls")
            row += 1
            time.sleep(seconds)
        except PermissionError:
            sys.exit("Please close the file.")


if __name__ == "__main__":
    sys.exit(main())
