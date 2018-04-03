def BruteForceClosestPoints(p):
    d = float('inf')
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            d = min(d, ((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2)**0.5)

    return d

p = [(1,1),(2,2),(3,3),(1,4)]
print(BruteForceClosestPoints(p))
