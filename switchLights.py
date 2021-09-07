def switchLights(a):
    flips = 0
    for i in range(len(a)-1, -1, -1):
        if a[i]:
            flips += 1
        a[i] += flips
        print(a)
        a[i] %= 2
        # print(a)
    return a