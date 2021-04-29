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
    using string slicing this checks to see if the string is 
    the same from beginning to end as it is from end to 
    beginning.
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
## shapeArea

Below we will define an n-interesting polygon. Your task is to 
find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 
1. An n-interesting polygon is obtained by taking the n - 1-
interesting polygon and appending 1-interesting polygons to 
its rim, side by side. 
"""

def shapeArea(n):
    return n*n + ((n-1)*(n-1))
    
"""
## makeArrayConsecutive2

Ratiorg got statues of different sizes as a present from CodeMaster 
for his birthday, each statue having an non-negative integer size. 
Since he likes to make things perfect, he wants to arrange them from 
smallest to largest so that each statue will be bigger than the 
previous one exactly by 1. He may need some additional statues to be 
able to accomplish that. Help him figure out the minimum number of 
additional statues needed.

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

"""
## almostIncreasingSequence

    Given a sequence of integers as an array, determine 
    whether it is possible to obtain a strictly increasing 
    sequence by removing no more than one element from the 
    array.

Note: sequence a0, a1, ..., an is considered to be a strictly 
increasing if a0 < a1 < ... < an. Sequence containing only one 
element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in 
order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing 
sequence [1, 2]. Alternately, you can remove 2 to get the 
strictly increasing sequence [1, 3].
"""
def almostIncreasingSequence(sequence):
    fails1 = 0
    fails2 = 0
    
    for i in range(len(sequence)-1):
            if sequence[i] >= sequence[i+1]:
                fails1 += 1
                
    for i in range(len(sequence)-2):
            if sequence[i] >= sequence[i+2]:
                fails2 += 1
                
    return (fails1 < 2) and (fails2 < 2)

"""
## matrixElementsSum

After becoming famous, the CodeBots decided to move into a new 
building together. Each of the rooms has a different cost, and 
some of them are free, but there's a rumour that all the free 
rooms are haunted! Since the CodeBots are quite superstitious, 
they refuse to stay in any of the free rooms, or any of the 
rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each 
value represents the cost of the room, your task is to return 
the total sum of all rooms that are suitable for the CodeBots 
(ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
matrixElementsSum(matrix) = 9.
"""

def matrixElementsSum(matrix):
    result = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0 and row+1 < len(matrix):
                matrix[row+1][col] = 0
            result += matrix[row][col]
    return result

"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""

def allLongestStrings(inputArray):
    longest = 0
    results = []
    for i in inputArray:
        if len(i) > longest:
            longest = len(i)
    for i in inputArray:
        if len(i) == longest:
            results.append(i)
    return results

"""
## commonCharacterCount

Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

"""
def commonCharacterCount(s1, s2):
    result = 0
    for i in set(s1):
        if i in s2:
            result += min(s1.count(i), s2.count(i))
    return result

"""
Ticket numbers usually consist of an even number of digits. A ticket 
number is considered lucky if the sum of the first half of the digits 
is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
"""
def isLucky(n):
    s = str(n)
    l = [int(x) for x in s] 
    return sum(l[:(len(l)//2)]) == sum(l[(len(l)//2):])