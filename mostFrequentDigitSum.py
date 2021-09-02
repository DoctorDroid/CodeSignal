# https://app.codesignal.com/arcade/code-arcade/mirror-lake/RpoP4Aqa5mbmC8koC
#  A step(x) operation works like this: it changes a number x into x - s(x),
#  where s(x) is the sum of x's digits. You like applying functions to numbers,
#  so given the number n, you decide to build a decreasing sequence of numbers:
#  n, step(n), step(step(n)), etc., with 0 as the last element.

# Building a single sequence isn't enough for you, so you replace all elements
#  of the sequence with the sums of their digits (s(x)). Now you're curious as
#  to which number appears in the new sequence most often. If there are several
#  answers, return the maximal one.

# Example

# For n = 88, the output should be
# mostFrequentDigitSum(n) = 9.

# Here is the first sequence you built: 88, 72, 63, 54, 45, 36, 27, 18, 9, 0;
# And here is s(x) for each of its elements: 16, 9, 9, 9, 9, 9, 9, 9, 9, 0.
# As you can see, the most frequent number in the second sequence is 9.

# For n = 8, the output should be
# mostFrequentDigitSum(n) = 8.

# At first you built the following sequence: 8, 0
# s(x) for each of its elements is: 8, 0
# As you can see, the answer is 8 (it appears as often as 0, but is greater than it).

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer n

# Guaranteed constraints:
# 1 ≤ n ≤ 105.

# [output] integer

# The most frequent number in the sequence s(n), s(step(n)), s(step(step(n))), etc.
# Function to get sum of digits 
def getSum(n):
    sum = 0
    while (n != 0):
        sum += (n % 10) # remainder 
        n = n//10       # chops off last digit
    return sum

def mostFrequentDigitSum(n):
    steps = [n] #begin steps list with n
    sums_list = [] #intitialize all other vars to empty or 0
    counts = {}
    max_count = 0
    max_sum = 0
    while n != 0: #build step list
        steps.append(n - getSum(n))
        n = steps[-1]
    for each in steps:
        sums_list.append(getSum(each)) #build sum list
    for each in sums_list:
        if each in counts: #count sums
            counts[each] += 1
        else:
            counts[each] = 0
    for key in counts: #find highest count(s)
        if counts[key] > max_count:
            max_count = counts[key]
    for i in range(len(steps)): 
        if counts[sums_list[i]] == max_count: #search for highest counts
            if sums_list[i] > max_sum:
                max_sum = sums_list[i] #assign highest sum value to return
    return max_sum


# def mostFrequentDigitSum(n):
#     return 18 if n>=999 else 9 if n>=9 else n


# top answer on CodeSignal... these guys had to discover this math trick after finding the solutions first. 