#!/usr/bin/env python3

def main():
    # Giver num en værdi på 4
    num = 4

    # her laver jeg et for loop hvor jeg har brugt en range til at angive max længden på mit loop
    for i in range(0, 11):
        print(num, 'multiplied by', i, 'is', num*i)


if __name__ == "__main__":
    main()
