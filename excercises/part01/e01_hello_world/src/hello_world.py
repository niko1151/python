#!/usr/bin/env python3

# Everything after a hash sign (#) is considered a comment in Python

# The print statement could be written on the top-level (zero indentation),
# but here we have put it inside the main function.
# This enables TestMyCode (TMC) framework to work correctly.

# In more complicated programs it is good practise not to clutter the top-level of the program
# by using a main function as here.

def main():
    print("Hello, world!")
    # prints hello world

if __name__ == "__main__": 
    main()
