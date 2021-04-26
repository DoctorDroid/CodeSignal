# -*- coding: utf-8 -*-
"""CodeSignal Intro

## centuryFromYear

Given a year, return the century it is in. The first century 
spans from the year 1 up to and including the year 100, the 
second - from the year 101 up to and including the year 200, 
etc.
"""

def centuryFromYear(year):
    return year//100 + (year%100 != 0)
    """
    this solution utilizes floor division and boolean values as
    part of a mathematical expression.
    """
"""    
## checkPalindrome

Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
"""

def checkPalindrome(inputString):
    return inputString == inputString[::-1]

    """
    using string slicing this checks to see if the string is the same from beggining to end as it is
    from end to beggining.
    """

""" 
## adjacentElementsProduct

Given an array of integers, find the pair of adjacent elements 
that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
"""
def adjacentElementsProduct(inputArray):
    largest_product = inputArray[0] * inputArray[1]
    for i in range(1,len(inputArray) - 1):
        if inputArray[i] * inputArray[i+1] > largest_product:
            largest_product = inputArray[i] * inputArray[i+1]
    return largest_product

"""
Below we will define an n-interesting polygon. Your task is to 
find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 
1. An n-interesting polygon is obtained by taking the n - 1-
interesting polygon and appending 1-interesting polygons to its rim,
 side by side. 
"""

def shapeArea(n):
    return n*n + ((n-1)*(n-1))