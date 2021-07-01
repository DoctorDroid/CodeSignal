# CodeSignal Intro problems

"""

You are given an array of integers. On each move you are allowed to increase exactly
 one of its element by one. Find the minimal number of moves required to obtain a 
 strictly increasing sequence from the input.

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

Call two people equally strong if their strongest arms are equally strong (the strongest 
arm can be both the right and the left), and so are their weakest arms.

Given your and your friend's arms' lifting capabilities find out if you two are equally 
strong.

Example

For yourLeft = 10, yourRight = 15, friendsLeft = 15, and friendsRight = 10, the output 
should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 10, the output
 should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
For yourLeft = 15, yourRight = 10, friendsLeft = 15, and friendsRight = 9, the output
 should be
areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false.
"""
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if ((yourLeft == friendsLeft) and (yourRight == friendsRight)) \
        or ((yourLeft == friendsRight) and (yourRight == friendsLeft)):
        return True
    return False

""" 

## arrayMaximalAdjacentDifference

Given an array of integers, find the maximal absolute difference between any two of its 
adjacent elements.

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


An IP address is a numerical label assigned to each device (e.g., computer, printer) 
participating in a computer network that uses the Internet Protocol for communication.
 There are two versions of the Internet protocol, and thus two versions of addresses.
  One of them is the IPv4 address.

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


You are given an array of integers representing coordinates of obstacles situated on a 
straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are 
allowed only to make jumps of the same length represented by some integer.

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
Last night you partied a little too hard. Now there's a black and white photo of you
that's about to go viral! You can't let this ruin your reputation, so you want to 
apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the
input image in the following way: Every pixel x in the output image has a value equal 
to the average value of the pixel values from the 3 × 3 square that has its center at 
x, including x itself. All the pixels on the border of x are then removed.

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
            result[i].append(sum(image[i][j:j+3] + image[i+1][j:j+3] + \
            image[i+2][j:j+3])/9//1)
    return result

"""

## minesweeper

    In the popular Minesweeper game you have a board with some mines and those 
    cells that don't contain a mine have a number in it that indicates the total 
    number of mines in the neighboring cells. Starting off with some arrangement
     of mines we want to create a Minesweeper game setup.

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
    A =[[0]*(len(M[0])+2)] + [[0]+x+[0] for x in M] + [[0]*(len(M[0])+2)] 
    #creates padding of zeros 
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = (A[i+0][j] + A[i+0][j+1] + A[i+0][j+2] + 
            
                       A[i+1][j] +      0      + A[i+1][j+2] + 
                       
                       A[i+2][j] + A[i+2][j+1] + A[i+2][j+2] ) 
                       # replaces each cell in M with number
                       # of neighboring mines (without index
                       # going out of range)
    return M

"""

## arrayReplace

Given an array of integers, replace all the occurrences of elemToReplace with 
substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the 
output should be arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].

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

    Correct variable names consist only of English letters, digits and underscores and 
    they can't start with a digit.

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

Given two cells on the standard chess board, determine whether they have the same color or 
not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.
 """   
def chessBoardCellColor(cell1, cell2):
    return (ord(cell1[0]) + int(cell1[1]))%2 == (ord(cell2[0]) + int(cell2[1]))%2

"""
    ##circleOfNumbers

    Consider integer numbers from 0 to n - 1 written down along the circle in such a way 
    that the distance between any two neighboring numbers is equal (note that 0 and n - 1
     are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position 
to firstNumber.

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

    You have deposited a specific amount of money into your bank account. Each year your 
    balance increases at the same growth rate. With the assumption that you don't make 
    any additional deposits, find out how long it would take for your balance to pass a 
    specific threshold.

Example

For deposit = 100, rate = 20, and threshold = 170, the output should be
depositProfit(deposit, rate, threshold) = 3.

Each year the amount of money in your account increases by 20%. So throughout the years, 
your balance would be:

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

Given a sorted array of integers a, your task is to determine which element of a is 
closest to all other values of a. In other words, find the element x in a, which 
minimizes the following sum:

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

"""

