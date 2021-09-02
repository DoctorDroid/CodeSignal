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