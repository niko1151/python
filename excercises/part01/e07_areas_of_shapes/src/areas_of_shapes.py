#!/usr/bin/env python3

import math


def main():
    shapes = "triangle rectangle circle".split()
    while(True):
        shape=input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle" :
            Tbase=input("Give base of the triangle: ")
            Theight=input("Give height of the triangle: ")
            area = Theight * Tbase
            print(f"The area is {area:.6f}")
        if shape == "rectangle" :
            Rwidth=input("Give width of the rectangle: ")
            Rheight=input("Give height of the rectangle: ")
            area = Rwidth * Rheight
            print(f"The area is {area:.6f}")
        if shape == "circle" :
            PI = 3.14
            r = float(input("Give radius of the circle:"))
            area = PI * r * r
            print(f"The area is {area:.6f}")
        if not shape in shapes:
            if shape == "":
                break
            else:
                print("Unknown shape!")





if __name__ == "__main__":
    main()


