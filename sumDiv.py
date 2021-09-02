def sumsDivisibleByK(a, k):
    count = 0
    for i in range(len(a)):
        for j in range(i +1, len(a)):
            if (a[i] + a[j]) % k == 0:
                count += 1
    return count
# O[n*logn] time
# O[1] space
def sumsDivisibleByK(a, k):
    count = 0 #empty count variable
    seen = {} #empty dictionary

    for i in a:                     #loop through each element
        remainder = i % k           #find the first half of the puzzle
        if remainder == 0:          
            seek = 0 #             #if a multiple of k, pair with other multiples
        else:
            seek = k - remainder    #else, pair with compliments (second half to the puzzle) 
        if seek in seen:
            count += seen[seek]     #if compliments are already there, add all of them to the count
        seen[remainder] = seen.get(remainder, 0) + 1    #increment the compliments by 1 (even if not present yet)
    print(seen)
    return count                    #after all have been checked, return answer

#O[n] time
#O[n] space

a = [1,2,3,4,5]
k = 3
print(sumsDivisibleByK(a, k))

# expect 4