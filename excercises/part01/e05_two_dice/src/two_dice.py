#!/usr/bin/env python3
import re

def main():
       for x in range(1, 7):
        for y in range(1, 7):
            if x + y == 5:
                mydata = '({},{})'
                print(mydata.format(x,y))

if __name__ == "__main__":
    main()
