# CodeSignal Intro problems

"""

You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3. 

"""
]
def checkArray(arr):
    for i in range(len(arr)):
        if arr[i]<=arr[i+1]:
            return False
    return True
    
def arrayChange(inputArray):
    moves = 0
    i = 0
    while checkArray(inputArray) is False:
        i +=1
        while i < len(inputArray)-1:
            while inputArray[i]>=inputArray[i+1]:
                inputArray[i+1] +=1
                moves +=1
    return moves

