#!/usr/bin/env python3

"""
plot_temp.py version 1.1
Python 3.7
"""

import sys
from matplotlib import pyplot as plt
import xlrd


def plot_temp():
    wb = xlrd.open_workbook("C:/Users/User/MyStuff/Temp.xls")
    sheet1 = wb.sheet_by_name("Temperature")

    time_x = sheet1.col_values(1)
    temp_y = sheet1.col_values(0)
    plt.title("Temperature by time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.plot(time_x, temp_y)

    plt.show()


if __name__ == "__main__":
    sys.exit(plot_temp())
