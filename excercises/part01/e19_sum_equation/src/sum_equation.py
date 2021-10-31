#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
            s = "0 = 0"
    else: 
        s = "+".join([str(n) for n in L])
        s =  " = " + str(sum(L))
    return s


def main():
    sum_equation([1,5,7])
    sum_equation([])
    sum_equation([1,5,7,9,13,55,65,246,8])


if __name__ == "__main__":
    main()
