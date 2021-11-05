#!/usr/bin/env python3
import re

def extract_numbers(s):
    l = []
    for t in s.split():
        try:
            l.append(int(t))
        except ValueError:
            try:
                l.append(float(t))
            except Exception:
                pass

    return l


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