## extractEachKth

Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
"""

def extractEachKth(inputArray, k):
    k = k-1
    if k == 0:
        return[]
    for i in range(k,len(inputArray),k):
        if i < len(inputArray):
            del inputArray[i]
    return inputArray

""" what I tried first but with improper syntax """
def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray

""" 
Example

For inputString = "var_1__Int", the output should be
firstDigit(inputString) = '1';
For inputString = "q2q-q", the output should be
firstDigit(inputString) = '2';
For inputString = "0ss", the output should be
firstDigit(inputString) = '0'.
"""

def firstDigit(inputString):
    for i in inputString:
        if '0' <= i <= '9':
            return i

""" 
Given array of integers, find the maximal possible sum of some of its k consecutive
elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
"""
def arrayMaxConsecutiveSum(inputArray, k):
    ans = temp = sum(inputArray[:k]) #sum a slice
    for i in range(len(inputArray)-k):
        temp += inputArray[i+k] - inputArray[i] # move 1 in from back and 1 out from front
        if temp > ans:
            ans = temp
    return ans

""" 
Caring for a plant can be hard work, but since you tend to it regularly, you have a plant 
that grows consistently. Each day, its height increases by a fixed amount represented by 
the integer upSpeed. But due to lack of sunlight, the plant decreases in height every 
night, by an amount represented by downSpeed.

Since you grew the plant from a seed, it started at height 0 initially. Given an integer 
desiredHeight, your task is to find how many days it'll take for the plant to reach this
height.

Example

For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be
growingPlant(upSpeed, downSpeed, desiredHeight) = 10.

#	Day	Night
1	100	90
2	190	180
3	280	270
4	370	360
5	460	450
6	550	540
7	640	630
8	730	720
9	820	810
10	910	900
The plant first reaches a height of 910 on day 10.
"""

def growingPlant(upSpeed, downSpeed, desiredHeight):
    h = 0
    days = 0
    while h < desiredHeight:
        days += 1
        h += upSpeed
        if h >= desiredHeight:
            return days
        h -= downSpeed

""" 
Let's define digit degree of some positive integer as the number of times we need to 
]replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;
For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
"""

def digitDegree(n):
    count = 0
    while n > 9:
        n = sum([int(digit) for digit in (str(n))]) #simple casting would not work here
        count += 1                                  #without an additional loop. list comp
    return count                                    #instead.


""" 
*
Given a string, find the shortest possible string which can be achieved by adding 
characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""

def buildPalindrome(st):
    end = ""
    i = 0
    while st + end != (st + end)[::-1]:
        end = st[i] + end
        i+=1
    return st + end

import string
def isMAC48Address(inputString):
    lis = inputString.split('-')
    if len(lis) != 6:
        return False
    print(lis)
    h = 0
    for elem in lis:
        for i in range(len(elem)):
            if elem[i].isdigit() or (elem[i] >= 'A' and elem[i] <= 'F'):
                h += 1
    return h == 12 

"""
only coide that passes the last hidden test without using regular expressions. 
still unsure why.

"""
    # if inputString.count("-")!=5:
    #     return False
    # for i in inputString.split("-"):
    #     for j in i:
    #         if j>"F" or (j<"A" and not j.isdigit()) or len(i)!=2:
    #             return False
    # return True 
"""
passes all sample and 19/20 hidden
"""
    
    # lst = inputString.split('-')
    # if len(lst) != 6:
    #     return False
    # for each in lst:
    #     if each[0] not in set(string.hexdigits) or each[1] not in set(string.hexdigits):
    #         return False
            
        # if '9' < each[0] < '0':
        #     return False    
        # elif each[0] < 'A' or each[0] > 'F':
        #     return False
        # if '9' < each[1] < '0':
        #     return False
        # elif each[1] < 'A' or each[1] > 'F':
        #     return False
        
    #return True

"""
passes all sample, no hidden
"""

"""
Given a rectangular matrix containing only digits, calculate the number of 
different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2
2 1
2 2
2 2
2 2
2 2
1 2
2 2
2 3
2 3
2 1


2 are identical therfore are not counted.
"""

def differentSquares(matrix):
    set_ms = set()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            set_ms.add((matrix[i][j], matrix[i+1][j],matrix[i][j+1],matrix[i+1][j+1]))
    return len(set_ms)