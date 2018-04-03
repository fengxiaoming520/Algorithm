def BruteForceStringMatch(T, P):
    # T stands for text
    # P stands for matching string
    for i in range(0, len(T)-len(P)):
        j = 0
        while j < len(P) and P[j] == T[i+j]:
            j = j+1
            if j == len(P):
                return i

    return -1


T = 'Hello world. My name is CoCo.'
P = 'name'
print(BruteForceStringMatch(T, P))
