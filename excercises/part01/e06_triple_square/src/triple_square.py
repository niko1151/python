#!/usr/bin/env python3

triple = lambda a : a * 3
square = lambda a : a ** 2

def main():
    for x in range(1, 11):
        t = triple(x)
        s = square(x)
        if s > t:
            break
        
        print(f"triple({x})=={t} square({x})=={s}")




if __name__ == "__main__":
    main()
