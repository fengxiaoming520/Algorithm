def JosephRing(p, m):
    L = [i for i in range(p)]
    count = -1
    while len(L) > 1:
        for i in range(m):
            count += 1
            if count >= len(L):
                count = 0
        del L[count]
    print(L)



JosephRing(1000,3)
    
        
