def GCD(a,b):
    if a == 0 or b == 0:
        if a > b:
            return a
        else:
            return b
    else:
        if a >= b :
            a = a % b
        elif b > a:
            b = b % a
            
        return GCD(a,b)




n = list(map(int,input().split(' ')))
a = n[0]
b = n[1]
print(GCD(a,b))
        
