#!/usr/bin/env python3

"""
Author: M. McConnaughey
plot_temp.py version 1.2
Date: 07/13/2022
Python 3.7+
"""

from matplotlib import pyplot as plt
import xlrd


def plot_temp():
    """Plot the temperature from the .xls file."""
    wb = xlrd.open_workbook("Temp.xls")
    sheet1 = wb.sheet_by_name("Temperature")
    time_x = sheet1.col_values(1)
    temp_y = sheet1.col_values(0)
    plt.title("Time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.plot(time_x, temp_y)
    plt.show()


if __name__ == "__main__":
    plot_temp()
