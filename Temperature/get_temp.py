#!/usr/bin/env python3
"""
get_temp.py version 2.1
Python 3.7
"""

from bs4 import BeautifulSoup
import get_time
import requests
import time
from xlwt import Workbook


def get_temperature():
    """Gets temperature from the interwebs and formats it."""
    get_page = requests.get("http://bit.ly/3bqVxjP")
    soup = BeautifulSoup(get_page.content, "html.parser")
    get_temp = soup.find("p", {"class": "myforecast-current-lrg"})


    # Formats temperature.
    current_temp = "".join(get_temp)
    temp_list = list(current_temp)
    trim_characters = [s for s in temp_list if s not in ["°", "F"]]
    temp = int("".join(trim_characters))
    return temp


def write_temperature():
    """Writes temperature and time to .xls file at set interval."""
    seconds = 60
    col, row = 0, 0
    book = Workbook()
    sheet1 = book.add_sheet("Temperature")
    while True:
        this_time = get_time.get_time()
        print(f"Temperature recorded at: {this_time}", end="\r")
        try:
            sheet1.write(row, col, get_temperature())
            sheet1.write(row, col + 1, this_time)
            book.save("Temp.xls")
            row += 1
            time.sleep(seconds)
        except PermissionError:
            print("Please close the file.")
            raise SystemExit


if __name__ == "__main__":
    write_temperature()
