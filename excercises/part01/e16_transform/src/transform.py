#!/usr/bin/env python3

def transform(s1, s2):
    #res_list = []
    l1 = list(map(int, s1.split()))
    l2 = list(map(int, s2.split()))

    x = [a * b for a, b in zip(l1, l2)]

    return x

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()