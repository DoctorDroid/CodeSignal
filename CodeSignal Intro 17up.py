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

""" 

## isIPv4Address


An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.
"""


    def isIPv4Address(inputString):
        l=inputString.split('.')
        if len(l)!=4:
            return False
        for i in range(len(l)):
            if l[i]=='':
                return False
            if l[i].isdecimal()==False:
                return False
            if l[i]!=str(int(l[i])):
                return False
            if int(l[i])>255:
                return False
        return True


""" 

## avoidObstacles


You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.
"""
def avoidObstacles(inputArray):
    start = 0
    increment = 1
    while (start < max(inputArray)):
        start += increment
        if start in inputArray:
            start = 0
            increment += 1
    return increment