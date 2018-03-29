def SequentialSearch(L, num):
    count = []
    j = 0
    for i in L:
        if i == num:
            count.append(j)
        j += 1
    return count

L = [1,2,3,4,5,6,7,8,90,0,6,4]
print(SequentialSearch(L, 6))
