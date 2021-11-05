#!/usr/bin/env python3
import re

def main():
    # Her har jeg lavet et double for loop for at udregne alle muligheder for de 2 terninger 
       for x in range(1, 7):
        for y in range(1, 7):
            # derefter kigger den efter resultater der er 5
            if x + y == 5:
                mydata = '({},{})'
                print(mydata.format(x,y))

if __name__ == "__main__":
    main()
