#!/usr/bin/env python3

def find_matching(L, pattern):
    return [s for s, x in enumerate(L) if pattern in x]

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
