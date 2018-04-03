def Euclid(m,n):
    # Calculate the gcd(m,n) using the Euclidean algorithm
    while n != 0:
        r = m % n
        m = n
        n = r
    return m

print(Euclid(66,88))
