
def GCD(i,j):
    while i != 0 and j!=0:
        if i > j:
            i = i % j
        elif j > i:
            j = j % i
    if i == 0:
        return j
    elif j == 0:
        return i
try:
    while True:
        G = 0
        N = int(input())
        if N == 0:
            break
        for i in range(1,N):
            for j in range(i+1,N+1):
                G += GCD(i,j)
        print(G)
except Exception:
    pass
