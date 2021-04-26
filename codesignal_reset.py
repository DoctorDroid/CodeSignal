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
    
"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
"""
def makeArrayConsecutive2(statues):
    in_order = sorted(statues)
    print(in_order)
    count = 0
    for i in range(len(in_order)-1):
        count += in_order[i+1]-in_order[i]-1
    return count