# Enter you module contents here
"""Hvad skal jeg skrive."""
from math import sqrt
__version__ = '1.0.0'
__author__ = 'Nikolai'


def hypothenuse(x, y):
    '''Udregner hypotenusen'''
    a = sqrt(x**2 + y**2)
    return a

def area(x, y):
    '''Udregner areal'''
    a = (x * y) / 2
    return a