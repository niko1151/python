#!/usr/bin/env python3


def main():
    # her laver jeg et double loop for at kunne lave en gange tabel som passer
    for x in range(1, 11):
        for y in range(1, 11):
            z = x * y
            print(z, end="\t")
        print()
    

if __name__ == "__main__":
    main()
