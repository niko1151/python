#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
      with open('src/rgb.txt') as f:
        for line in f:
            line = f.read()
            regex = re.findall(r"[ \t]*(\d+)[ \t]*(\d+)[ \t]*(\d+)[ \t]*(.*)", line)
            string_list = list(map('\t'.join, regex))
            print(string_list)
        return string_list

def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()
