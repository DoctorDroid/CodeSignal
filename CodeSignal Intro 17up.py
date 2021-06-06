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

""" 

## boxBlur
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: 
(1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. 
The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
the output should be

boxBlur(image) = [[5, 4], 
                  [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four integers 
in the blurred output. To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) =
 47 / 9 = 5.2222 = 5. The other three integers are obtained the same way, then the 
 surrounding integers are cropped from the final result.
"""

def boxBlur(image):
    result = []
    for i in range(len(image)-2):
        result.append([])
        for j in range(len(image[0])-2):
            result[i].append(sum(image[i][j:j+3] + image[i+1][j:j+3] + image[i+2][j:j+3])/9//1)
    return result

"""

## minesweeper

    In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
"""

def minesweeper(M):
    A =[[0]*(len(M[0])+2)] + [[0]+x+[0] for x in M] + [[0]*(len(M[0])+2)] #creates padding of zeros 
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = (A[i+0][j] + A[i+0][j+1] + A[i+0][j+2] + # replaces each cell in M with number
                       A[i+1][j] +      0      + A[i+1][j+2] + # of neighboring mines (without index
                       A[i+2][j] + A[i+2][j+1] + A[i+2][j+2] ) # going out of range)
    return M

"""

## arrayReplace

Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

"""

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray

    """evenDigitsOnly
    Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
evenDigitsOnly(n) = true;
For n = 642386, the output should be
evenDigitsOnly(n) = false.
    """

def evenDigitsOnly(n):
    s = str(n)
    return all([int(i) % 2 == 0 for i in s])

    """variableName

    Correct variable names consist only of English letters, digits and underscores and they can't start with a digit.

Check if the given string is a correct variable name.

Example

For name = "var_1__Int", the output should be
variableName(name) = true;
For name = "qq-q", the output should be
variableName(name) = false;
For name = "2w2", the output should be
variableName(name) = false.
    """
import string
def variableName(name):
    # return name.isidentifier()
    if name[0] in ['0','1','2','3','4','5','6','7','8','9']:
        return False
    if name.replace('_', '0').isalnum() == False:
        return False
    return True
    
 """
 ## chessBoardCellColor

Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.
 """   
def chessBoardCellColor(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1]))%2 == (ord(cell2[0]) + int(cell2[1]))%2

"""
    ##circleOfNumbers

    Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
circleOfNumbers(n, firstNumber) = 7.
 """

def circleOfNumbers(n, firstNumber):
    if firstNumber == n/2:
        return 0
    if firstNumber < n/2:
        return firstNumber+ n/2
    return firstNumber- n/2
    """
    ## depositProfit

    You have deposited a specific amount of money into your bank account. Each year your balance increases at the same growth rate. With the assumption that you don't make any additional deposits, find out how long it would take for your balance to pass a specific threshold.

Example

For deposit = 100, rate = 20, and threshold = 170, the output should be
depositProfit(deposit, rate, threshold) = 3.

Each year the amount of money in your account increases by 20%. So throughout the years, your balance would be:

year 0: 100;
year 1: 120;
year 2: 144;
year 3: 172.8.
Thus, it will take 3 years for your balance to pass the threshold, so the answer is 3.
    """
def depositProfit(deposit, rate, threshold):
    count = 0
    while deposit < threshold:
        deposit += deposit * (rate/100)
        count += 1
    return count

""" 
## absoluteValuesSumMinimization

Given a sorted array of integers a, your task is to determine which element of a is closest to all other values of a. In other words, find the element x in a, which minimizes the following sum:

abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
(where abs denotes the absolute value)

If there are several possible answers, output the smallest one.

Example

For a = [2, 4, 7], the output should be absoluteValuesSumMinimization(a) = 4.

for x = 2, the value will be abs(2 - 2) + abs(4 - 2) + abs(7 - 2) = 7.
for x = 4, the value will be abs(2 - 4) + abs(4 - 4) + abs(7 - 4) = 5.
for x = 7, the value will be abs(2 - 7) + abs(4 - 7) + abs(7 - 7) = 8.
The lowest possible value is when x = 4, so the answer is 4.

For a = [2, 3], the output should be absoluteValuesSumMinimization(a) = 2.

for x = 2, the value will be abs(2 - 2) + abs(3 - 2) = 1.
for x = 3, the value will be abs(2 - 3) + abs(3 - 3) = 1.
Because there is a tie, the smallest x between x = 2 and x = 3 is the answer.
"""

def absoluteValuesSumMinimization(a):
    lst = []
    sums = []
    for x in a:
        lst.append([abs(x - c) for c in a]) # list of lists of abs
    for i in range(len(lst)):
        sums.append(sum(lst[i]))            # list of sums
    for j in range(len(sums)):              # find min sum
        if sums[j] == min(sums):
            return a[j]          # return element at matching index


""" 
fewer lines, less readable
"""
def absoluteValuesSumMinimization(a):
    sums = []
    for x in a:
        sums.append(sum([abs(x - c) for c in a])) # list of sums 
    return a[sums.index(min(sums))]