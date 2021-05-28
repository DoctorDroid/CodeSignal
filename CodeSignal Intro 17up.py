# CodeSignal Intro problems

"""

You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3. 

"""

def arrayChange(inputArray):
    #Compare x[i] to x[i+1].  
    #If x[i] < x[i+1], pass.
    #Else, find the difference x[i]+1-x[i+1].  Add this 
    #difference to total and then set x[i+1] to x[i]+1
    x, total = inputArray, 0
    for i in range(len(x)-1):
        a,b = x[i], x[i+1]
        if a >= b:
            total += a + 1 - b
            x[i+1] = a + 1
    return total

"""
## palindromeRearranging

Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""


def palindromeRearranging(inputString):

    # count the number of each individual character
    # can form a palindrome only if:
    #   at most one of the character counts is odd, all others must be even
    first = 0
    for letter in set(inputString):
        if (inputString.count(letter) % 2 != 0):
            if len(inputString) % 2 == 1:
                if first:
                    return False
                else:    
                    first += 1
            else:
                return False
    return True

""" 
Call two arms equally strong if the heaviest weights they each are able to lift are equal.

Call two people equally strong if their strongest arms are equally strong (the strongest arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.
"""
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if ((yourLeft == friendsLeft) and (yourRight == friendsRight)) or ((yourLeft == friendsRight) and (yourRight == friendsLeft)):
        return True
    return False

""" 

## arrayMaximalAdjacentDifference

Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""
def arrayMaximalAdjacentDifference(inputArray):
    maxi = 0
    for i in range(1, len(inputArray)):
         if abs(inputArray[i] - inputArray[i-1]) > maxi:
             maxi = abs(inputArray[i] - inputArray[i-1])
    return maxi