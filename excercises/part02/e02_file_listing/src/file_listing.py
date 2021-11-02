#!/usr/bin/env python3

import re
import datetime


def file_listing(filename="src/listing.txt"):
    rows = filename.split("\n")
    new_rows = []

    for row in rows:
        row_data = row.split()
        mode = row_data[0]
        hardlink_count = row_data[1]
        user = row_data[2]
        group = row_data[3]
        size = row_data[4]
        month = row_data[5]
        day = row_data[6]
        hour = row_data[7]
        filename = row_data[8]
        # Also doable in a single line in Python 3 with:
        # mode, hardlink_count, user, group, size, month, day, time, *filename = row.split()
        new_rows.append((filename, size, month, day, hour))
        # You can use something similar if you need to transform the string date
        # into a date object:
        #new_rows.append((filename, size, datetime.datetime.strptime("{}-{} {}".format(month, day, hour), '%b-%d %H:%M')))

    return new_rows

def main():
    filepath = "C:\Users\Tec\Python-og-DataAnalyse-1\excercises\part02\e02_file_listing\src\listing.txt"
    file_listing(filepath)

if __name__ == "__main__":
    main()
